import flask


# Create the application.
app = flask.Flask(__name__)


@app.route('/')

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return flask.render_template('index.html')

   

if __name__ == '__main__':
    # app.debug=True
    app.run()