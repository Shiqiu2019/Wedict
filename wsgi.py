def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return ['<!DOCTYPE html><html><meta charset="utf-8"><title>It works',
            '</title><h1>It works!!!!!!shiqiu20190630</h1>']
