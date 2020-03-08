import numpy as np
import os
from core import config_manager
from core import data_provider
from core import model_builder
from core import MODULE_DIR


def extract_features(docs):
    words = []
    class_labels = []
    for doc in docs:
        words.extend(doc[0])
        class_labels.append(doc[1])
    words = sorted(set(words))
    class_labels = sorted(set(class_labels))

    # Saving to config file
    config = config_manager.get_config()
    config['words'] = words
    config['class_labels'] = class_labels
    config_manager.save_config(config)

    return words, class_labels


def get_train_set(docs, words, class_labels):
    train_set = []
    output_empty = [0] * len(class_labels)  # an empty array for our output
    for doc in docs:
        tokens = doc[0]
        bow = mp.get_bag_of_words(tokens, words)

        cls = doc[1]
        output_row = list(output_empty)
        output_row[class_labels.index(cls)] = 1

        # training set contains a the bag of words model and the output row that tells
        # which class that bow belongs to.
        train_set.append([bow, output_row])

    # shuffling features
    # random.shuffle(train_set)
    export_trainset(train_set)
    exit()

    # x_train contains the Bag of words and y_train contains the class labels
    train_set = np.array(train_set)

    x_train = list(train_set[:, 0])
    y_train = list(train_set[:, 1])

    return x_train, y_train


def export_trainset(train_set):
    with open('train.csv', 'w') as file:
        train_set_str = ''
        for row in train_set:
            for col in row:
                train_set_str = train_set_str + f'[{", ".join([str(i) for i in col])}], '
            train_set_str = train_set_str[:-2]
            train_set_str = train_set_str + '\n'
            # break
        file.write(train_set_str)


def train():
    print("Processing...")
    print("==============================================")

    docs = data_provider.get_docs_2()
    words = extract_features(docs)

    print("Preparing training data ...")
    x_train, y_train = get_train_set(docs, words)

    print("Initializing training model ...")
    model = model_builder.build_nn(len(x_train[0]), len(y_train[0]))

    print("Training started  ...")
    # Applying gradient descent algorithm
    model.fit(x_train,
              y_train,
              n_epoch=10,
              batch_size=8,
              show_metric=True
    )

    path = f'{MODULE_DIR}/data/models/model_2/fp.tfl'
    print(f"Saving model at {path}")
    model.save(path)

    # print(f"Evaluating model ...")
    # x_test = x_train[630:640]
    # y_test = y_train[630:640]
    # result = []
    # for x, y in zip(x_test, y_test):
    #     result.extend(model.evaluate(np.array([x]), np.array([y])))
    # print(result)
    #x_test, y_test = dp.get_test_set()
    #mp.get_score(model, x_test, y_test)
    # mp.get_score(model, np.array(x_test), np.array(y_test))

    print("==============================================")
    print("Done!")