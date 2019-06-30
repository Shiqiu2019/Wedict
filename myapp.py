from flask import Flask
app = Flask(__name__)

@app.route('/')
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return ['<!DOCTYPE html><html><meta charset="utf-8"><title>It works',
            '</title><h1>It works!</h1>']

if __name__ == '__main__':
    app.run()