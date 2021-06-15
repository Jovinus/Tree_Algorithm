# %%
from datatable import fread
from IPython.display import display

# %%








# %%

if __name__ == '__main__':
    df_orig = fread('./sct_relationship_codes.csv', na_strings=['NA','']).to_pandas()
    display(df_orig.head())