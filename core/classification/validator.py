import numpy as np
import os
import json
from core.data_provider import DataProvider
from core.config_manager import ConfigurationManager
from core import model_provider as mp


def get_features(docs, cm):
    words = cm.get("words")
    class_labels = cm.get("class_labels")

    # Saving to config file
    # cm.update_config({'words': words})
    # cm.update_config({'class_labels': class_labels})

    return words, class_labels


def get_test_set(docs, words, class_labels):
    test_set = []
    output_empty = [0] * len(class_labels)  # an empty array for our output
    for doc in docs:
        tokens = doc[0]
        bow = mp.get_bag_of_words(tokens, words) ####

        cls = doc[1]
        output_row = list(output_empty)
        output_row[class_labels.index(cls)] = 1

        # training set contains a the bag of words model and the output row that tells
        # which class that bow belongs to.
        test_set.append([bow, output_row])

    # x_train contains the Bag of words and y_train contains the class labels
    test_set = np.array(test_set)
    x_test = list(test_set[:, 0])
    y_test = list(test_set[:, 1])

    return x_test, y_test


def test(model, x_test, y_test, class_labels):
    print("ACTUAL CLASS\tPREDICTED CLASS\t\tCONFIDENCE")
    print("============\t===============\t\t======")
    for x, y in zip(x_test, y_test):
        # x_t = np.array([x])
        #r =  model.evaluate(np.array([x]), np.array([y]))
        #print(r)
        prediction_result = model.predict([x])  # here list representation is important
        rating = compute_rating(prediction_result)

        # fancy stuffs
        predicted_class = class_labels[np.argmax(prediction_result)]
        actual_class = class_labels[y.index(1)]

        print("{0}\t{1}\t\t{2:.2f}".format(actual_class, predicted_class, rating))


def compute_rating(prediction_result):
    # TODO: normalizing to range(0, 1)
    rating = -prediction_result[0][0] + prediction_result[0][1]

    return rating


def main():
    print("Processing...")
    print("==============================================")

    cm = ConfigurationManager()
    dp = DataProvider(f"data/processed/test.csv")

    docs = dp.get_docs()
    words, class_labels = get_features(docs, cm)

    print("Preparing training data ...")
    x_test, y_test = get_test_set(docs, words, class_labels)

    print("Initializing training model ...")
    model = mp.get_model(len(words), len(class_labels))

    path = os.path.join('./data/model/fp.tfl')
    print(f"Loading trained model from {path}")
    model.load(path)

    print(f"Testing initiated ...")
    test(model, x_test, y_test, class_labels)

    print("==============================================")
    print("Done!")


main()



