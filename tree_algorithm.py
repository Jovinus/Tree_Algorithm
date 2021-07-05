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
        self.graph_descend = nx.from_pandas_edgelist(df_orig, 
                                                     target=self.parent, 
                                                     source=self.source, 
                                                     create_using=nx.DiGraph())
        
        self.graph_ascend = nx.from_pandas_edgelist(df_orig, 
                                                     target=self.source, 
                                                     source=self.parent, 
                                                     create_using=nx.DiGraph())
        
        ## Print maximum level between higher node and lowest node
        print(max(nx.single_source_shortest_path_length(self.graph_descend, 138875005).values()))
        
    def get_descendent(self, node, level, save=False):
        decendents = nx.descendants_at_distance(G=self.graph_descend, 
                                                source=node, 
                                                distance=level)
        
        ## displaying
        results = self.data[self.data['sourceId'].isin(decendents)].copy()
        results['level'] = level
        
        display(results)

        if save == True:
            results.to_csv("./"+ str(node) + "_decendent.csv", index=False, encoding='utf-8')

    def get_descendent_all(self, node, max_level=0, save=False):
        
        ## Get max depth of given node 
        max_depth = max(nx.single_source_shortest_path_length(self.graph_descend, node).values())
        
        ## Select max_depth when max level isn't specified
        if max_level == 0:
            max_level = max_depth
        
        results = pd.DataFrame([], columns=df_orig.columns)
        
        ## Get level 1 to given level
        for level in range(1, max_level + 1):
            decendents = nx.descendants_at_distance(G=self.graph_descend, 
                                                    source=node, 
                                                    distance=level)
            
            tmp_df = self.data[self.data['sourceId'].isin(decendents)].copy()
            tmp_df['level'] = level
            results = pd.concat((results, tmp_df), axis=0)
        
        ## displaying
        display(results)
        
        if save == True:
            results.to_csv("./"+ str(node) + "_decendent_all.csv", index=False, encoding='utf-8')
    
    ## Get ascendent from given level
    def get_ascendent(self, node, level, save=False):
        decendents = nx.descendants_at_distance(G=self.graph_ascend, 
                                                source=node, 
                                                distance=level)
        
        ## displaying
        results = self.data[self.data['sourceId'].isin(decendents)].copy()
        results['level'] = level
        
        display(results)

        if save == True:
            results.to_csv("./"+ str(node) + "_ascendent.csv", index=False, encoding='utf-8')
    
    ## Get all ascendent from 1 to given levels
    def get_ascendent_all(self, node, max_level=0, save=False):
        
        ## Get max depth of given node 
        max_depth = max(nx.single_source_shortest_path_length(self.graph_ascend, node).values())
        
        ## Select max_depth when max level isn't specified
        if max_level == 0:
            max_level = max_depth
        
        results = pd.DataFrame([], columns=df_orig.columns)
        
        ## Get level 1 to given level
        for level in range(1, max_level + 1):
            decendents = nx.descendants_at_distance(G=self.graph_descend, 
                                                    source=node, 
                                                    distance=level)
            
            tmp_df = self.data[self.data['sourceId'].isin(decendents)].copy()
            tmp_df['level'] = level
            results = pd.concat((results, tmp_df), axis=0)
        
        ## displaying
        display(results)
        
        if save == True:
            results.to_csv("./"+ str(node) + "_ascendent_all.csv", index=False, encoding='utf-8')

# %%

if __name__ == '__main__':
    df_orig = fread('./sct_relationship_codes.csv', na_strings=['NA','']).to_pandas()
    
    test = hierarchical_graph(data=df_orig, parent='destinationId', source='sourceId')
    test.get_descendent(node=138875005, level=1, save=False)
    test.get_descendent_all(node=138875005, max_level=0, save=False)
    test.get_ascendent(node=138875005, level=1, save=False)
    test.get_ascendent_all(node=138875005, max_level=0, save=False)
    
# %%

# %%
