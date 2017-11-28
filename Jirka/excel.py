import pandas as pd

with open('import.csv', errors='ignore') as file:
    df = pd.read_csv(file, header=0)
    df_columns = df.columns[2:]
    new_df = pd.DataFrame(columns=["Kdo", "Datum", "Co", "Kolik"])
    i = 0
    for index, row in df.iterrows():
        for column in df_columns:
            if float(row[column]) > 0:
                #     new_df.append([row['Kdo'], row['Datum'], column, row[column]])
                new_df.loc[i] = ([row['Kdo'], row['Datum'], column, row[column]])
                i += 1

with open('export.csv', 'w') as file:
    new_df.to_csv(file)
