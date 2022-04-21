import pandas as pd
import numpy as np
import os

# 1. Merge datim org unit to pmtct pivot on keycode 
# for i in range(1, 5):
# df_list = []
# for filename in os.listdir('pasta'):
#     df = pd.read_csv(os.path.join('pasta', filename))
#     df_list.append(df)

# df = pd.concat(df_list).drop_duplicates().reset_index(drop=True)

# df.to_csv('pasta/datim_dataelements_mapped.csv')

# datim = os.listdir('datim_dataelements')
# for file in datim:
#     df = pd.read_csv(os.path.join('datim_dataelements', file, encoding='ISO-8859-1'))

#     print(df.head())

# df = pd.read_csv('DataelementsUpdated.csv', encoding='ISO-8859-1')

# print(df.head())

# orgunit = [file for file in os.listdir('orgunits')]
# df1 = pd.read_csv(os.path.join('orgunits', orgunit[0]))
# print(df1.head())
files = os.listdir('initial_files')
print(files)

