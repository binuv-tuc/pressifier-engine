import json
from flask import Flask, Response, request
import hashlib

app = Flask(__name__)


@app.route('/')
def index():
    return 'IT WORKS!'


@app.route('/api/ds1', methods=['POST'])
def get_ds1():
    if authenticated():
        with open('fp_ds_1.json', 'r', encoding='utf-8') as fp:
            data = json.load(fp)
        return Response(json.dumps(data), mimetype='application/json')
    return Response(status=401)


@app.route('/api/ds2', methods=['POST'])
def get_ds2():
    if authenticated():
        with open('fp_ds_2.json', 'r', encoding='utf-8') as fp:
            data = json.load(fp)
        return Response(json.dumps(data), mimetype='application/json')
    return Response(status=401)


@app.route('/api/rating', methods=['POST'])
def get_rating():
    if authenticated():
        data = {
            'article': 100019,
            'class': 'negative',
            'rating': 0.59
        }
        return Response(json.dumps(data), mimetype='application/json')
    return Response(status=401)


def authenticated():
    if 'binuv' in request.headers:
        for i in ['b', 'i', 'n', 'u', 'v']:
            result = hashlib.md5(i.encode('utf-8'))
            if request.headers.get('binuv') == result.hexdigest():
                return True
    return False


if __name__ == "__main__":
    app.run()