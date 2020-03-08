from core import data_loader
from core import MODULE_DIR


def get_docs():
    df = data_loader.load_json(f'{MODULE_DIR}/data/processed/fp_ds_2.json')
    df = df.apply(lambda x: (x["entities"], x["value"]), axis=1)
    docs = df.tolist()
    return docs