import bcrypt

from flask import jsonify, make_response
from application import request, SSHTunnelForwarder, pymysql

def login(ec2_dns, db_pass):

    # username = request.json["username"]
    # password = request.json["password"]

    username = "admin"
    password = "admin"

    password = password.encode('utf-8')

    password = bcrypt.hashpw(password, bcrypt.gensalt(10))

    # get_login_query = "SELECT * FROM db.users WHERE Username='" + username + "' AND Password='" + password + "';"
    # get_login_query = "SELECT * FROM db.users WHERE Username=(%(username)s) AND Password=(%(password)s);"

    with SSHTunnelForwarder(
        ec2_dns,
        ssh_username="ec2-user",
        ssh_pkey="db-keys.pem",
        remote_bind_address=("seado-db.cnqarh1c5gpt.us-east-1.rds.amazonaws.com", 3306)
    ) as tunnel:
        tunnel.start()

        conn = pymysql.connect(
            user="admin",
            password=db_pass,
            host="localhost",
            port=tunnel.local_bind_port
        )

        try:
            with conn.cursor() as cur:
                # If the query was successful, 1 will be returned.
                # If the query was unsuccessful, 0 will be returned.
                # response = cur.execute("""SELECT * FROM db.users WHERE Username = %(username)s AND Password = %(password)s""", {'username': username, 'password': password})
                response = cur.execute("""INSERT INTO db.users (Username, Password) VALUES (%(username)s, %(password)s);""", {'username': username, 'password': password})
                conn.commit()
                print(response)
                if response == 1:
                    for row in cur:
                        user_type = row[1]
                else:
                    user_type = "invalid"

        finally:
            conn.close()
            tunnel.close()
    #
    # user_type_return = make_response(jsonify({"user_type": user_type}))
    # user_type_return.headers["Content-Type"] = "application/json"
    # return user_type_return
    return user_type