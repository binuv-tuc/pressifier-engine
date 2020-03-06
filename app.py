import json
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    data = {'a': 10}
    return json.dumps(data)


if __name__ == "__main__":
    app.run()