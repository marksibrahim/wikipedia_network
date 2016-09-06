"""
computes the betweeness centrality on 
the sample directed graph in the paper
"""

import networkx as nx


edge_list = [("A", "B"),
            ("B", "C"),
            ("C", "A"),
            ("D", "C"),
            ("E", "C"),
            ("F", "E"),
            ("G", "E")]


G = nx.DiGraph()
G.add_edges_from(edge_list)

"""
In [1]: nx.betweenness_centrality(G)
Out[1]:
{'A': 0.16666666666666666,
 'B': 0.03333333333333333,
 'C': 0.3,
 'D': 0.0,
 'E': 0.2,
 'F': 0.0,
 'G': 0.0}

In [3]: nx.eigenvector_centrality_numpy(G)
Out[3]:
{'A': 0.577350269189626,
 'B': 0.5773502691896255,
 'C': 0.577350269189626,
 'D': -3.652158313422749e-17,
 'E': 1.7124591974895072e-17,
 'F': -3.807937337545159e-17,
 'G': -8.262461530561738e-18}
 """

