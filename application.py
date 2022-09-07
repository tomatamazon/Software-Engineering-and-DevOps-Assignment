from flask import Flask, request, send_from_directory, render_template
from sshtunnel import SSHTunnelForwarder
import json
import pymysql
import boto3
import base64
from botocore.exceptions import ClientError
import get_pass, get_keys, login

application = app = Flask(__name__, static_url_path='', static_folder='frontend/build')
ec2_dns = "ec2-54-89-239-77.compute-1.amazonaws.com"
# db_pass = get_pass.get_pass(boto3, base64, ClientError)

# db_pass_to_dict = json.loads(db_pass)
# db_pass = db_pass_to_dict["password"]

db_pass = "seado-db1!"

# db_keys = get_keys.get_keys(boto3, base64, ClientError)
# db_keys = json.loads(db_keys.read())
# db_keys = db_keys[""]

# FOR TESTING
# pass_file = open("db-pass.txt", 'r')
# db_pass = pass_file.read()
# pass_file.close()

@application.route("/", defaults={'path': ''})
def home(path):
    return send_from_directory(application.static_folder, "index.html")

@application.route("/login", methods=["POST"])
def login_func():
    user_type = login.login(ec2_dns, db_pass)
    return user_type