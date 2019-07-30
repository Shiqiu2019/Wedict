from flask import Flask, render_template, request, json
import pymysql.cursors
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        allwords = {}

        connection = pymysql.connect(# unix_socket='/srv/run/mysqld/mysqld.sock',
                                     host='localhost',
                                     user = 'testuser',
                                     # user='root',
                                     password='test123',
                                     db='formdb',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
             # Connect to the database MySQL


            with connection.cursor() as cursor:
                # Create a new recrod
                word = result['word']
                meaning = result['meaning']
                sql = 'INSERT INTO sqdict (word, meaning) VALUES (%s, %s)'
                cursor.execute(sql, (word, meaning))  # execute 别忘了

            # connection is not autocommit by default. So you must commit to save your changes.
            connection.commit()

            with connection.cursor() as cursor:
                sql = 'SELECT * from sqdict'
                cursor.execute(sql)
                # sqlresult = cursor.fetchone()  # only show the first row
                sqlresult = cursor.fetchall()  # all rows
                print('sqlresult')
                print(sqlresult)
                allwords = sqlresult

        except Exception as e:
            return e

        finally:
            connection.close()

        print('allwords')
        print(allwords)

        return render_template("result.html",result = result, allwords = allwords)



    else:
        return 'note: request.method is GET'


@app.route('/testpage')
def testpage():
    return render_template('testpage.html')


@app.route('/test',methods = ['POST', 'GET'])
def test():
    if request.method == 'POST':
        word = 'default'
        meaning = 'defaultmeaning'
        allwords = {}

        # Connect to the database MySQL
        connection = pymysql.connect(unix_socket='/srv/run/mysqld/mysqld.sock',
                                     host='localhost',
                                     # user = 'testuser',
                                     user='root',
                                     # password='test123',
                                     db='formdb',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Create a new recrod
                word = request.form.get('word')
                print('word')
                print(word)
                meaning = request.form.get('meaning')
                sql = 'INSERT INTO sqdict (word, meaning) VALUES (%s, %s)'
                cursor.execute(sql, (word, meaning))  # execute 别忘了

            # connection is not autocommit by default. So you must commit to save your changes.
            connection.commit()

            with connection.cursor() as cursor:
                sql = 'SELECT * from sqdict'
                cursor.execute(sql)
                # sqlresult = cursor.fetchone()  # only show the first row
                sqlresult = cursor.fetchall()  # all rows
                print('sqlresult')
                print(sqlresult)
                allwords = sqlresult

        except Exception as e:
            return e

        finally:
            connection.close()

        print('allwords')
        print(allwords)

        return render_template("testresult.html",word = word, meaning = meaning, allwords = allwords)



    else:
        return 'note: request.method is GET'


@app.route('/testchinese')
def testchinese():
    return '测试中文 已疯'

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(debug = False)
