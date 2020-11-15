import pandas as pd
import numpy as np

df=pd.read_csv('Datasets/unemployment-data.csv', sep=',', error_bad_lines=False, index_col=False, dtype='unicode')

df.set_index(list(df)[0], inplace=True)
selectedRows=df.iloc[10:]
selectedRows=selectedRows.T
# selectedRows['2020.0'] = selectedRows['2020.0'].astype(float)
# selectedRows['2020.0'] = selectedRows['2020.0'].astype(int)
selectedRows = selectedRows.rename(columns={'2020.0': '2020'})

selectedRows.to_csv('unemployment-data-cleaned.csv', sep='\t', index=False)
