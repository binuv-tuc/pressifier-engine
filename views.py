import json
from flask import Response, request
import hashlib
from core.classification import client as classifier
from core.rating import client as rater


def index():
    return 'IT WORKS!'


def get_articles():
    print(request.args)
    if authenticated():
        ds = int(request.args.get('ds')) if 'ds' in request.args else 0
        offset = int(request.args.get('offset')) if 'offset' in request.args else 0
        limit = int(request.args.get('limit')) if 'limit' in request.args else 0

        if ds == 1:
            path = 'core/data/processed/fp_ds_1.json'
        elif ds == 2:
            path = 'core/data/processed/fp_ds_2.json'
        else:
            return Response(status=404)

        with open(path, 'r', encoding='utf-8') as fp:
            articles = json.load(fp)

        start = offset
        end = len(articles) if limit == 0 else offset+limit
        articles = articles[start: end]

        resp = {
            'count': len(articles),
            'articles': articles
        }
        return Response(json.dumps(resp), mimetype='application/json')

    return Response(status=401)


def classify_articles():
    if authenticated():
        articles = json.loads(request.data)
        if isinstance(articles, dict):
            articles = [articles]

        result = classifier.classify(articles)  # a dict
        if len(result) == 1:
            result = result[0]

        return Response(json.dumps(result), mimetype='application/json')
    return Response(status=401)


def rate_articles():
    if authenticated():
        articles = json.loads(request.data)
        if isinstance(articles, dict):
            articles = [articles]

        result = rater.rate(articles)  # a list of dict
        if len(result) == 1:
            result = result[0]

        return Response(json.dumps(result), mimetype='application/json')
    return Response(status=401)


# Not a view
def authenticated():
    if 'binuv' in request.headers:
        for i in ['b', 'i', 'n', 'u', 'v']:
            result = hashlib.md5(i.encode('utf-8'))
            if request.headers.get('binuv') == result.hexdigest():
                return True
    return False