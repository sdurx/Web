from tg import expose, TGController, AppConfig, request

class RootController(TGController):
     @expose()
     def index(self):
     	ip = request.environ.get("X_FORWARDED_FOR", request.environ["REMOTE_ADDR"])
        return str(ip)

     @expose("hello.jinja")
     def hello(self, person=None):
     	return dict(person=person)

config = AppConfig(minimal=True, root_controller=RootController())
config.renderers = ["jinja"]

application = config.make_wsgi_app()

from wsgiref.simple_server import make_server
import os

print "Serving on port 8000080..."
httpd = make_server('', 8080, application)
httpd.serve_forever()