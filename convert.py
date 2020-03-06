import csv
from builtins import map


def getWehr(list, name):
    for wehr in list:
        if wehr.name == name:
            return wehr
    return None

class Feuerwehr():
    def __init__(self, name, pos_x, pos_y, tlf, elw1, dlk, rw, hlf, gwOel, gwA, gwS, hoeh, mess, gwG, elw2, dekonP, fwk):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tlf = int(tlf)
        self.elw1 = int(elw1)
        self.dlk = int(dlk)
        self.rw = int(rw)
        self.hlf = int(hlf)
        self.gwOel = int(gwOel)
        self.gwA = int(gwA)
        self.gwS = int(gwS)
        self.hoeh = int(hoeh)
        self.mess = int(mess)
        self.gwG = int(gwG)
        self.elw2 = int(elw2)
        self.dekonP = int(dekonP)
        self.fwk = int(fwk)
        self.neibors = []
    def addNeibor(self, wehr):
        self.neibors.append(wehr)
        self.neibors = list(dict.fromkeys(self.neibors))
    def getTLFs(self):
        tlfs = self.tlf
        wehren = []
        wehren.append(self)
        for wehr in self.neibors:
            if not (wehr in wehren):
                tlfs += wehr.tlf
                wehren.append(wehr)
            for neibor in wehr.neibors:
                if not (neibor in wehren):
                    tlfs += neibor.tlf
                    wehren.append(neibor)
        value = tlfs/len(wehren)
        if len(wehren)<3:
            value += 0.2
        return value
    def getELW1s(self):
        elw1s = self.elw1
        wehren = []
        wehren.append(self)
        for wehr in self.neibors:
            if not (wehr in wehren):
                elw1s += wehr.elw1
                wehren.append(wehr)
            for neibor in wehr.neibors:
                if not (neibor in wehren):
                    elw1s += neibor.elw1
                    wehren.append(neibor)
        value = elw1s/len(wehren)
        if len(wehren)<2:
            value += 0.5
        return value
    def getDLKs(self):
        dlks = self.dlk
        wehren = []
        wehren.append(self)
        for wehr in self.neibors:
            if not (wehr in wehren):
                dlks += wehr.dlk
                wehren.append(wehr)
            for neibor in wehr.neibors:
                if not (neibor in wehren):
                    dlks += neibor.dlk
                    wehren.append(neibor)
        value = dlks/len(wehren)
        if len(wehren)<2:
            value += 0.25
        return value
    def getRWs(self):
        rws = self.rw
        wehren = []
        wehren.append(self)
        for wehr in self.neibors:
            if not (wehr in wehren):
                rws += wehr.rw
                wehren.append(wehr)
            for neibor in wehr.neibors:
                if not (neibor in wehren):
                    rws += neibor.rw
                    wehren.append(neibor)
        value = rws/len(wehren)
        if len(wehren)<3:
            value += 0.2
        return value
    def getHLFs(self):
        hlfs = self.hlf
        wehren = []
        wehren.append(self)
        for wehr in self.neibors:
            if not (wehr in wehren):
                hlfs += wehr.hlf
                wehren.append(wehr)
            for neibor in wehr.neibors:
                if not (neibor in wehren):
                    hlfs += neibor.hlf
                    wehren.append(neibor)
        value = hlfs/len(wehren)
        if len(wehren)<3:
            value += 0.2
        return value
    def getGWOELs(self):
        gwOels = self.gwOel
        wehren = []
        wehren.append(self)
        for wehr in self.neibors:
            if not (wehr in wehren):
                gwOels += wehr.gwOel
                wehren.append(wehr)
            for neibor in wehr.neibors:
                if not (neibor in wehren):
                    gwOels += neibor.gwOel
                    wehren.append(neibor)
        value = gwOels/len(wehren)
        if len(wehren)<4:
            value += (1.0/7.0)
        return value
    def getGWAs(self):
        gwAs = self.gwA
        wehren = []
        wehren.append(self)
        for wehr in self.neibors:
            if not (wehr in wehren):
                gwAs += wehr.gwA
                wehren.append(wehr)
            for neibor in wehr.neibors:
                if not (neibor in wehren):
                    gwAs += neibor.gwA
                    wehren.append(neibor)
        value = gwAs/len(wehren)
        if len(wehren)<4:
            value += (1.0/8.0)
        return value
    def getGWSs(self):
        gwSs = self.gwS
        wehren = []
        wehren.append(self)
        for wehr in self.neibors:
            if not (wehr in wehren):
                gwSs += wehr.gwS
                wehren.append(wehr)
            for neibor in wehr.neibors:
                if not (neibor in wehren):
                    gwSs += neibor.gwS
                    wehren.append(neibor)
        value = gwSs/len(wehren)
        if len(wehren)<4:
            value += (1.0/8.0)
        return value
    def getHOEHs(self):
        hoehs = self.hoeh
        wehren = []
        wehren.append(self)
        for wehr in self.neibors:
            if not (wehr in wehren):
                hoehs += wehr.hoeh
                wehren.append(wehr)
            for neibor in wehr.neibors:
                if not (neibor in wehren):
                    hoehs += neibor.hoeh
                    wehren.append(neibor)
        value = hoehs/len(wehren)
        if len(wehren)<6:
            value += (1.0/11.0)
        return value
    def getMESSs(self):
        messs = self.mess
        wehren = []
        wehren.append(self)
        for wehr in self.neibors:
            if not (wehr in wehren):
                messs += wehr.mess
                wehren.append(wehr)
            for neibor in wehr.neibors:
                if not (neibor in wehren):
                    messs += neibor.mess
                    wehren.append(neibor)
        value = messs/len(wehren)
        if len(wehren)<6:
            value += (1.0/12.0)
        return value
    def getGWGs(self):
        gwGs = self.gwG
        wehren = []
        wehren.append(self)
        for wehr in self.neibors:
            if not (wehr in wehren):
                gwGs += wehr.gwG
                wehren.append(wehr)
            for neibor in wehr.neibors:
                if not (neibor in wehren):
                    gwGs += neibor.gwG
                    wehren.append(neibor)
        value = gwGs/len(wehren)
        if len(wehren)<7:
            value += (1.0/13.0)
        return value
    def getELW2s(self):
        elw2s = self.elw2
        wehren = []
        wehren.append(self)
        for wehr in self.neibors:
            if not (wehr in wehren):
                elw2s += wehr.elw2
                wehren.append(wehr)
            for neibor in wehr.neibors:
                if not (neibor in wehren):
                    elw2s += neibor.elw2
                    wehren.append(neibor)
        value = elw2s/len(wehren)
        if len(wehren)<7:
            value += (1.0/14.0)
        return value
    def getDEKONPs(self):
        dekonPs = self.dekonP
        wehren = []
        wehren.append(self)
        for wehr in self.neibors:
            if not (wehr in wehren):
                dekonPs += wehr.dekonP
                wehren.append(wehr)
            for neibor in wehr.neibors:
                if not (neibor in wehren):
                    dekonPs += neibor.dekonP
                    wehren.append(neibor)
        value = dekonPs/len(wehren)
        if len(wehren)<8:
            value += (1.0/15.0)
        return value
    def getFWKs(self):
        fwks = self.fwk
        wehren = []
        wehren.append(self)
        for wehr in self.neibors:
            if not (wehr in wehren):
                fwks += wehr.fwk
                wehren.append(wehr)
            for neibor in wehr.neibors:
                if not (neibor in wehren):
                    fwks += neibor.fwk
                    wehren.append(neibor)
        value = fwks/len(wehren)
        if len(wehren)<8:
            value += (1.0/15.0)
        return value

wehren = []
data = csv.reader(open('wehren.csv', "r", encoding='ansi'))
next(data)
for row in data:
    wehr = Feuerwehr(row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip(), row[4].strip(), row[5].strip(), row[6].strip(), row[7].strip(), row[8].strip(), row[9].strip(), row[10].strip(), row[11].strip(), row[12].strip(), row[13].strip(), row[14].strip(), row[15].strip(), row[16].strip())
    wehren.append(wehr)

data = csv.reader(open('verbindungen.csv', "r", encoding='ansi'))
for row in data:
    getWehr(wehren,row[0].strip()).addNeibor(getWehr(wehren,row[1].strip()))
    getWehr(wehren,row[1].strip()).addNeibor(getWehr(wehren,row[0].strip()))

data = "!!python/object:networkx.classes.graph.Graph\n"
data += "_adj:\n"
for wehr in wehren:
    data += "  " + wehr.name + ":\n"
    for neibor in wehr.neibors:
        data += "    " + neibor.name + ": {}\n"
data += "_node: &id001\n"
for wehr in wehren:
    data += "  " + wehr.name + ": {pos_x: " + wehr.pos_x + ", pos_y: " + wehr.pos_y + ", tlf: " + str(wehr.getTLFs()) + ", elw1: " + str(wehr.getELW1s()) + ", dlk: " + str(wehr.getDLKs()) + ", rw: " + str(wehr.getRWs()) + ", hlf: " + str(wehr.getHLFs()) + ", gwOel: " + str(wehr.getGWOELs()) + ", gwA: " + str(wehr.getGWAs()) + ", gwS: " + str(wehr.getGWSs()) + ", hoeh: " + str(wehr.getHOEHs()) + ", mess: " + str(wehr.getMESSs()) + ", gwG: " + str(wehr.getGWGs()) + ", elw2: " + str(wehr.getELW2s()) + ", dekonP: " + str(wehr.getDEKONPs()) + ", fwk: " + str(wehr.getFWKs()) + "}\n"
data += "adjlist_inner_dict_factory: &id002 !!python/name:builtins.dict ''\n"
data += "adjlist_outer_dict_factory: *id002\n"
data += "edge_attr_dict_factory: *id002\n"
data += "graph:\n"
data += "  name: FFs\n"
data += "graph_attr_dict_factory: *id002\n"
data += "node_attr_dict_factory: *id002\n"
data += "node_dict_factory: *id002\n"
data += "nodes: !!python/object:networkx.classes.reportviews.NodeView\n"
data += "  _nodes: *id001\n"

f = open("test.yml", "w")
f.write(data)
f.close()