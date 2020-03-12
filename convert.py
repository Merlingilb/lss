import csv
import json
from io import StringIO

import requests
from lxml import etree


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
        self.id = None
        self.neibors = []
    def __init__(self, name, pos_x, pos_y, id):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tlf = 0
        self.elw1 = 0
        self.dlk = 0
        self.rw = 0
        self.hlf = 0
        self.gwOel = 0
        self.gwA = 0
        self.gwS = 0
        self.hoeh = 0
        self.mess = 0
        self.gwG = 0
        self.elw2 = 0
        self.dekonP = 0
        self.fwk = 0
        self.id = id
        self.neibors = []
    def addFahrzeug(self, type):
        if type=="tlf": self.tlf += 1
        if type=="elw1": self.elw1 += 1
        if type=="dlk": self.dlk += 1
        if type=="rw": self.rw += 1
        if type=="hlf": self.hlf += 1
        if type=="gwOel": self.gwOel += 1
        if type=="gwA": self.gwA += 1
        if type=="gwS": self.gwS += 1
        if type=="hoeh": self.hoeh += 1
        if type=="mess": self.mess += 1
        if type=="gwG": self.gwG += 1
        if type=="elw2": self.elw2 += 1
        if type=="dekonP": self.dekonP += 1
        if type=="fwk": self.fwk += 1
    def addNeibor(self, wehr):
        self.neibors.append(wehr)
        self.neibors = list(dict.fromkeys(self.neibors))
    def deleteNeibor(self, wehr):
        self.neibors.remove(wehr)
    def getTLFs(self):
        try:
            data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        except:
            data = csv.reader(open('../../settings.csv', "r", encoding='ansi'))
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
        try:
            data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        except:
            data = csv.reader(open('../../settings.csv', "r", encoding='ansi'))
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
        try:
            data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        except:
            data = csv.reader(open('../../settings.csv', "r", encoding='ansi'))
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
        try:
            data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        except:
            data = csv.reader(open('../../settings.csv', "r", encoding='ansi'))
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
        try:
            data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        except:
            data = csv.reader(open('../../settings.csv', "r", encoding='ansi'))
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
        try:
            data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        except:
            data = csv.reader(open('../../settings.csv', "r", encoding='ansi'))
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
        try:
            data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        except:
            data = csv.reader(open('../../settings.csv', "r", encoding='ansi'))
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
        try:
            data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        except:
            data = csv.reader(open('../../settings.csv', "r", encoding='ansi'))
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
        try:
            data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        except:
            data = csv.reader(open('../../settings.csv', "r", encoding='ansi'))
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
        try:
            data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        except:
            data = csv.reader(open('../../settings.csv', "r", encoding='ansi'))
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
        try:
            data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        except:
            data = csv.reader(open('../../settings.csv', "r", encoding='ansi'))
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
        try:
            data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        except:
            data = csv.reader(open('../../settings.csv', "r", encoding='ansi'))
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
        try:
            data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        except:
            data = csv.reader(open('../../settings.csv', "r", encoding='ansi'))
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
        try:
            data = csv.reader(open('settings.csv', "r", encoding='ansi'))
        except:
            data = csv.reader(open('../../settings.csv', "r", encoding='ansi'))
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
    username = ""
    password = ""
    http_proxy = ""
    https_proxy = ""
    proxy = False
    excludeWehren = []
    try:
        data = csv.reader(open('config.csv', "r", encoding='ansi'))
    except:
        data = csv.reader(open('../../config.csv', "r", encoding='ansi'))
    for row in data:
        if row[0].strip()=="username":
            username = row[1].strip()
            if username=="<<<email|username>>>":
                raise Exception("config.csv has still default values... Change them before starting the program.")
        if row[0].strip()=="password":
            password = row[1].strip()
            if password=="<<<password>>>":
                raise Exception("config.csv has still default values... Change them before starting the program.")
        if row[0].strip()=="proxy" and row[1].strip()=="yes":
            proxy = True
        if row[0].strip()=="proxy" and row[1].strip()=="<<<yes|no>>>":
            raise Exception("config.csv has still default values... Change them before starting the program.")
        if row[0].strip()=="http_proxy":
            http_proxy = row[1].strip()
            if http_proxy=="<<<http_proxy|delete line>>>":
                raise Exception("config.csv has still default values... Change them before starting the program.")
        if row[0].strip()=="https_proxy":
            https_proxy = row[1].strip()
            if https_proxy=="<<<https_proxy|delete line>>>":
                raise Exception("config.csv has still default values... Change them before starting the program.")
        if row[0].strip()=="exclude":
            excludeWehren.append(row[1].strip())
            if row[1].strip()=="<<<building id>>>":
                raise Exception("config.csv has still default values... Change them before starting the program.")

    if proxy:
        proxyDict = {
            "http": http_proxy,
            "https": https_proxy
        }
    else:
        proxyDict = {}

    session = requests.Session()
    parser = etree.HTMLParser()
    r = session.get('https://www.leitstellenspiel.de/users/sign_in', proxies=proxyDict)
    html = r.content.decode("utf-8")
    tree = etree.parse(StringIO(html), parser=parser)
    refs = tree.xpath('/html/head/meta[@name="csrf-token"]/@content')[0]
    #print(refs)

    payload = {'user[email]': username, 'user[password]': password, 'user[remember_me]': '0',
               'utf8': '✓', 'authenticity_token': refs, 'commit': 'Einloggen'}
    r = session.post('https://www.leitstellenspiel.de/users/sign_in', data=payload, proxies=proxyDict)
    #print(session.cookies.get_dict()['_session_id'])

    r = session.get('https://www.leitstellenspiel.de/api/buildings', proxies=proxyDict)
    #print(r.content.decode("utf-8"))
    buildings = json.loads(r.content.decode("utf-8"))

    wehren = []
    for building in buildings:
        if building['building_type'] == 0 and (str(building['id']) not in excludeWehren):
            wehr = Feuerwehr(building['caption'],building['latitude'],building['longitude'],building['id'])
            wehren.append(wehr)

    r = session.get('https://www.leitstellenspiel.de/api/vehicles', proxies=proxyDict)
    # print(r.content.decode("utf-8"))
    vehicles = json.loads(r.content.decode("utf-8"))

    for vehicle in vehicles:
        if vehicle['vehicle_type'] == 0 or vehicle['vehicle_type'] == 1 or vehicle['vehicle_type'] == 6 or vehicle['vehicle_type'] == 7 or vehicle['vehicle_type'] == 8 or vehicle['vehicle_type'] == 9 or vehicle['vehicle_type'] == 17 or vehicle['vehicle_type'] == 18 or vehicle['vehicle_type'] == 19 or vehicle['vehicle_type'] == 7 or vehicle['vehicle_type'] == 20 or vehicle['vehicle_type'] == 21 or vehicle['vehicle_type'] == 22 or vehicle['vehicle_type'] == 23 or vehicle['vehicle_type'] == 24 or vehicle['vehicle_type'] == 25 or vehicle['vehicle_type'] == 26 or vehicle['vehicle_type'] == 37:
            for wehr in wehren:
                if wehr.id==vehicle['building_id']:
                    wehr.addFahrzeug("tlf")
        if vehicle['vehicle_type'] == 2:
            for wehr in wehren:
                if wehr.id==vehicle['building_id']:
                    wehr.addFahrzeug("dlk")
        if vehicle['vehicle_type'] == 3:
            for wehr in wehren:
                if wehr.id==vehicle['building_id']:
                    wehr.addFahrzeug("elw1")
        if vehicle['vehicle_type'] == 4 or vehicle['vehicle_type'] == 47:
            for wehr in wehren:
                if wehr.id==vehicle['building_id']:
                    wehr.addFahrzeug("rw")
        if vehicle['vehicle_type'] == 5 or vehicle['vehicle_type'] == 48:
            for wehr in wehren:
                if wehr.id==vehicle['building_id']:
                    wehr.addFahrzeug("gwA")
        if vehicle['vehicle_type'] == 10 or vehicle['vehicle_type'] == 49:
            for wehr in wehren:
                if wehr.id==vehicle['building_id']:
                    wehr.addFahrzeug("gwOel")
        if vehicle['vehicle_type'] == 11 or vehicle['vehicle_type'] == 13 or vehicle['vehicle_type'] == 14 or vehicle['vehicle_type'] == 15 or vehicle['vehicle_type'] == 16:
            for wehr in wehren:
                if wehr.id==vehicle['building_id']:
                    wehr.addFahrzeug("gwS")
        if vehicle['vehicle_type'] == 12:
            for wehr in wehren:
                if wehr.id==vehicle['building_id']:
                    wehr.addFahrzeug("mess")
        if vehicle['vehicle_type'] == 27:
            for wehr in wehren:
                if wehr.id==vehicle['building_id']:
                    wehr.addFahrzeug("gwG")
        if vehicle['vehicle_type'] == 30:
            for wehr in wehren:
                if wehr.id==vehicle['building_id']:
                    wehr.addFahrzeug("hlf")
        if vehicle['vehicle_type'] == 33:
            for wehr in wehren:
                if wehr.id==vehicle['building_id']:
                    wehr.addFahrzeug("hoeh")
        if vehicle['vehicle_type'] == 34:
            for wehr in wehren:
                if wehr.id==vehicle['building_id']:
                    wehr.addFahrzeug("elw2")
        if vehicle['vehicle_type'] == 53 or vehicle['vehicle_type'] == 54:
            for wehr in wehren:
                if wehr.id==vehicle['building_id']:
                    wehr.addFahrzeug("dekonP")
        if vehicle['vehicle_type'] == 57:
            for wehr in wehren:
                if wehr.id==vehicle['building_id']:
                    wehr.addFahrzeug("fwk")

    try:
        data = csv.reader(open('verbindungen.csv', "r", encoding='ansi'))
    except:
        try:
            data = csv.reader(open('../../verbindungen.csv', "r", encoding='ansi'))
        except:
            data = []
    for row in data:
        if len(row)>1:
            getWehr(wehren,row[0].strip()).addNeibor(getWehr(wehren,row[1].strip()))
            getWehr(wehren,row[1].strip()).addNeibor(getWehr(wehren,row[0].strip()))

    data = "!!python/object:networkx.classes.graph.Graph\n"
    data += "_adj:\n"
    for wehr in wehren:
        data += "  " + wehr.name + ":\n"
        for neibor in wehr.neibors:
            data += "    " + neibor.name + ": {}\n"
        data += "    " + wehr.name + ": {}\n"
    data += "_node: &id001\n"
    for wehr in wehren:
        data += "  " + wehr.name + ": {pos_x: " + str(wehr.pos_x) + ", pos_y: " + str(wehr.pos_y) + ", tlf: " + str(wehr.getTLFs()) + ", elw1: " + str(wehr.getELW1s()) + ", dlk: " + str(wehr.getDLKs()) + ", rw: " + str(wehr.getRWs()) + ", hlf: " + str(wehr.getHLFs()) + ", gwOel: " + str(wehr.getGWOELs()) + ", gwA: " + str(wehr.getGWAs()) + ", gwS: " + str(wehr.getGWSs()) + ", hoeh: " + str(wehr.getHOEHs()) + ", mess: " + str(wehr.getMESSs()) + ", gwG: " + str(wehr.getGWGs()) + ", elw2: " + str(wehr.getELW2s()) + ", dekonP: " + str(wehr.getDEKONPs()) + ", fwk: " + str(wehr.getFWKs()) + "}\n"
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

    return wehren
