from appJar import gui

def loadData():
    x = open("airports.dat", "r")
    for line in x:
        print(line)

def main():
    loadData()
    app = gui()
    app.addLabel("My Test Project")
    app.go()

main()