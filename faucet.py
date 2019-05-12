#!/usr/bin/env python3

from aiohttp import web
from routes import index,claim,status,info
import config

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_static('/js', './www/js/')
    app.router.add_static('/css', './www/css/')
    app.router.add_post('/claim', claim)
    app.router.add_get('/status', status)
    app.router.add_get('/info', info)
    
if __name__ == '__main__':
   try:
      app = web.Application()
      setup_routes(app)
      web.run_app(app, host=config.listen_host, port=config.listen_port)
   except Exception as e:
      print(e)   
