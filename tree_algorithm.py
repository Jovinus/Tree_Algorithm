# %% Import packages to use
from datatable import fread
import pandas as pd
from IPython.display import display
import networkx as nx

# %% Hierarchical Graph Class
class hierarchical_graph():
    
    def __init__(self, data, parent, source):
        self.data = data            ## DataFrame
        self.parent = source        ## Children(Lower)
        self.source = parent        ## Parents(Higher)
        
        super().__init__()
        
        ## Generate Relationship Graph
        ## Decendants
        self.graph = nx.from_pandas_edgelist(df_orig, 
                                             target=self.parent, 
                                             source=self.source, 
                                             create_using=nx.DiGraph())
        
        ## Print maximum level between higher node and lowest node
        print(max(nx.single_source_shortest_path_length(self.graph, 138875005).values()))
        
    def get_descendent(self, node, level, save=False):
        decendents = nx.descendants_at_distance(G=self.graph, 
                                                source=node, 
                                                distance=level)
        
        ## displaying
        results = self.data[self.data['sourceId'].isin(decendents)].copy()
        results['level'] = level
        
        display(results)

        if save == True:
            results.to_csv("./"+ str(node) + "_decendent.csv", index=False, encoding='utf-8')
        
    def get_descendent_all(self, node, max_level, save=False):
        
        ## Get max depth of given node 
        max_depth = max(nx.single_source_shortest_path_length(self.graph, node).values())
        
        results = pd.DataFrame([])
        
        ## Get level 1 to given level
        for level in range(1, min(max_level + 1, max_depth + 1)):
            decendents = nx.descendants_at_distance(G=self.graph, 
                                                    source=node, 
                                                    distance=level)
            
            tmp_df = self.data[self.data['sourceId'].isin(decendents)].copy()
            tmp_df['level'] = level
            results = pd.concat((results, tmp_df), axis=0)
        
        ## displaying
        display(results)
        
        if save == True:
            results.to_csv("./"+ str(node) + "_decendent_all.csv", index=False, encoding='utf-8')

# %%

if __name__ == '__main__':
    df_orig = fread('./sct_relationship_codes.csv', na_strings=['NA','']).to_pandas()
    
    test = hierarchical_graph(data=df_orig, parent='destinationId', source='sourceId')
    test.get_descendent(node=138875005, level=1, save=False)
    test.get_descendent_all(node=138875005, max_level=14, save=False)
    
# %%
