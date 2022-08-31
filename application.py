from flask import Flask, request, send_from_directory, render_template
from sshtunnel import SSHTunnelForwarder
import pymysql
import open_pass

application = app = Flask(__name__, static_url_path='', static_folder='frontend/build')
ec2_dns = "ec2-54-89-239-77.compute-1.amazonaws.com"
db_pass = open_pass.get_pass()

@application.route("/", defaults={'path': ''})
def home(path):
    return send_from_directory(application.static_folder, "index.html")

# if __name__ == "__main__":
#     application.run()