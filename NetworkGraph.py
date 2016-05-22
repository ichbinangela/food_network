# Scrape the data and extract the materials from the recepie
from bs4 import BeautifulSoup
import requests
import itertools
result = []
for j in range(20):
    url = "https://icook.tw/categories/68?page={}".format(j)
    rescook = requests.get(url)
    soup = BeautifulSoup(rescook.text, "lxml")
    
    for i in range(12):
        text = soup.select('.material')[i].text[3:]
        text = text.split('、')
    
        result.extend(list(itertools.combinations(text, 2)))
print('Number of total pairs:', len(result))
print('Some examples:', result[:5])

# Draw the network graph
import matplotlib.pyplot as plt
import networkx as nx
%matplotlib inline

default_weight = 0.1
G = nx.Graph()

BLUE = "#99CCFF"

for nodes in result:
    n0 = nodes[0]
    n1 = nodes[1]
    if G.has_edge(n0,n1):   
        G[n0][n1]['weight'] += default_weight
    else:
        G.add_edge(n0,n1, weight = default_weight)
        
nx.draw(G, node_color = BLUE, with_labels = False, node_size = 4)
