import time
import matplotlib.pyplot as plt
import networkx as nx
import networkx.classes.graph
import networkx.classes
import networkx
import tkinter as tk
import convert
import csv
import requests
from lxml import etree
from io import StringIO

def writeVerbindungen(liste):
       data=""
       for wehr in liste:
              for neibor in wehr.neibors:
                     data+=wehr.name+","+neibor.name+"\n"
       f = open("verbindungen.csv", "w")
       f.write(data)
       f.close()

def show(type):
       global G, wehren, color
       wehren = convert.convert()

       try:
              data = csv.reader(open('settings.csv', "r", encoding='ansi'))
       except:
              data = csv.reader(open('../../settings.csv', "r", encoding='ansi'))
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

       click1 = []
       nx.draw(G,pos,with_labels=True,node_color=color)

       def onclick(event):
              global G, wehren, color
              if event.dblclick:
                     print(event.xdata, event.ydata)
                     varianceX = event.inaxes.axes.viewLim.height / event.canvas.figure.bbox.height * 12.5
                     varianceY = event.inaxes.axes.viewLim.width / event.canvas.figure.bbox.width * 12.5
                     length = len(click1)
                     for key in G._node:
                            if G._node[key]["pos_y"]+varianceY>event.xdata and G._node[key]["pos_y"]-varianceY<event.xdata and G._node[key]["pos_x"]+varianceX>event.ydata and G._node[key]["pos_x"]-varianceX<event.ydata:
                                   if key in click1:
                                          click1.remove(key)
                                   else:
                                          click1.append(key)
                     if length + 1 < len(click1):
                            click1.clear()
                     print(click1)
                     if len(click1) > 1:
                            if G.has_edge(click1[0],click1[1]):
                                   convert.getWehr(wehren,click1[0]).deleteNeibor(convert.getWehr(wehren,click1[1]))
                                   convert.getWehr(wehren,click1[1]).deleteNeibor(convert.getWehr(wehren,click1[0]))
                                   G.remove_edge(click1.pop(),click1.pop())
                            else:
                                   convert.getWehr(wehren,click1[0]).addNeibor(convert.getWehr(wehren,click1[1]))
                                   convert.getWehr(wehren,click1[1]).addNeibor(convert.getWehr(wehren,click1[0]))
                                   G.add_edge(click1.pop(),click1.pop())
                            fig.set_facecolor((1.0, 0, 0))
                            fig.canvas.draw()
                            fig.canvas.flush_events()
                            writeVerbindungen(wehren)
                            wehren = convert.convert()
                            G = nx.read_yaml("test.yml")
                     color = []
                     for key in G._node:
                            if key in click1:color.append('orange')
                            elif G._node[key]["tlf"] < minimum and type == "tlf":color.append('red')
                            elif G._node[key]["elw1"] < minimum and type == "elw1":color.append('red')
                            elif G._node[key]["dlk"] < minimum and type == "dlk":color.append('red')
                            elif G._node[key]["rw"] < minimum and type == "rw":color.append('red')
                            elif G._node[key]["hlf"] < minimum and type == "hlf":color.append('red')
                            elif G._node[key]["gwOel"] < minimum and type == "gwOel":color.append('red')
                            elif G._node[key]["gwA"] < minimum and type == "gwA":color.append('red')
                            elif G._node[key]["gwS"] < minimum and type == "gwS":color.append('red')
                            elif G._node[key]["hoeh"] < minimum and type == "hoeh":color.append('red')
                            elif G._node[key]["mess"] < minimum and type == "mess":color.append('red')
                            elif G._node[key]["gwG"] < minimum and type == "gwG":color.append('red')
                            elif G._node[key]["elw2"] < minimum and type == "elw2":color.append('red')
                            elif G._node[key]["dekonP"] < minimum and type == "dekonP":color.append('red')
                            elif G._node[key]["fwk"] < minimum and type == "fwk":color.append('red')
                            else:color.append('green')
                     fig.clf()
                     nx.draw(G, pos, with_labels=True, node_color=color)
                     plt.show()

       def onkey(event):
              global G, wehren, color, fig
              if event.key=='r':
                     fig.set_facecolor((1.0, 0, 0))
                     fig.canvas.draw()
                     fig.canvas.flush_events()
                     wehren = convert.convert()
                     G = nx.read_yaml("test.yml")
                     color = []
                     for key in G._node:
                            if G._node[key]["tlf"] < minimum and type == "tlf":color.append('red')
                            elif G._node[key]["elw1"] < minimum and type == "elw1":color.append('red')
                            elif G._node[key]["dlk"] < minimum and type == "dlk":color.append('red')
                            elif G._node[key]["rw"] < minimum and type == "rw":color.append('red')
                            elif G._node[key]["hlf"] < minimum and type == "hlf":color.append('red')
                            elif G._node[key]["gwOel"] < minimum and type == "gwOel":color.append('red')
                            elif G._node[key]["gwA"] < minimum and type == "gwA":color.append('red')
                            elif G._node[key]["gwS"] < minimum and type == "gwS":color.append('red')
                            elif G._node[key]["hoeh"] < minimum and type == "hoeh":color.append('red')
                            elif G._node[key]["mess"] < minimum and type == "mess":color.append('red')
                            elif G._node[key]["gwG"] < minimum and type == "gwG":color.append('red')
                            elif G._node[key]["elw2"] < minimum and type == "elw2":color.append('red')
                            elif G._node[key]["dekonP"] < minimum and type == "dekonP":color.append('red')
                            elif G._node[key]["fwk"] < minimum and type == "fwk":color.append('red')
                            else:color.append('green')
                     fig.clf()
                     nx.draw(G, pos, with_labels=True, node_color=color)
                     plt.show()

       global fig
       fig = plt.figure(1)
       fig.canvas.mpl_connect('button_press_event', onclick)
       fig.canvas.mpl_connect('key_press_event', onkey)
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
button_lf = tk.Button(frame, text="LF", command=lf, width=30)
button_lf.grid(row=0, column=0)
button_elw1 = tk.Button(frame, text="ELW1", command=elw1, width=30)
button_elw1.grid(row=0, column=1)
button_dlk = tk.Button(frame, text="DLK", command=dlk, width=30)
button_dlk.grid(row=1, column=0)
button_rw = tk.Button(frame, text="RW", command=rw, width=30)
button_rw.grid(row=1, column=1)
button_hlf = tk.Button(frame, text="HLF", command=hlf, width=30)
button_hlf.grid(row=2, column=0)
button_gwOel = tk.Button(frame, text="GW-Öl", command=gwOel, width=30)
button_gwOel.grid(row=2, column=1)
button_gwA = tk.Button(frame, text="GW-A", command=gwA, width=30)
button_gwA.grid(row=3, column=0)
button_gwS = tk.Button(frame, text="GW-S", command=gwS, width=30)
button_gwS.grid(row=3, column=1)
button_hoeh = tk.Button(frame, text="GW-Höh", command=hoeh, width=30)
button_hoeh.grid(row=4, column=0)
button_mess = tk.Button(frame, text="GW-Mess", command=mess, width=30)
button_mess.grid(row=4, column=1)
button_gwG = tk.Button(frame, text="GW-G", command=gwG, width=30)
button_gwG.grid(row=5, column=0)
button_elw2 = tk.Button(frame, text="ELW2", command=elw2, width=30)
button_elw2.grid(row=5, column=1)
button_dekonP = tk.Button(frame, text="GW-Dekon-P", command=dekonP, width=30)
button_dekonP.grid(row=6, column=0)
button_fwk = tk.Button(frame, text="FWK", command=fwk, width=30)
button_fwk.grid(row=6, column=1)

root.mainloop()


