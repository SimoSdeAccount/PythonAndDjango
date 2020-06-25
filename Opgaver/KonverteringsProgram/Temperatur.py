class Temperatur:
    convertVal = 0
    def __init__(self, Val):
        self.convertVal = Val

    def CelsiusToFahrenheit(self):
        return self.convertVal * 9/5 + 32
    
    def CelsiusToKelvin(self):
        return self.convertVal + 273.15

    def FahrenheitToCelsius(self):
        return (self.convertVal - 32)*5/9

    def FahrenheitToKelvin(self):
        return "kage"

    def KelvinToCelsius(self):
        return "kage"
    
    def KelvinToFahrenheit(self):
        return "kage"