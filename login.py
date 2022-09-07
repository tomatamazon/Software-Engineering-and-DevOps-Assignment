from flask import jsonify, make_response
from application import request, SSHTunnelForwarder, pymysql

def login(ec2_dns, db_pass, db_keys):

    print("ec2_dns is", ec2_dns)
    print("DB pass is", db_pass)
    print("DB key is", db_keys)
    print("Type of DB pass is", type(db_pass))
    print("Type of DB key is", type(db_keys))

    username = request.json["username"]
    password = request.json["password"]

    get_login_query = "SELECT * FROM /* DATABASE.table */ WHERE Username='" + username + "' AND Password='" + password + "';"
    # Add some security on this line above so that SQL Injections cannot be carried out.

    with SSHTunnelForwarder(
        ec2_dns,
        ssh_username="ec2-user",
        ssh_pkey=db_keys,
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
                response = cur.execute(get_login_query)
                if response == 1:
                    for row in cur:
                        user_type = row[1]
                else:
                    user_type = "invalid"

        finally:
            conn.close()
            tunnel.close()

    user_type_return = make_response(jsonify({"user_type": user_type}))
    user_type_return.headers["Content-Type"] = "application/json"
    return user_type_return