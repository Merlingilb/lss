import csv


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
        data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        minimum = 0
        for row in data:
            if row[0] == "tlf":
                minimum = float(row[1])
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
            value += minimum/2
        return value
    def getELW1s(self):
        data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        minimum = 0
        for row in data:
            if row[0] == "elw1":
                minimum = float(row[1])
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
        if len(wehren)<int((1.0/minimum)/2.0):
            value += minimum
        return value
    def getDLKs(self):
        data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        minimum = 0
        for row in data:
            if row[0] == "dlk":
                minimum = float(row[1])
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
        if len(wehren)<int((1.0/minimum)/2.0):
            value += minimum
        return value
    def getRWs(self):
        data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        minimum = 0
        for row in data:
            if row[0] == "rw":
                minimum = float(row[1])
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
        if len(wehren)<int((1.0/minimum)/2.0):
            value += minimum
        return value
    def getHLFs(self):
        data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        minimum = 0
        for row in data:
            if row[0] == "hlf":
                minimum = float(row[1])
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
        if len(wehren)<int((1.0/minimum)/2.0):
            value += minimum
        return value
    def getGWOELs(self):
        data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        minimum = 0
        for row in data:
            if row[0] == "gwOel":
                minimum = float(row[1])
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
        if len(wehren)<int((1.0/minimum)/2.0):
            value += minimum
        return value
    def getGWAs(self):
        data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        minimum = 0
        for row in data:
            if row[0] == "gwA":
                minimum = float(row[1])
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
        if len(wehren)<int((1.0/minimum)/2.0):
            value += minimum
        return value
    def getGWSs(self):
        data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        minimum = 0
        for row in data:
            if row[0] == "gwS":
                minimum = float(row[1])
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
        if len(wehren)<int((1.0/minimum)/2.0):
            value += minimum
        return value
    def getHOEHs(self):
        data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        minimum = 0
        for row in data:
            if row[0] == "hoeh":
                minimum = float(row[1])
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
        if len(wehren)<int((1.0/minimum)/2.0):
            value += minimum
        return value
    def getMESSs(self):
        data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        minimum = 0
        for row in data:
            if row[0] == "mess":
                minimum = float(row[1])
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
        if len(wehren)<int((1.0/minimum)/2.0):
            value += minimum
        return value
    def getGWGs(self):
        data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        minimum = 0
        for row in data:
            if row[0] == "gwG":
                minimum = float(row[1])
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
        if len(wehren)<int((1.0/minimum)/2.0):
            value += minimum
        return value
    def getELW2s(self):
        data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        minimum = 0
        for row in data:
            if row[0] == "elw2":
                minimum = float(row[1])
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
        if len(wehren)<int((1.0/minimum)/2.0):
            value += minimum
        return value
    def getDEKONPs(self):
        data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        minimum = 0
        for row in data:
            if row[0] == "dekonP":
                minimum = float(row[1])
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
        if len(wehren)<int((1.0/minimum)/2.0):
            value += minimum
        return value
    def getFWKs(self):
        data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        minimum = 0
        for row in data:
            if row[0] == "fwk":
                minimum = float(row[1])
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
        if len(wehren)<int((1.0/minimum)/2.0):
            value += minimum
        return value

def convert():
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