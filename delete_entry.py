from flask import jsonify, make_response
from application import request, SSHTunnelForwarder, pymysql

def delete_entry(ec2_dns, db_pass):
    entry_id = request.json["id"]

    entry_id = str(entry_id)

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
                # If the query is successful, a 1 will be returned.
                # If the query is unsuccessful, a 0 will be returned.
                response = cur.execute("""DELETE FROM db.ticket_info WHERE ID = %(entry_id)s""", {'entry_id': entry_id})
                conn.commit()
                if response == 1:
                    delete_ticket_status = "success"
                else:
                    delete_ticket_status = "invalid"

        finally:
            conn.close()
            tunnel.close()

    delete_ticket_status_response = make_response(jsonify({"delete_entry_status": delete_ticket_status}))
    delete_ticket_status_response.headers["Content-Type"] = "application/json"
    return delete_ticket_status_response