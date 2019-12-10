from flask import Flask, redirect, jsonify, request
import os
import inspect
from common.mysql_util import MysqlUtil


app = Flask(__name__, static_url_path="")
app.static_folder = os.path.dirname(
    os.path.abspath(inspect.stack()[0][1])) + '/static/dist'


@app.route('/')
def index():
    return redirect('index.html')


@app.route('/dbtest')
def dbtest():
    with MysqlUtil() as my:
        # records = my.execute_one('SELECT * FROM colors')
        records = my.execute_one('SELECT * FROM users')
    return jsonify(records)


@app.route('/user/register', methods=['POST'])
def register():
    form = request.get_json()

    sql = '''
        INSERT INTO users ( username , password , email , name , redid) 
        VALUES ( %s , %s , %s , %s , %s)
    '''
    params = [form['username']
        , form['password']
        , form['email']
        , form['name']
        , form['redid'] if 'redid' in form else None
    ]

    sql2 = "SELECT * from users where id = LAST_INSERT_ID()"

    sps = [[sql, params], [sql2]]

    with MysqlUtil() as my:
        result = my.execute_statements(sps)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=50000)
