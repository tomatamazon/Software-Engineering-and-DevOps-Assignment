from flask import Flask, request, send_from_directory, render_template
from sshtunnel import SSHTunnelForwarder
import json
import pymysql
import boto3
import base64
from botocore.exceptions import ClientError
import get_pass, login, create_ticket, get_entries, update_entry, delete_entry

application = app = Flask(__name__, static_url_path='', static_folder='frontend/build')
ec2_dns = "ec2-54-89-239-77.compute-1.amazonaws.com"
db_pass = get_pass.get_pass(boto3, base64, ClientError)

db_pass_to_dict = json.loads(db_pass)
db_pass = db_pass_to_dict["password"]

@application.route("/", defaults={'path': ''})
def home(path):
    return send_from_directory(application.static_folder, "index.html")

@application.route("/login", methods=["POST"])
def login_func():
    user_type = login.login(ec2_dns, db_pass)
    return user_type

@application.route("/post_data", methods=["POST"])
def create_ticket_func():
    create_ticket_status = create_ticket.create_ticket(ec2_dns, db_pass)
    return create_ticket_status

@application.route("/get_entries", methods=["POST"])
def get_database_entries_func():
    entries = get_entries.get_entries(ec2_dns, db_pass)
    return entries

@application.route("/update_entry", methods=["POST"])
def update_entries_func():
    update_entry_status = update_entry.update_entry(ec2_dns, db_pass)
    return update_entry_status

@application.route("/delete_entry", methods=["POST"])
def delete_entries_func():
    delete_entry_status = delete_entry.delete_entry(ec2_dns, db_pass)
    return delete_entry_status