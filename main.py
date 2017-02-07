import sys
import os
import json
import tornado
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url, StaticFileHandler
from handlers import MainHandler


def make_app():
    # some web application settings
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "template_path": os.path.join(os.path.dirname(__file__), "templates")
    }

    # this is where url patterns are matched to different handlers
    # except for the SampleHandler, we want to create a separate file for each
    # handler class
    return Application([
        url(r"/", MainHandler, name='index'),
    ], **settings)
    # ], debug=True, **settings)


def main():
    print("starting Tornado...")
    if len(sys.argv) < 2:
        port = 8000
    else:
        port = sys.argv[1]
    # instantiate a web application
    app = make_app()
    # bind the web application to port
    app.listen(int(port))
    # run the web application
    IOLoop.current().start()


# program entry point
if __name__ == '__main__':
    main()