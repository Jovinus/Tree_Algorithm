# %% Import packages to use
from datatable import fread
from IPython.display import display
import networkx as nx

# %% Hierarchical Graph Class
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
        
        ## Print maximum level between higher node and lowest node
        print(max(nx.single_source_shortest_path_length(self.graph, 138875005).values()))
        
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
    test.get_descendent_all(node=138875005)
