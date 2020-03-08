import os
import pandas as pd
from core import MODULE_DIR

print("Processing ...")
print("==============================================")

df = pd.DataFrame()
data_directory=f'{MODULE_DIR}/data/raw/fp_records_1'
print(f"Loading JSON records from {data_directory}")
directories=os.listdir(data_directory)
for directory in directories:
    temp = 0
    file_names=os.listdir(f"{data_directory}/{directory}")
    for file_name in file_names:
        article=pd.read_json(f'{data_directory}/{directory}/{file_name}',
                             lines=True,
                             encoding='utf8')

        article.drop(labels=['value', 'image'], axis=1, inplace=True)      # removes unnecessary columns
        article['id'] = file_name.split('.', 2)[0]                         # getting id column from the file name
        article['class'] = directory                                       # getting class column from directory name
        article.replace("\n|[ ]{2,}|<.*?>", "", regex=True, inplace=True)  # removes extra spaces, new lines & html tags

        df = df.append(article, sort=True)
        temp = temp + 1
        if temp==250: break

df = df.set_index('id')
df = df.reindex(columns=["class", "category", "section", "entities", "title", "subtitle", "text"])

path=f"{MODULE_DIR}/data/processed/fp_ds_1.csv"
print(f"Writing to CSV at {path}")
df.to_csv(path, encoding='utf8')

path=f"{MODULE_DIR}/data/processed/fp_ds_1.json"
print(f"Writing to JSON at {path}")
resultJSON = df.to_json(orient='records', force_ascii=False)
with open(path, 'w', encoding='utf8') as json_file:
    json_file.write(resultJSON)

print("==============================================")
print("Done!")