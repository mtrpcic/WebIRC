from twisted.words.protocols import irc

class TalkBot(irc.IRCClient):
    def _get_nickname(self):
        return self.factory.nickname
    nickname = property(_get_nickname)
    
    def connectionMade(self):
        irc.IRCClient.connectionMade(self)
        self.factory.clients.append(self)

    def signedOn(self):
        self.join(self.factory.channel)
        print "Signed on as %s." % (self.nickname,)

    def joined(self, channel):
        print "Joined %s." % (channel,)

    def privmsg(self, user, channel, msg):
        data = {
            'nickname' : user.split("!")[0],
            'channel'  : channel,
            'message'  : msg,
            'type'     : 'message'
        }
        self.factory.socket_server.send(data)
        
    def action(self, user, channel, msg):
        data = {
            'nickname' : user.split("!")[0],
            'channel'  : channel,
            'message'  : msg,
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
            'message'  : message,
            'type'     : 'quit'
        }
        self.factory.socket_server.send(data)
