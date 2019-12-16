from flask import Flask, redirect, jsonify, request
import os
import inspect
from common.mysql_util import MysqlUtil as Mysql
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, set_access_cookies


app = Flask(__name__, static_url_path="")
app.static_folder = os.path.dirname(
    os.path.abspath(inspect.stack()[0][1])) + '/static/dist'

app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_SECRET_KEY'] = 'secret'

bcrypt = Bcrypt(app)
jwt = JWTManager(app)


@app.route('/')
def index():
    return redirect('index.html')


@app.route('/test')
def test():
    return jsonify({'success': True})


@app.route('/testdb')
@jwt_required
def dbtest():
    with Mysql() as my:
        records = my.fetch_all('SELECT * FROM z_test')
    return jsonify(records)


@app.route('/user/register', methods=['POST'])
def register():
    form = request.get_json()

    sql = '''
        INSERT INTO user ( email, password , name , redid) 
        VALUES ( %s , %s , %s , %s)
    '''
    passenc = bcrypt.generate_password_hash(form['password']).decode('utf-8')
    params = [form['email'], passenc, form['name']]

    sql2 = "SELECT * from user where id = LAST_INSERT_ID()"

    sps = [[sql, params], [sql2]]

    with Mysql() as my:
        result = my.execute_statements(sps)

    return jsonify(result)


@app.route('/user/login', methods=['POST'])
def login():
    form = request.get_json()

    q = "SELECT * FROM user where email = %s"
    params = [form['email']]

    with Mysql() as my:
        record = my.fetch_one(q, params)

    if not bcrypt.check_password_hash(record['password'], form['password']):
        return jsonify({"error": "Invalid username and password"})

    access_token = create_access_token(
        identity={
            'name': record['name'],
            'email': record['email']
        })

    # Set the JWT cookies in the response
    resp = jsonify({'success': True})
    set_access_cookies(resp, access_token)
    return resp, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=50000)
