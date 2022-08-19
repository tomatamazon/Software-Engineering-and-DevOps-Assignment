from flask import Flask

app = Flask(__name__)

# Home route
@app.route('/test')
def test():
    return {"test": ["test1", "test2", "test3"]}

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)