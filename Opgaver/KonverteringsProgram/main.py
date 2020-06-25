from Menu import Menu
from Selector import Selector
menu = Menu()
programKøre = True
while(programKøre):
    menu.printMenu()
    brugervalg = input("Vælg menupunkt")
    if brugervalg == "1":
        tempSelector = Selector()
        tempSelector.TemperatureConvertSelector()
    elif brugervalg == "2":
        print("Du valgte 2")
    elif brugervalg == "3":
        print("Du valgte 3")
    elif brugervalg == "4":
        print("du valgte 4")
    elif brugervalg == "5":
        programKøre = False
print("Programmet er slut")