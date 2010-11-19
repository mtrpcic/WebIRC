from twisted.web import resource
from mako.template import Template
from mako.lookup import TemplateLookup

class Home(resource.Resource):
    isLeaf = False
    
    def getChild(self, name, request):
        if name == '':
            return self
        return resource.Resource.getChild(self, name, request)
        
    def render_GET(self, request):
        return Template(filename="./views/form.html.mako", lookup=TemplateLookup(directories=['.'])).render()
