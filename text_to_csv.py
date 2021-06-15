# %% Import Module
import pandas as pd
from IPython.display import display
# %%
df_orig = pd.read_csv('./sct2_Relationship_Snapshot_INT_20210131.txt', delimiter='\t')
df_orig.head()
# %%
df_orig.to_csv('./sct_relationship_codes.csv', index=False)
