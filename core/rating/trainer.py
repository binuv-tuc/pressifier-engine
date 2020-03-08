from core import data_loader
from core import MODULE_DIR
import pandas as pd
import tflearn
import tensorflow as tf

def train():
    print("Processing...")
    print("==============================================")

    docs = pd.read_csv(f'{MODULE_DIR}/train/train.csv')

    print("Preparing training data ...")
    x_train, y_train = get_train_set(dp.get_docs(), words, class_labels)



    print("Initializing training model ...")
    # reset underlying graph data
    tf.reset_default_graph()
    # building neural network
    net = tflearn.input_data(shape=[None, len_x], name='input')
    net = tflearn.fully_connected(net, 16, name='dense1')
    net = tflearn.fully_connected(net, 8, name='dense2')
    net = tflearn.fully_connected(net, len_y, activation='softmax')
    net = tflearn.regression(net)

    # define model and setup tensorboard
    model = tflearn.DNN(network=net,
                        # checkpoint_path=os.path.join('./data/model/checkpoints/fp.tfl.ckpt'),
                        tensorboard_dir='./data/model/model_1/tflearn_logs')

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