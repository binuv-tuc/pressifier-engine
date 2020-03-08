import os
import pandas as pd
from core import MODULE_DIR

print("Processing ...")
print("==============================================")

df = pd.DataFrame()
data_directory = f'{MODULE_DIR}/data/raw/fp_records_2'
print(f"Loading JSON records from {data_directory}")
file_names = os.listdir(data_directory)
temp_count=1
for file_name in file_names:
    article = pd.read_json(f'{data_directory}/{file_name}',
                         lines=True,
                         encoding='utf8')

    article.drop(labels=['image'], axis=1, inplace=True)                # removes unnecessary columns
    article['id'] = file_name.split('.', 2)[0]                          # getting id column from the file name
    article.replace("\n|[ ]{2,}|<.*?", "", regex=True, inplace=True)    # removes extra spaces, new lines & html tags
    #article['text'] = ''

    df = df.append(article, sort=True)
    temp_count = temp_count+1
    if temp_count==500: break

df = df.set_index('id')
df = df.reindex(columns=["value", "category", "section", "entities", "title", "subtitle", "text"])

# print(df)

path = f'{MODULE_DIR}/data/processed/fp_ds_2.csv'
print(f"Writing CSV at {path}")
df.to_csv(path, encoding='utf-8')

path = f'{MODULE_DIR}/data/processed/fp_ds_2.json'
print(f"Writing JSON at {path}")
resultJSON = df.to_json(orient='records', force_ascii=False)
with open(path, 'w', encoding='utf-8') as json_file:
    json_file.write(resultJSON)


print("==============================================")
print("Done!")