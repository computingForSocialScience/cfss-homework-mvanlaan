import pandas as pd
import networkx as nx 
import numpy as np

def readEdgeList(filename):
    df = pd.read_csv(filename)
    if len(df.columns) > 2:
        print('WARNING file has more than 2 columns')
        df = df[df.columns[0:2]]
    return df

def degree(edgeList, in_or_out):
    if in_or_out == "in":
        count = edgeList['artist2'].value_counts()
        return count

    if in_or_out == "out":
        count = edgeList['artist1'].value_counts()
        return count

def combineEdgeLists(edgeList1, edgeList2):
    combinedlist = edgeList1.append(edgeList2)
    combinedlist.drop_duplicates(inplace=True)
    return combinedlist

def pandasToNetworkX(edgeList):
    edge_data = edgeList.to_records(index=False)
    g = nx.DiGraph()
    for artist1, artist2 in edge_data:
        g.add_edge(artist1, artist2)
    return g

def randomCentralNode(inputDiGraph):
    dict = nx.eigenvector_centrality(inputDiGraph)
    dict_sum = float(sum(dct.values()))
    nc_dict = dict((k, v / dct_sum) for k, v in dct.items())
    randomnode = np.random.choice(nc_dct.keys(), p=nc_dct.values())
    return randomnode