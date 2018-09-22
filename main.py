from flask import Flask
from routes.scanner import scan


app = Flask(__name__)


app.register_blueprint(scan)


if __name__ == '__main__':
    app.run(debug=True)