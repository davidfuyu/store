from flask import Flask, redirect, jsonify, request
import os
import inspect
from common.mysql_util import MysqlUtil as Mysql
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token


app = Flask(__name__, static_url_path="")
app.static_folder = os.path.dirname(
    os.path.abspath(inspect.stack()[0][1])) + '/static/dist'

app.config['JWT_SECRET_KEY'] = 'secret'

bcrypt = Bcrypt(app)
jwt = JWTManager(app)


@app.route('/')
def index():
    return redirect('index.html')


@app.route('/dbtest')
def dbtest():
    with Mysql() as my:
        records = my.fetch_all('SELECT * FROM users')
    return jsonify(records)


@app.route('/user/register', methods=['POST'])
def register():
    form = request.get_json()

    sql = '''
        INSERT INTO users ( email, password , name , redid) 
        VALUES ( %s , %s , %s , %s)
    '''
    params = [form['email']
        , bcrypt.generate_password_hash(form['password']).decode('utf-8')
        , form['name']
        , form['redid'] if 'redid' in form else None
    ]

    sql2 = "SELECT * from users where id = LAST_INSERT_ID()"

    sps = [[sql, params], [sql2]]

    with Mysql() as my:
        result = my.execute_statements(sps)

    return jsonify(result)


@app.route('/user/login', methods=['POST'])
def login():
    form = request.get_json()

    q = "SELECT * FROM users where email = %s"
    params = [form['email']]

    with Mysql() as my:
        rv = my.fetch_one(q, params)

    print(rv)

    if bcrypt.check_password_hash(rv['password'], form['password']):
        access_token = create_access_token(
            identity={
                'name': rv['name'],
                'email': rv['email']
            })
        result = access_token
    else:
        result = jsonify({"error": "Invalid username and password"})

    return result


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=50000)
