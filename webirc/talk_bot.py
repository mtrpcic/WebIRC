from twisted.words.protocols import irc
from cgi import escape

class TalkBot(irc.IRCClient):
    def _get_nickname(self):
        return self.factory.nickname
    nickname = property(_get_nickname)
    
    def connectionMade(self):
        self._names = {}
        irc.IRCClient.connectionMade(self)
        self.factory.clients.append(self)

    def signedOn(self):
        self.join(self.factory.channel)
        print "Signed on as %s." % (self.nickname,)

    def joined(self, channel):
        print "Joined %s." % (channel,)
        
    def irc_RPL_NAMREPLY(self, prefix, params):
        """
        Handles the raw NAMREPLY that is returned as an answer to the NAMES command
        Accumulates users until RPL_ENDOFNAMES
        """
        channel = params[2]
        users = params[3].split()
        self._names.setdefault(channel.lower(), []).extend(users)
        
    def irc_RPL_ENDOFNAMES(self, prefic, params):
        """
        Handles the end of the RPL_NAMREPLY.  This is called when all NAMREPLYs have
        finished. It calls the higher-level functions as well as fires the deferreds
        """
        channel = params[1]
        users = self._names.pop(channel, [])
        self.channelNames(channel, users)
        
    def names(self, channel):
        """
        Tells the server to give a list of users in the specified channel
        """
        if channel is not None:
            self._names[channel] = []
            self.sendLine("NAMES %s" % channel)
            
    def privmsg(self, user, channel, msg):
        data = {
            'nickname' : user.split("!")[0],
            'channel'  : channel,
            'message'  : escape(msg),
            'type'     : 'message'
        }
        self.factory.socket_server.send(data)
        
    def action(self, user, channel, msg):
        data = {
            'nickname' : user.split("!")[0],
            'channel'  : channel,
            'message'  : escape(msg),
            'type'     : 'action'
        }
        self.factory.socket_server.send(data)
        
    def userJoined(self, user, channel):
        data = {
            'nickname' : user.split("!")[0],
            'channel'  : channel,
            'type'     : 'join'
        }
        self.factory.socket_server.send(data)
        
    def userLeft(self, user, channel):
        data = {
            'nickname' : user.split("!")[0],
            'channel'  : channel,
            'type'     : 'part'
        }
        self.factory.socket_server.send(data)
        
    def userRenamed(self, oldname, newname):
        data = {
            'old_nickname' : oldname,
            'new_nickname' : newname,
            'type'         : 'rename'
        }
        self.factory.socket_server.send(data)
        
    def userQuit(self, user, message):
        data = {
            'nickname' : user.split("!")[0],
            'message'  : escape(message),
            'type'     : 'quit'
        }
        self.factory.socket_server.send(data)
        
    def channelNames(self, channel, names):
        """
        Called when a list of users in the channel has been requested
        """
        data = {
            'channel' : channel,
            'names'   : names,
            'type'    : 'names'
        }
        self.factory.socket_server.send(data)
        
