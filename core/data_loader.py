import ast
import pandas as pd


def load_csv(path) -> pd.DataFrame:
    df = pd.read_csv(path,
                     encoding='utf-8',
                     header=0,
                     index_col=0)

    df['entities'] = df['entities'].apply(lambda x: ast.literal_eval(x))
    return df


def load_json(path) -> pd.DataFrame:
    df = pd.read_json(path,
                      orient='records',
                      encoding='utf-8')
    return df