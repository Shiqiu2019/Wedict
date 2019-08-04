import sys
import traceback
from flask import Flask, render_template, request, json, flash
from forms import ContactForm, WordEditForm
import pymysql.cursors
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_bootstrap import Bootstrap



app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'secret 1 development key'

# Connect to the database MySQL
connection = pymysql.connect(unix_socket='/srv/run/mysqld/mysqld.sock',
                             host='localhost',
                             # user = 'testuser',
                             user='root',
                             # password='test123',
                             db='formdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


@app.route('/')
def home():
    return render_template('homepage.html',bootstrap = bootstrap)

@app.route('/contactme')
def contactme():
    return render_template('contactme.html')


@app.route('/contact',methods = ['POST', 'GET'])
def contact():
    contactform= ContactForm()
    if request.method == 'POST':
        if contactform.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', contactform = contactform)
        else:
            try:
                # The connection will be closed for you as soon as execution leaves the <with> block, no matter by what route.
                with connection.cursor() as cursor:
                    # Create a new recrod
                    name = contactform.name.data
                    email = contactform.email.data
                    goodatfields = contactform.goodatfields.data
                    comment = contactform.comment.data
                    wechat = contactform.wechat.data
                    # sql = 'INSERT INTO sqdict (word, meaning) VALUES (%s, %s)'
                    sql = 'INSERT INTO contacttb (name, email, goodatfields, comment, wechat) VALUES (%s, %s, %s, %s, %s)'
                    cursor.execute(sql, (name, email, goodatfields, comment, wechat))  # execute 别忘了
                    connection.commit()
                    cursor.close()
                    return 'success'

            except Exception as e:
                traceback.print_exc(limit=1, file=sys.stdout)
    else:
        return render_template('contact.html', contactform = contactform)

@app.route('/edit',methods = ['POST', 'GET'])
def edit():
    wordedit_form = WordEditForm()
    if request.method == 'POST':
        result = request.form
        print('test')
        print(result)
        dict_result = result.to_dict()
        print(dict_result)
        allwords = {}
        try:
            # Connect to the database MySQL
            with connection.cursor() as cursor:
                # Create a new recrod
                word = result['word']
                meaning = result['meaning']
                classify = result['classify']
                sql = 'INSERT INTO sqdict (word, meaning, classify) VALUES (%s, %s, %s)'
                cursor.execute(sql, (word, meaning, classify))  # execute 别忘了
                # connection is not autocommit by default. So you must commit to save your changes.
                connection.commit()
                cursor.close()

            with connection.cursor() as cursor:
                sql = 'SELECT * from sqdict'
                cursor.execute(sql)
                # sqlresult = cursor.fetchone()  # only show the first row
                sqlresult = cursor.fetchall()  # all rows
                print('sqlresult')
                # print(sqlresult)
                allwords = sqlresult
                cursor.close()

        except Exception as e:
            traceback.print_exc(limit=1, file=sys.stdout)
        print('allwords')
        print(allwords)
        return render_template("result.html",dict_result = dict_result, allwords = allwords)
    else:
        return render_template('edit.html', wordedit_form=wordedit_form)

@app.route('/links')
def links():
    return render_template('links.html')



if __name__ == '__main__':
    # app.config['JSON_AS_ASCII'] = False what does it mean?
    app.run(debug = False)
