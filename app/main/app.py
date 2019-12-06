import os, inspect
from flask import Flask, redirect

app = Flask(__name__, static_url_path="")
app.static_folder = os.path.dirname(os.path.abspath(inspect.stack()[0][1])) + '/static/dist'


@app.route('/')
def index():
    return redirect('index.html')


@app.route('/dbtest')
def dbtest():
    from common.mysql_util import MysqlUtil
    with MysqlUtil() as my:
        records = my.execute_query('SELECT * FROM favorite_colors')
    return str(records)


@app.route('/originaldbtest')
def original():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'store'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()
    return results


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
