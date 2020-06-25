import random

def PrintSlutterPaa7():
    tal = 7
    while tal < 1000:
        print(tal)
        tal += 10

def SumOpTilN(n):
    counter = 0
    summer = 0
    while counter <= n:
        summer += counter
        counter += 1
    print(summer)

def Ugedag(dag):
    ugeDage = {1: "Mandag", 2: "Tirsdag", 3: "Onsdag", 4: "Torsdag", 5: "Fredag", 6: "Lørdag", 7: "Søndag"}
    print(ugeDage[dag])

def TerningSlag(terningAntal):
    terningsummer = 0
    counter = 0
    while counter < terningAntal:
        tempKast = random.randint(1,6)
        terningsummer += tempKast
        print(tempKast)
        counter += 1
    print(terningsummer)

def Divisible3og5(n):
    tal = 0
    talsum = 0
    while tal <= n:
        if(tal % 3 == 0 and tal % 5 == 0):
            print(tal)
            talsum += tal
            tal += 1
        else:
            tal += 1
    print(talsum)
def Fibbo01(n):
    summer = 0
    a = 0
    b = 1
    while a <= n:
        temp = a
        if a % 2 == 0:
            print(a)
            summer += a
        a = b
        b = temp + b
    print(summer)

def Fibbo02(n):
    summer = 0
    counter = 1
    fibboList = [1, 2]
    ligefibboList = []
    while True:
        tempNumber = fibboList[counter-1] + fibboList[counter]
        if(tempNumber < n):
            fibboList.append(tempNumber)
            counter += 1
        else:
            break
    counter = 0
    ligefibboindex = 0
    while counter < len(fibboList):
        if(fibboList[counter] % 2 == 0):
            ligefibboList.append(fibboList[counter])
            summer += ligefibboList[ligefibboindex]
            ligefibboindex += 1
        counter += 1
    print(ligefibboList)
    print(summer)


def getPrimtal(n):

    def genPotPrime(bummelum):
        potprime = 2
        primeCounter = 1
        while primeCounter < bummelum:
            potprime += 1
            primeStatus = isPrime(potprime)
            if primeStatus == True:
                primeCounter += 1
                print(str(potprime) + " " + str(primeCounter))
                
    def isPrime(potPrime):
        count = 2
        while count < potPrime:
            if potPrime % count == 0:
                return False
            count += 1
        return True
    genPotPrime(n)

def getPrimeSum(n):
    def genPrimeSum(bummelum):
        potprime = 2
        summer = 2
        while potprime < bummelum:
            potprime += 1
            primeStatus = isPrime(potprime)
            if primeStatus == True:
                summer += potprime
        print(summer)
    def isPrime(potPrime):
        count = 2
        while count < potPrime:
            if potPrime % count == 0:
                return False
            count += 1
        return True
    genPrimeSum(n)
def GaetteSpil():
    spilIgang = True
    while(spilIgang):
        spilValg = ""
        while((spilValg != "s" and spilValg != "S") and (spilValg != "q" and spilValg != "Q")):
            spilValg = input("tast S hvis du vil starte nyt spil og Q hvis du vil afslutte spil")
        if spilValg == "s" or spilValg == "S":
            tal = random.randint(1, 6)
            gaet = int(input("Skriv bud på genereret tal"))
            while(gaet != tal):
                if gaet < tal:
                    print("Gættet var mindre end")
                else:
                    print("gættet var større end  tallet")
                gaet = int(input("Skriv bud på genereret tal"))
            print("Tillykke du gættede tallet")
        else:
            spilIgang = False
    print("Spillet er nu afsluttet")

def talSort():
    talArr = [4, 9, 7, 1, 6, 5, 7, 9, 2]
    sortedTalArr = []
    outerCount = 0
    origiLength = len(talArr)
    while(outerCount < origiLength):
        innerCount = 0
        smallestIndex = 0
        potSmallest = talArr[0]
        while(innerCount < len(talArr)):
            if talArr[innerCount] < potSmallest:
                potSmallest = talArr[innerCount]
                smallestIndex = innerCount
            innerCount += 1
        sortedTalArr.append(potSmallest)
        talArr.pop(smallestIndex)
        outerCount += 1
    for i in sortedTalArr:
        print(i)

def OrdSortering01(ord):
    alfabet = [["a", 0], ["b", 1], ["c", 2], ["d", 3], ["e", 4], ["f", 5], ["g", 6], ["h", 7], ["i", 8], ["j", 9], ["k", 10], ["l", 11], ["m", 12], ["n", 13], ["o", 14], ["p", 15], ["q", 16], ["r", 17], ["s", 18], ["t", 19], ["u", 20], ["v", 21], ["w", 22], ["x", 23], ["y", 24], ["z", 25]]
    newOrdArr = ord.split(" ")
    multiArr = []
    sortedArr = []
    outerCount = 0
    innerCount = 0
    origiLength = len(newOrdArr)
    while(outerCount < origiLength):
        innerCount = 0
        while(innerCount < len(alfabet)):
            if newOrdArr[outerCount][0] == alfabet[innerCount][0]:
                multiArr.append([newOrdArr[outerCount], alfabet[innerCount][1]])
            innerCount += 1
        outerCount += 1
    outerCount = 0
    innerCount = 0
    smallestIndex = 0
    while(outerCount < origiLength):
        innerCount = 0
        smallestIndex = 0
        potSmallest = multiArr[0][1]
        while(innerCount < len(multiArr)):
            if multiArr[innerCount][1] < potSmallest:
                potSmallest = multiArr[innerCount][1]
                smallestIndex = innerCount
            innerCount += 1
        sortedArr.append(multiArr[smallestIndex][0])
        multiArr.pop(smallestIndex)
        outerCount += 1
    print(sortedArr)
        
def OrdRendser(Ord):
    OrdArr = Ord.split(" ")
    print(OrdArr)
    outerCount = 0
    innerCount = 0
    while(outerCount < len(OrdArr)):
        innerCount = outerCount + 1
        while(innerCount < len(OrdArr)):
            if OrdArr[outerCount] == OrdArr[innerCount]:
                OrdArr.pop(innerCount)
            innerCount += 1
        outerCount += 1
    OrdArr.sort()
    outerCount = 0
    while(outerCount < len(OrdArr)):
        print(OrdArr[outerCount])
        outerCount += 1

def TekstStatistik(Ord):
    OrdArr = Ord.split(" ")
    ordCounter = 0
    bogstavCounter = 0
    mellemrumCounter = 0
    symbolCounter = 0
    storbogstavCounter = 0
    talCounter = 0
    NumericString = False
    for i in OrdArr:
        if i.isnumeric():
            talCounter += 1
            NumericString = True
        for j in i:
            if j.isupper():
                storbogstavCounter += 1
                bogstavCounter += 1
            if j.islower():

                bogstavCounter += 1
            if j.isnumeric():
                if NumericString == False:
                    talCounter += 1
            if j == "," or j == "." or j == ";" or j == ":" or j == "-":
                symbolCounter += 1
        if i != "," and i != "." and i != ";" and i != ":" and i != "-" and NumericString != True:
            ordCounter += 1
        NumericString = False
    mellemrumCounter = len(OrdArr) - 1
    print("Ord:")
    print(ordCounter)
    print("Bogstaver:")
    print(bogstavCounter)
    print("Mellemrum:")
    print(mellemrumCounter)
    print("Symboler:")
    print(symbolCounter)
    print("Store bogstaver:")
    print(storbogstavCounter)
    print("Tal:")
    print(talCounter)

def CollatzSekvens(n):
    sekvensSteps = []
    while(n > 2):
        startTal = n
        StartStartTal = n
        sekvensCounter = 1
        while(startTal > 2):
            if startTal % 2 == 0:
                sekvensCounter += 1
                startTal = startTal / 2
            if startTal % 2 != 0:
                sekvensCounter += 1
                startTal = 3*startTal + 1
        tempArr = [StartStartTal, sekvensCounter + 1]
        sekvensSteps.append(tempArr)
        n -= 1
    count = 0
    while(count < len(sekvensSteps)):
        print("****************************************************************")
        print(sekvensSteps[count][0])
        print(sekvensSteps[count][1])
        count += 1
    count = 0
    nVal = 0
    potHighest = sekvensSteps[0][1]
    while(count < len(sekvensSteps)):
        if potHighest < sekvensSteps[count][1]:
            potHighest = sekvensSteps[count][1]
            nVal = sekvensSteps[count][0]
        count += 1
    print(nVal)
    print(potHighest)

def EnderPaa13(n):
    count = 0
    summer = 0
    while(count < n-100):
        summer += count
        count += 100
    print(summer)

def KalenderSystem(antalDage, startDag):
    count = 1
    ugeLoopCount = 0
    ugeListe = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]

    if startDag == "Mandag":
        ugeLoopCount = 0
    elif startDag == "Tirsdag":
        ugeLoopCount = 1
    elif startDag == "Onsdag":
        ugeLoopCount = 2
    elif startDag == "Torsdag":
        ugeLoopCount = 3
    elif startDag == "Fredag":
        ugeLoopCount = 4
    elif startDag == "Lørdag":
        ugeLoopCount = 5
    elif startDag == "Søndag":
        ugeLoopCount = 6
    else:
        print("Forkert input")

    while(count <= antalDage):
        if(ugeLoopCount == 7):
            ugeLoopCount = 0
        print(str(count) + " " + ugeListe[ugeLoopCount])
        ugeLoopCount += 1
        count += 1

def SteenSaksPapir():
    spilIgang = True
    while(spilIgang):
        brugerValg = input("Tast s for at starte spil, tast q for at afslutte")
        if brugerValg == "s":
            runder = int(input("Intast antal runder du vil spille mod computeren"))
            spillerPoint = 0
            computerPoint = 0
            rundeCount = 0
            while(rundeCount < runder):
                computerhaand = random.randint(1,3)
                haand = input("Indtast haand du vil spille: Sten, Saks eller Papir")
                if computerhaand == 1:
                    if haand == "Sten":
                        print("Draw")
                    elif haand == "Saks":
                        print("Computeren slog Sten, computeren vandt")
                        computerPoint += 1
                        spillerPoint -= 1
                    elif haand == "Papir":
                        print("Computeren slog papir, du vandt")
                        spillerPoint += 1
                        computerPoint -= 1
                elif computerhaand == 2:
                    if haand == "Sten":
                        print("Computeren slog saks, du vandt")
                        spillerPoint += 1
                        computerPoint -= 1
                    elif haand == "Saks":
                        print("Draw")
                    elif haand == "Papir":
                        print("Computeren slog saks, computeren vandt")
                        computerPoint += 1
                        spillerPoint -= 1
                elif computerhaand == 3:
                    if haand == "Sten":
                        print("Computeren slog papir, computeren vandt")
                        computerPoint += 1
                        spillerPoint -=1
                    elif haand == "Saks":
                        print("Computeren slog papir, du vandt")
                        computerPoint -= 1
                        spillerPoint += 1
                    elif haand == "Papir":
                        print("Draw")
                rundeCount += 1
            if spillerPoint > computerPoint:
                print("Du vandt med følgende stilling")
                print("Spiller: " + str(spillerPoint) + " Point, Computer: " + str(computerPoint) + "Point")
            elif computerPoint > spillerPoint:
                print("Du table med følgende stilling")
                print("Spiller: " + str(spillerPoint) + " Point, Computer: " + str(computerPoint) + "Point")
            else:
                print("Stillingen blev uafgjort")
            input("Tryk på en vilkår tast for at fortsætte")
        elif brugerValg == "q":
            spilIgang = False
        else:
            print("ugyldigt input")
    print("Du har afsluttet spillet")
def TerningSimulator(dices):
    terningArr = dices.split(" ")
    count = 0
    summer = 0
    while(count < len(terningArr)):
        terningValArr = terningArr[count].split("D")
        innerCount = 0
        while(innerCount < int(terningValArr[0])):
            slag = random.randint(1, int(terningValArr[1]))
            print("D" + terningValArr[1] + ": " +  str(slag))
            summer += slag
            innerCount += 1
        count  += 1
    print("sum" + summer)
TerningSimulator("2D20 3D8 1D6")
#SteenSaksPapir()
#KalenderSystem(31, "Søndag")
#EnderPaa13(1001)
#CollatzSekvens(50)
#TekstStatistik("Dette er en saetning, med23 komma og punktum. Nu er der en bindestreg - et kolon : et semikolon; 12345") //skal vende tilbage til
#OrdRendser("sko blyant taske sko blyant kugelpen")
#OrdSortering01("denne her har lister fra")
#talSort()
#GaetteSpil()
#getPrimeSum(10)
#getPrimtal(10001)
#Fibbo01(55)
#Fibbo02(55)
#skal vende tilbage til
#PrintSlutterPaa7()
#SumOpTilN(3)
#Ugedag(3)
#TerningSlag(4)
#Divisible3og5(1000)
