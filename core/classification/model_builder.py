import tflearn
import tensorflow as tf


def build_nn(len_x, len_y):
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
    return model


def build_bow(tokens, words):
    # TODO: stem each token
    # stems = [stemmer.stem(token.lower()) for token in tokens]
    stems = tokens

    bow = []
    for w in words:
        bow.append(1) if w in stems else bow.append(0)

    return bow


def get_score(model, x_test, y_test):
    score = model.evaluate(x_test, y_test)
    print(score)