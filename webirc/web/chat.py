from twisted.web import resource
from webirc.talk_bot_factory import TalkBotFactory
from mako.template import Template
from mako.lookup import TemplateLookup
from twisted.internet import reactor

class Chat(resource.Resource):
    isLeaf = True
    def __init__(self, socket_server):
        self.socket_server = socket_server
        
    def render_POST(self, request):
        server = request.args['server'][0]
        port = int(request.args['port'][0])
        channel = request.args['channel'][0]
        nickname = request.args['nickname'][0]
        
        bot_factory = TalkBotFactory(channel, self.socket_server, nickname)
        self.socket_server.bot_factory = bot_factory
        reactor.connectTCP(server, port, bot_factory)
        return Template(filename="./views/show.html.mako", lookup=TemplateLookup(directories=['.'])).render(channel=channel, nickname=nickname, server=server)
