import pandas as pd
import numpy as np
import os

# 1. Merge datim org unit to pivot on keycode 
orgunit = [file for file in os.listdir('orgunits')]
df_orgunit = pd.read_csv(os.path.join('orgunits', orgunit[0]))
datim_dataelements = [file for file in os.listdir('datim_dataelements')]
datim_file = os.path.join('datim_dataelements', datim_dataelements[0])
df_datim = pd.read_csv(datim_file, encoding='ISO-8859-1')
files = os.listdir('initial_files')
count = 0
for file in files:
    count += 1
    df2 = pd.read_csv(os.path.join('initial_files', file))
    df2 = df2.replace(np.nan, '', regex=True)
    # Removing whitespace at the begining of dataframe
    df2.columns = df2.columns.str.lstrip()

    df = pd.merge(df_orgunit, df2, on='Keycode', how='inner')
    df.to_csv('files_with_orgunits/file'+ str(count) + '.csv', index=False)
  
    print(f'File{count}:{file}')

    df = pd.read_csv('files_with_orgunits/file'+ str(count) + '.csv')

# 2. Unpivot columns
    columns = df.loc[:,~df.columns.isin(
    ['Keycode', 'period','orgunitlevel2', 'orgunitlevel3', 'dhis_organisationunitid',
     'dhis_organisationunitname', 'datim_organisationunitid', 'datim_organisationunitname'
     ])]

    column_list = [x for x in columns]

    df_unpivoted = df.melt(
       id_vars =  ['Keycode', 'period',	'orgunitlevel2', 'orgunitlevel3', 'dhis_organisationunitid',
                   'dhis_organisationunitname', 'datim_organisationunitid', 'datim_organisationunitname'
                 ], 
        value_vars = column_list,
        var_name = 'dataelement'
    )

    df_unpivoted.to_csv('transformed_files/file'+ str(count) + '.csv', index=False)
    # datim_datalements = pd.read_csv('DataelementsUpdated.csv', encoding='ISO-8859-1')
    # datim_datalements = pd.read_csv('datim_dataelements.csv')
    df = pd.read_csv('transformed_files/file'+ str(count) + '.csv')

    df_final = pd.merge(df_datim, df, on='dataelement', how='inner')

    df_final.to_csv('final_files/file'+ str(count) + '.csv', index=False)

df_list = []
final_files = os.listdir('final_files')
for final_file in final_files:
    df = pd.read_csv(os.path.join('final_files', final_file))
    df_list.append(df)
final_file = pd.concat(df_list).drop_duplicates().reset_index(drop=True)
final_file.to_csv('merged/final_file.csv', index=False)

df = pd.read_csv('merged/final_file.csv')
df = df[['dataelementuid', 'period', 'datim_organisationunitid', 'categoryoptioncombouid', 'value']]

df.columns = ['dataelement', 'period', 'orgunit', 'categoryoptioncombo', 'value']

values = []
for i in range(df.shape[0]):
    values.append('70212')
print('Merging and transforming to final file....')
# Adding column attributeoptioncombo with values list
df1 = df.assign(attributeoptioncombo = values)

#Change columns order
df = df1.iloc[:, [0,1,2,3,5,4]]

df.to_csv('merged/file_to_import.csv', index=False)
print(f'Process completed! Found {count} initial files! The file to be imported to dev-de is file_to_import.csv')
