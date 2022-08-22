from flask import Flask

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Flask app is running!"

if __name__ == "__main__":
    app.run()