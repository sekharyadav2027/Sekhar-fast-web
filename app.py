from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome Abhishek 🚀</h1>
    <p>This is my first website</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
