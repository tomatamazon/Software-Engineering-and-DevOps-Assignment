from flask import Flask

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Hello Elastic Beanstalk!"

if __name__ == "__main__":
    app.run()