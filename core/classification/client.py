import numpy as np
import os
from core import config_manager
from core.classification import model_builder
from core import data_loader
from core import MODULE_DIR


def classify(articles) -> list:
    config = config_manager.get_config()
    words = config['words']
    class_labels = config['class_labels']

    docs = [article['entities'] for article in articles]
    print(docs)
    x_test = []
    for doc in docs:
        x_test.append(model_builder.build_bow(doc, words))

    model = model_builder.build_nn(len(words), len(class_labels))

    path = os.path.join(f"{MODULE_DIR}/models/model_1/fp.tfl")
    model.load(path)

    results = []
    for i, x in enumerate(iterable=x_test, start=1) :
        prediction_result = model.predict([x])  # here list representation is important
        predicted_class = class_labels[np.argmax(prediction_result)]  # fancy stuffs

        result = {"auto_id": i, "class_label": predicted_class}
        results.append(result)

    return results


def main():
    df = data_loader.load_json('inputs.json')
    articles = df.to_dict(orient='records')
    print(classify(articles))


if __name__ == '__main__':
    main()
