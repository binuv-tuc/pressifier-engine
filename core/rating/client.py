import random


def rate(articles) -> list:
    results = []
    for i, x in enumerate(iterable=articles, start=1):
        results.append({"auto_id": i, "rating": round(random.random(), 2)})
    return results
