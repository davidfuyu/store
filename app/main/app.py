from flask import Flask, redirect, jsonify, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, set_access_cookies, get_jwt_identity
import os
import inspect
import json
from common.mysql_util import MysqlUtil as Mysql
from common import utils


app = Flask(__name__, static_url_path="")
app.static_folder = os.path.dirname(
    os.path.abspath(inspect.stack()[0][1])) + '/static/dist'

app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_SECRET_KEY'] = 'secret'

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

_qop = f"""
    SELECT o.organism_name
        , op.organism_property_id
        , op.property_id
        , p.property_name
        , value
        , opl.user_id
        , s.status_name
    FROM organism_property_log opl
    JOIN organism_property op on opl.organism_property_id = op.organism_property_id
    JOIN organism o ON op.organism_id = o.organism_id
    JOIN property p ON op.property_id = p.property_id
    JOIN status s ON opl.status_id = s.status_id
    WHERE organism_property_log_id = (
        SELECT MAX(organism_property_log_id) 
        FROM organism_property_log opl2
        WHERE opl2.organism_property_id = opl.organism_property_id
        GROUP BY opl2.organism_property_id
        )
"""


@app.route('/')
def index():
    return redirect('index.html')


@app.route('/metrics/general', methods=['GET'])
def metrics():
    with Mysql() as my:
        count_organism = my.fetch("SELECT count(*) AS count FROM organism")
        count_organism_property = my.fetch(
            "SELECT count(*) AS count FROM organism_property")

    records = {
        'count_organism': count_organism,
        'count_organism_property': count_organism_property,
    }

    return utils.generate_success_response([records])


@app.route('/metrics', methods=['GET'])
@jwt_required
def metrics_user():
    token = get_jwt_identity()
    user_id = token['user_id']

    with Mysql() as my:
        count_organism = my.fetch("SELECT count(*) AS count FROM organism")
        count_organism_property = my.fetch(
            "SELECT count(*) AS count FROM organism_property")
        count_verified = my.fetch(f"""
            SELECT count(*) AS count
            FROM organism_property_log 
            WHERE status_id = (SELECT status_id FROM status WHERE status_name = 'verified' limit 1)
            AND user_id = {user_id}
       """)
        count_other = my.fetch(f"""
            SELECT count(*) AS count
            FROM organism_property_log 
            WHERE status_id = (SELECT status_id FROM status WHERE status_name != 'verified' limit 1)
            AND user_id = {user_id}
        """)

    records = {
        'count_organism': count_organism,
        'count_organism_property': count_organism_property,
        'count_verified': count_verified,
        'count_other': count_other
    }

    return utils.generate_success_response([records])


@app.route('/organism', methods=['GET'])
def all_organism():
    q = "SELECT * FROM organism"

    with Mysql() as my:
        records = my.fetch(q)

    return utils.generate_success_response(records)


@app.route('/organism/<int:organism_id>', methods=['GET'])
def get_organism(organism_id):
    q = f"SELECT * FROM organism WHERE organism_id = {organism_id} LIMIT 1"

    with Mysql() as my:
        records = my.fetch(q)

    return utils.generate_success_response(records)


@app.route('/organism', methods=['PUT'])
def set_organism():
    form = request.get_json()

    q1 = f"INSERT INTO organism (organism_name) VALUES (%s);"
    p1 = [form["title"]]
    qp1 = [q1, p1]

    qp2 = ['select * from organism where organism_id = LAST_INSERT_ID()']

    qps = [qp1, qp2]

    with Mysql() as my:
        records = my.execute_statements(qps)

    return utils.generate_success_response(records)


@app.route('/organism-property/<int:organism_id>', methods=['GET'])
@jwt_required
def organism_property(organism_id):
    q = _qop + f" AND op.organism_id = {organism_id}"

    with Mysql() as my:
        records = my.fetch(q)

    return utils.generate_success_response(records)


@app.route('/organism-property/<int:organism_id>', methods=['POST'])
@jwt_required
def set_organism_property(organism_id):
    token = get_jwt_identity()
    user_id = token['user_id']

    form = request.get_json()

    for k in form:
        v = form[k]
        sps = []
        if ('organism_property_id' in v):
            opid = v['organism_property_id']
            q1 = "UPDATE organism_property SET value = %s WHERE organism_property_id = %s"
            p1 = [v["value"], opid]

            q2 = f"""
                INSERT INTO organism_property_log(
                    organism_property_id
                    , user_id
                    , status_id
                ) VALUES (
                    opid
                    , {user_id}
                    , (SELECT status_id FROM status WHERE status_name = 'updated' LIMIT 1)
                )
            """
        else:
            q1 = f"""
                INSERT INTO organism_property (
                    organism_id
                    , property_id
                    , value
                ) VALUES (%s, %s, %s)
            """
            p1 = [v["organism_id"], v["property_id"], v["value"]]

            q2 = f"""
                INSERT INTO organism_property_log(
                    organism_property_id
                    , user_id
                    , status_id
                ) VALUES (
                    LAST_INSERT_ID()
                    , {user_id}
                    , (SELECT status_id FROM status WHERE status_name = 'input' LIMIT 1)
                )
            """

        sps.append([q1, p1])
        sps.append([q2])
        with Mysql() as my:
            my.execute_statements(sps)

    q = _qop + f" AND op.organism_id = {organism_id}"

    with Mysql() as my:
        records = my.fetch(q)

    return utils.generate_success_response(records)


@app.route('/organism-property/<int:organism_id>/verify', methods=['POST'])
@jwt_required
def verify_organism_property(organism_id):
    token = get_jwt_identity()
    user_id = token['user_id']

    form = request.get_json()

    for row in form:
        opid = row['organism_property_id']

        q = f"""
            INSERT INTO organism_property_log(
                organism_property_id
                , user_id
                , status_id
            ) VALUES (
                {opid}
                , {user_id}
                , (SELECT status_id FROM status WHERE status_name = 'verified' LIMIT 1)
            )
        """

        with Mysql() as my:
            my.execute(q)

    q = _qop + f" AND op.organism_id = {organism_id}"

    with Mysql() as my:
        records = my.fetch(q)

    return utils.generate_success_response(records)


@app.route('/category', methods=['GET'])
def all_category():
    q = "SELECT * FROM property_category ORDER BY property_category_order"

    with Mysql() as my:
        records = my.fetch(q)
    return utils.generate_success_response(records)


@app.route('/property')
def all_property():
    q = """
        SELECT 
            p.*
            , pc.property_category_name
            , pt.property_type_name
        FROM property p
        JOIN property_category pc on p.property_category_id = pc.property_category_id
        JOIN property_type pt on p.property_type_id = pt.property_type_id
    """

    with Mysql() as my:
        records = my.fetch(q)

    return utils.generate_success_response(records)


@app.route("/user/register", methods=["POST"])
def register():
    form = request.get_json()

    sql = """
        INSERT INTO user ( email, password , name) 
        VALUES ( %s , %s , %s)
    """
    passenc = bcrypt.generate_password_hash(form["password"]).decode("utf-8")
    params = [form["email"], passenc, form["name"]]

    sql2 = "SELECT * from user where user_id = LAST_INSERT_ID()"

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
        record = my.fetchone(q, params)

    if not bcrypt.check_password_hash(record['password'], form['password']):
        return jsonify({"error": "Invalid username and password"})

    access_token = create_access_token(
        identity={
            'user_id': record['user_id'],
            'name': record['name'],
            'email': record['email']
        })

    result = {
        'success': True,
        'records': {
            'user_id': record['user_id'],
            'name': record['name'],
            'email': record['email']
        }
    }

    # resp = jsonify({'success': True})
    resp = jsonify(result)

    # Set the JWT cookies in the response
    set_access_cookies(resp, access_token)
    return resp, 200


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=50000)
