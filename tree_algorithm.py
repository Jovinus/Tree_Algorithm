# %%
from datatable import fread
from IPython.display import display
# %%
df_orig = fread('./sct_relationship_codes.csv', na_strings=['NA','']).to_pandas()
df_orig.head()
# %%
