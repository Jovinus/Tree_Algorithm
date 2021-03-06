# %% Import Module
import pandas as pd
from IPython.display import display
# %% Relation ship
df_orig = pd.read_csv('./sct2_Relationship_Snapshot_INT_20210131.txt', delimiter='\t')
# df_orig = df_orig[df_orig['active'] == 1].reset_index(drop=True)
print(len(df_orig))
display(df_orig.head())

# %% Concept ID
df_concept = pd.read_csv("./sct2_Concept_Snapshot_INT_20210131.txt", delimiter='\t')
df_concept['concept_ID'] = df_concept['id']
df_concept['source_concept_active'] = df_concept['active']
df_concept['destination_concept_active'] = df_concept['active']

print(len(df_concept))
display(df_concept.head())
# %%
print("Before Merge: {}".format(len(df_orig)))

df_orig = pd.merge(df_orig, df_concept[['concept_ID', 'source_concept_active']], left_on=['sourceId'], right_on=['concept_ID'], how='left').drop(columns='concept_ID')
print("Process 1 Result : {}".format(len(df_orig)))

df_orig = pd.merge(df_orig, df_concept[['concept_ID', 'destination_concept_active']], left_on=['destinationId'], right_on=['concept_ID'], how='left').drop(columns='concept_ID')
print("Process 2 Result : {}".format(len(df_orig)))

# %% Discription name
df_name = pd.read_csv('./sct2_Description_Snapshot-en_INT_20210131.txt', delimiter='\t')
df_name['parsed_type'] = df_name['typeId'].apply(lambda x: str(x)[-3:])
df_name = df_name[df_name['active'] == 1].reset_index(drop=True)

### 001
df_name['sourceId_nm'] = df_name['term']
df_name['destinationId_nm'] = df_name['term']

df_name = df_name[df_name['parsed_type'] == "001"].reset_index(drop=True)
df_name['rank'] = df_name.groupby(['conceptId'])['term'].transform(lambda x: pd.Series.rank(x, ascending=True, method='dense'))
df_name['leng'] = df_name.groupby(['conceptId', 'rank'])['term'].transform(lambda x: len(x))

print(len(df_name))
display(df_name.head())

# %%
print(df_name['rank'].value_counts())
print(len(df_name['conceptId'].unique()))

# %%
df_orig = pd.merge(df_orig, df_name[['conceptId', 'sourceId_nm']].drop_duplicates(), left_on=['sourceId'], right_on=['conceptId'], how='left').drop(columns='conceptId')
print(len(df_orig))
df_orig = pd.merge(df_orig, df_name[['conceptId', 'destinationId_nm']].drop_duplicates(), left_on=['destinationId'], right_on=['conceptId'], how='left').drop(columns='conceptId')
print(len(df_orig))
# %%

column_order = ['id', 'effectiveTime', 'active', 'moduleId', 'source_concept_active', 'sourceId', 'sourceId_nm', 
                'destination_concept_active', 'destinationId', 'destinationId_nm', 'relationshipGroup', 'typeId', 
                'characteristicTypeId', 'modifierId']

df_orig[column_order]



# %%
df_orig[column_order].to_csv('./sct_relationship_codes.csv', index=False)