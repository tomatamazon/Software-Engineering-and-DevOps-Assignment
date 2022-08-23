from flask import Flask

application = Flask(__name__)

# Home route
@application.route('/')
def home():
    return "Hello Elastic Beanstalk from Application!"

if __name__ == "__main__":
    application.run()