from core import data_loader
from core import MODULE_DIR


def get_docs():
    df = data_loader.load_json(f'{MODULE_DIR}/data/processed/fp_ds_1.json')
    df = df.apply(lambda x: (x["entities"], x["class"]), axis=1)
    docs = df.tolist()
    return docs


def extract_features(docs):
    words = []
    class_labels = []
    for doc in docs:
        words.extend(doc[0])
        class_labels.append(doc[1])
    words = sorted(set(words))
    class_labels = sorted(set(class_labels))

    # Saving to config file
    cm.save({'words': words})
    cm.save({'class_labels': class_labels})

    return words, class_labels


def build_train_set(docs, words, class_labels):
    train_set = []
    output_empty = [0] * len(class_labels)  # an empty array for our output
    for doc in docs:
        tokens = doc[0]
        bow = model_builder.build_bow(tokens, words)

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
