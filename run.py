from twisted.web import server, static
from twisted.internet import reactor
from ConfigParser import SafeConfigParser
from txwebsockets import WebSocketFactory

import webirc
from webirc.socket_server import SocketServer
from webirc.web import home, chat

if __name__ == "__main__":
    print "Starting WebIRC v%s" % webirc.version
    socket_server = SocketServer()
    socket_factory = WebSocketFactory(socket_server)
    
    root = home.Home()
    root.putChild('styles', static.File("./styles"))
    root.putChild('scripts', static.File("./scripts"))
    root.putChild('irc', chat.Chat(socket_server))
    site = server.Site(root)
    
    reactor.listenTCP(8888, socket_factory)
    reactor.listenTCP(8080, site)
    reactor.run()
    
    
