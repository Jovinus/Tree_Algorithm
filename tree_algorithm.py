# %%
from datatable import fread
from IPython.display import display
import networkx as nx

# %%
df_orig = fread('./sct_relationship_codes.csv', na_strings=['NA','']).to_pandas()
display(df_orig.head())

# %%

DiG = nx.from_pandas_edgelist(df_orig, target='sourceId', source='destinationId', create_using=nx.DiGraph())

# %%

if __name__ == '__main__':
    df_orig = fread('./sct_relationship_codes.csv', na_strings=['NA','']).to_pandas()
    display(df_orig.head())
    
# %%
nx.descendants_at_distance(G=DiG, source=138875005, distance=1)
# %%
