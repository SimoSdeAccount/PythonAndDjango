class Selector:

    def TemperatureConvertSelector(self):
        from Temperatur import Temperatur
        Valg = ""
        TemperaturIgang = True
        while(TemperaturIgang):
            while(Valg != "c" and Valg !="C" and Valg != "f" and Valg != "F"):
                print("tast c for at konvertere fra celsius til fahrenheit")
                print("tast f for at konvertere fra fahrenheit til celsius")
                print("tast q for at vende tilbage til hovedprogram")
                Valg = input("Indtast valg")

            returnVal = ""

            if Valg == "c" or Valg == "C":
                temperatur = float(input("Indtast temperatur"))
                fTemperatur = Temperatur(temperatur)
                returnVal = fTemperatur.CelsiusToFahrenheit()
            elif Valg == "f" or Valg == "F":
                temperatur = float(input("Indtast temperatur"))
                cTemperatur = Temperatur(temperatur)
                returnVal = cTemperatur.FahrenheitToCelsius()
            elif Valg == "q" or Valg == "Q":
                break
            Valg = ""
            print(returnVal)