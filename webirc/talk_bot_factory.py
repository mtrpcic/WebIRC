from twisted.internet import protocol
from talk_bot import TalkBot

class TalkBotFactory(protocol.ClientFactory):
    protocol = TalkBot
    def __init__(self, channel, socket_server, nickname='mtr_testbot'):
        self.channel = channel
        self.socket_server = socket_server
        self.nickname = nickname
        self.clients = []

    def clientConnectionLost(self, connector, reason):
        print "Lost connection (%s)." % (reason,)
        # The line below forces the bot to rejoin after a graceful quit.
        # Uncomment it to enable auto-reconnecting.
        # connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "Could not connect: %s" % (reason,)
        
    def send_msg(self, msg):
        for client in self.clients:
            client.say(self.channel, str(msg))
            
    def close_connections(self):
        for client in self.clients:
            client.quit()
