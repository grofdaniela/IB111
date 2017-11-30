import pandas as pd
import operator

with open('sherlock-holmes.txt', errors='ignore') as file:
    d = {}
    file = file.read()
    for word in file.split(' '):
        if len(word) > 3:
            if word in d.keys():
                d[word] += 1
            else:
                d[word] = 1
    sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    # print(sorted_d[:5])


with open('jmena.csv', errors='ignore') as file:
    df = pd.read_csv(file)
    df_columns = list(df)[1:]
    dict = {}
    for col in df_columns:
        dict[col] = df.groupby('JMÉNO').max()
    print(dict)
