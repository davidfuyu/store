from flask import Flask, redirect, jsonify, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, set_access_cookies
import os
import inspect
from common.mysql_util import MysqlUtil as Mysql
from common import utils


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


@app.route('/property-category')
def all_category():
    q = ''' SELECT * FROM property_category ORDER BY property_category_order'''
    with Mysql() as my:
        records = my.fetch_all(q)
    return utils.generate_success_response(records)


@app.route('/organism')
def all_organism():
    q = "SELECT * FROM organism"
    with Mysql() as my:
        records = my.fetch_all(q)

    return utils.generate_success_response(records)


@app.route('/organism/<int:organism_id>', methods=['GET'])
def get_organism(organism_id):
    q = f"SELECT * FROM organism WHERE organism_id = {organism_id} LIMIT 1"
    with Mysql() as my:
        records = my.fetch_one(q)

    return utils.generate_success_response(records)


@app.route('/organism-property/<int:organism_id>', methods=['GET'])
def organism_property(organism_id):
    q = f"""
        SELECT o.name
            , op.property_id
            , p.property_name
            , value
        FROM organism_property op
        JOIN organism o ON op.organism_id = o.organism_id
        JOIN property p ON op.property_id = p.property_id
        WHERE op.organism_id = {organism_id}
    """
    with Mysql() as my:
        records = my.fetch_all(q)

    return utils.generate_success_response(records)


@app.route('/property')
def all_property():
    q = '''
        SELECT p.*, pc.property_category_name, pc.property_category_order, pt.property_type_name
        FROM property p
        JOIN property_category pc on p.property_category_id = pc.property_category_id
        JOIN property_type pt on p.property_type_id = pt.property_type_id
    '''
    with Mysql() as my:
        records = my.fetch_all(q)
    return utils.generate_success_response(records)


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

    return utils.generate_success_response(result)


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
