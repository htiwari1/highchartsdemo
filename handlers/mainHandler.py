from tornado.web import RequestHandler

class MainHandler(RequestHandler):

    def get(self):
        title = "Demo"
        template = "main.html"
        self.render(template_name=template,
                    title=title)
