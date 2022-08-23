from flask import Flask

application = app = Flask(__name__)

@application.route('/')
def home():
    return 'Hello Elastic Beanstalk from Application!'

if __name__ == "__main__":
    application.run()

