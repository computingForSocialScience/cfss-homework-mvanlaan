import sys
import requests
import pandas as pd
import networkx as nx
from io import open
import csv
import numpy as np
def readEdgeList(file_name):
	edgelist_df = pd.read_csv(file_name)
	if len(edgelist_df.columns) != 2:
		print "Not 2 columns"
	new_edgelist_df = edgelist_df[edgelist_df.columns[:2]]
	return new_edgelist_df
def degree(edgeList, inorout):
	if inorout is 'in':
		return edgeList['artist2'].value_counts(sort=True)
	if inorout is 'out':
		return edgeList['artist1'].value_counts(sort=True)
	else:
		print "put in or out"
def combineEdgeLists(edgeList1,edgeList2):
	concatenated = pd.concat([edgeList1,edgeList2])
	return concatenated.drop_duplicates()
def pdToNX(edgeList):
	ndg = nx.DiGraph()
	for sender,receiver in edgeList.to_records(index=False):
		ndg.add_edge(sender,receiver)
	return ndg
def randomCentralNode(inputdigraph):
	freqdict = nx.eigenvector_centrality(inputdigraph)
	total = 0
	for i in freqdict:
		total += freqdict[i]
	new_freq_dict = {}
	for i in freqdict:
		new_freq_dict[i] = freqdict[i]/total
	'''new_total = 0
	for i in new_freq_dict:
		new_total += new_freq_dict[i]
	print new_total'''
	rcn = np.random.choice(new_freq_dict.keys(), p=new_freq_dict.values())
	return  rcn