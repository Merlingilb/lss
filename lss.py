import matplotlib.pyplot as plt
import csv
import networkx as nx

import convert

G = nx.read_yaml("test.yml")
pos = {}
color = []
for key in G._node:
       pos[key]=(G._node[key]["pos_y"],G._node[key]["pos_x"])
#       if G._node[key]["tlf"]<2.2: color.append('red')
#       if G._node[key]["elw1"]<0.5: color.append('red')
       if G._node[key]["dlk"]<0.25: color.append('red')
#       if G._node[key]["rw"]<0.2: color.append('red')
#       if G._node[key]["hlf"]<0.2: color.append('red')
#       if G._node[key]["gwOel"]<(1.0/7.0): color.append('red')
#       if G._node[key]["gwA"]<(1.0/8.0): color.append('red')
#       if G._node[key]["gwS"]<(1.0/8.0): color.append('red')
#       if G._node[key]["hoeh"]<(1.0/11.0): color.append('red')
#       if G._node[key]["mess"]<(1.0/12.0): color.append('red')
#       if G._node[key]["gwG"]<(1.0/13.0): color.append('red')
#       if G._node[key]["elw2"]<(1.0/14.0): color.append('red')
#       if G._node[key]["dekonP"]<(1.0/15.0): color.append('red')
#       if G._node[key]["fwk"]<(1.0/15.0): color.append('red')
       else: color.append('green')

nx.draw(G,pos,with_labels=True,node_color=color)
plt.axis('off')
plt.show()