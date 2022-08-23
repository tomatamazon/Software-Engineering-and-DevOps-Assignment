from flask import Flask, request, send_from_directory, render_template
from sshtunnel import SSHTunnelForwarder
import pymysql

application = app = Flask(__name__)

@application.route('/')
def home():
    return 'Hello Elastic Beanstalk!'

if __name__ == "__main__":
    application.run()