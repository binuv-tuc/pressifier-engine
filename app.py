import json
from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def index():
    return 'IT WORKS!'


@app.route('/ds1')
def get_ds1():
    with open('fp_ds_1.json', 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    return Response(json.dumps(data, ensure_ascii=False), mimetype='application/json')


@app.route('/ds2')
def get_ds2():
    with open('fp_ds_2.json', 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    return Response(json.dumps(data, ensure_ascii=False), mimetype='application/json')


if __name__ == "__main__":
    app.run()