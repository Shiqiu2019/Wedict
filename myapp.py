import flask


# Create the application.
app = flask.Flask(__name__)


@APP.route('/')
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return flask.render_template('index.html')

'''         
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')
'''

if __name__ == '__main__':
    # APP.debug=True
    app.run()