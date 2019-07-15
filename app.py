from flask import Flask, render_template
from flask_mysqldb import MySQL



app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'testuser'
app.config['MYSQL_PASSWORD'] = 'test123'
app.config['MYSQL_DB'] = 'formdb'

mysql = MYSQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        details = request.form
        firstName = details['fname']
        lastname = details['lname']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)', (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success' 
    return render_template('index.html')

if __name__ == '__main__':
    # app.debug = True
    app.run()
