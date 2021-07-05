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
class hierarchical_graph():
    
    def __init__(self, data, parent, source):
        self.data = data            ## DataFrame
        self.parent = source        ## Children(Lower)
        self.source = parent        ## Parents(Higher)
        
        super().__init__()
        
        self.graph = nx.from_pandas_edgelist(df_orig, 
                                             target=self.parent, 
                                             source=self.source, 
                                             create_using=nx.DiGraph())
    
    def get_descendent(self, node, level):
        decendents = nx.descendants_at_distance(G=self.graph, 
                                                source=node, 
                                                distance=level)
        
        ## displaying
        display(self.data[self.data['sourceId'].isin(decendents)])
        
    def get_descendent_all(self, node):
        decendents = nx.descendants(G=self.graph, 
                                    source=node)
        ## displaying
        display(self.data[self.data['sourceId'].isin(decendents)])

# %%

if __name__ == '__main__':
    df_orig = fread('./sct_relationship_codes.csv', na_strings=['NA','']).to_pandas()
    
    test = hierarchical_graph(data=df_orig, parent='destinationId', source='sourceId')
    test.get_descendent(node=138875005, level=1)
    
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
max(nx.single_source_shortest_path_length(DiG, 138875005).values())
# %%
