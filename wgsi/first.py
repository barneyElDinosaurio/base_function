# -*-coding=utf-8-*-

def application(environ, start_response):
    start_response('255 OK',[('Content-Type','text/html')])
    body = '<h1>Hello %s !' %(environ['PATH_INFO'])
    return [body.encode('utf-8')]

