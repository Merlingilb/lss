import matplotlib.pyplot as plt
import networkx as nx
import tkinter as tk
import convert
import csv

def show(type):
       convert.convert()

       data = csv.reader(open('settings.csv', "r", encoding='ansi'))
       minimum=0
       for row in data:
              if row[0] == type:
                     minimum = float(row[1])

       G = nx.read_yaml("test.yml")
       pos = {}
       color = []
       for key in G._node:
              pos[key]=(G._node[key]["pos_y"],G._node[key]["pos_x"])
              if G._node[key]["tlf"]<minimum and type=="tlf": color.append('red')
              elif G._node[key]["elw1"]<minimum and type=="elw1": color.append('red')
              elif G._node[key]["dlk"]<minimum and type=="dlk": color.append('red')
              elif G._node[key]["rw"]<minimum and type=="rw": color.append('red')
              elif G._node[key]["hlf"]<minimum and type=="hlf": color.append('red')
              elif G._node[key]["gwOel"]<minimum and type=="gwOel": color.append('red')
              elif G._node[key]["gwA"]<minimum and type=="gwA": color.append('red')
              elif G._node[key]["gwS"]<minimum and type=="gwS": color.append('red')
              elif G._node[key]["hoeh"]<minimum and type=="hoeh": color.append('red')
              elif G._node[key]["mess"]<minimum and type=="mess": color.append('red')
              elif G._node[key]["gwG"]<minimum and type=="gwG": color.append('red')
              elif G._node[key]["elw2"]<minimum and type=="elw2": color.append('red')
              elif G._node[key]["dekonP"]<minimum and type=="dekonP": color.append('red')
              elif G._node[key]["fwk"]<minimum and type=="fwk": color.append('red')
              else: color.append('green')

       nx.draw(G,pos,with_labels=True,node_color=color)
       plt.axis('off')
       plt.show()

def lf():
       show("tlf")
def elw1():
       show("elw1")
def dlk():
       show("dlk")
def rw():
       show("rw")
def hlf():
       show("hlf")
def gwOel():
       show("gwOel")
def gwA():
       show("gwA")
def gwS():
       show("gwS")
def hoeh():
       show("hoeh")
def mess():
       show("mess")
def gwG():
       show("gwG")
def elw2():
       show("elw2")
def dekonP():
       show("dekonP")
def fwk():
       show("fwk")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button_quit = tk.Button(frame, text="QUIT", fg="red", command=quit)
button_quit.pack(side=tk.LEFT)
button_lf = tk.Button(frame, text="LF", command=lf)
button_lf.pack(side=tk.LEFT)
button_elw1 = tk.Button(frame, text="ELW1", command=elw1)
button_elw1.pack(side=tk.LEFT)
button_dlk = tk.Button(frame, text="DLK", command=dlk)
button_dlk.pack(side=tk.LEFT)
button_rw = tk.Button(frame, text="RW", command=rw)
button_rw.pack(side=tk.LEFT)
button_hlf = tk.Button(frame, text="HLF", command=hlf)
button_hlf.pack(side=tk.LEFT)
button_gwOel = tk.Button(frame, text="GW-Öl", command=gwOel)
button_gwOel.pack(side=tk.LEFT)
button_gwA = tk.Button(frame, text="GW-A", command=gwA)
button_gwA.pack(side=tk.LEFT)
button_gwS = tk.Button(frame, text="GW-S", command=gwS)
button_gwS.pack(side=tk.LEFT)
button_hoeh = tk.Button(frame, text="GW-Höh", command=hoeh)
button_hoeh.pack(side=tk.LEFT)
button_mess = tk.Button(frame, text="GW-Mess", command=mess)
button_mess.pack(side=tk.LEFT)
button_gwG = tk.Button(frame, text="GW-G", command=gwG)
button_gwG.pack(side=tk.LEFT)
button_elw2 = tk.Button(frame, text="ELW2", command=elw2)
button_elw2.pack(side=tk.LEFT)
button_dekonP = tk.Button(frame, text="GW-Dekon-P", command=dekonP)
button_dekonP.pack(side=tk.LEFT)
button_fwk = tk.Button(frame, text="FWK", command=fwk)
button_fwk.pack(side=tk.LEFT)

root.mainloop()


