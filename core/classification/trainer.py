import numpy as np
import os
from core import config_manager
from core.classification_problem import model_builder
from core.classification_problem import data_provider


def train():
    print("Processing...")
    print("==============================================")

    docs = data_provider.get_docs()

    print("Preparing training data ...")
    x_train, y_train = data_provider.get_train_set(dp.get_docs(), words, class_labels)



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

    path = os.path.join('./data/models/model_1/fp.tfl')
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