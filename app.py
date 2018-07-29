import appJar
from appJar import gui

APTDICT = {}

def loadData():
    x = open("airports.dat", "r", encoding="utf8")
    for lines in x:
        tempDict = {}
        g = lines.split(',')
        
        name = g[1].strip('"')
        city = g[2].strip('"')
        country = g[3].strip('"')
        icaoCode = g[5].strip('"')
        tempDict = {"Name" : name, "City" : city, "Country" : country, "ICAO" : icaoCode}
        
        APTDICT[name] = tempDict
    x.close()

def main():
    loadData()
    #print(APTDICT["Tucson International Airport"])

    for (k, v) in APTDICT.items():
        if v['City'] == "Tucson":
            print(k)

    app = gui()
    app.addLabel("My Test Project")
    #app.go()

main()