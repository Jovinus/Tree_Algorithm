# %%
from datatable import fread
from IPython.display import display
import networkx as nx

# %%
df_orig = fread('./sct_relationship_codes.csv', na_strings=['NA','']).to_pandas()
display(df_orig.head())

# %%

DiG = nx.from_pandas_edgelist(df_orig, target='sourceId', source='destinationId', create_using=nx.DiGraph())


#%%
class hierarchical_graph(self, data, parent, source):
    
    def __init__(self):
        self.data = data
    
    def get_descendent(node):
        data

# %%

if __name__ == '__main__':
    df_orig = fread('./sct_relationship_codes.csv', na_strings=['NA','']).to_pandas()
    display(df_orig.head())
    
# %%
print(nx.descendants_at_distance(G=DiG, source=138875005, distance=1))
# %%
test = nx.single_source_shortest_path_length(DiG, 138875005)
max(test.values())
# %%
df_orig[(df_orig['sourceId'].isin(nx.descendants_at_distance(G=DiG, source=138875005, distance=1))) & (df_orig['active'] == True)]
# %%

df_orig[(df_orig['sourceId'].isin(nx.descendants(G=DiG, source=267038008))) & (df_orig['active'] == True)]
# %%
