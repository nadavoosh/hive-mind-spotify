import logging
from app import app

class WebFactionMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = '/hivemindplaylists'
        return self.app(environ, start_response)

if __name__ == '__main__':
    app.run(debug=True)
else:
    app.wsgi_app = WebFactionMiddleware(app.wsgi_app)
