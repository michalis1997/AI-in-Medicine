import pandas as pd
import zipfile
import os
# Download
os.system("kaggle datasets download -d fedesoriano/stroke-prediction-dataset")

# Unzip
with zipfile.ZipFile("stroke-prediction-dataset.zip", 'r') as zip_ref:
    zip_ref.extractall("stroke_dataset")

df = pd.read_csv("stroke_dataset/healthcare-dataset-stroke-data.csv")
print(df.head())