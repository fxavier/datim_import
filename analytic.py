import pandas as pd
import numpy as np
import os
import uuid

df_list = []
final_files = os.listdir('transformed_files')
for final_file in final_files:
    df = pd.read_csv(os.path.join('transformed_files', final_file))
    df_list.append(df)
final_file = pd.concat(df_list).drop_duplicates().reset_index(drop=True)
final_file.to_csv('pivots/merged_initial_files.csv', index=False)

df1 = pd.read_csv(os.path.join('pivots/merged_initial_files.csv'))

pivot_province = df1.pivot_table(values="value", index="orgunitlevel2", columns="dataelement", aggfunc="sum")

pivot_province.to_csv('pivots/pivoted_province_level.csv')

pivot_fac =  df1.pivot_table(
       values="value",
       index="dhis_organisationunitname",
       columns="dataelement",
       aggfunc="sum"
       )
pivot_fac.to_csv('pivots/pivoted_Facility_level.csv')