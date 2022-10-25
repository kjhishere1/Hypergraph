from hypergraph import Hypergraph as HG

func = lambda x: 1/x*200
hg = HG(512, 512, func, 3)
hg.Graph()