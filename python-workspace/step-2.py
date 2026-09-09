import pandas as pd

csv_filepath = r"SEIP_data.csv"

csv_dataframe = pd.read_csv(csv_filepath)

print(csv_dataframe.head())

print(csv_dataframe.info())