# Import SenseHat
from sense_hat import SenseHat
# Import MQTTPub module.
import MQTTPub

# Module for getting the temperature from the raspberryPi SenseHat humidity sensor.
class GetTemperature:
    
    # Initiates SenseHat
    def __init__(self):
        self.sense = SenseHat()
    
    # Gets temperature from the humidity sensor.
    def getTemp(self):
        temp = self.sense.get_temperature_from_humidity()
        MQTTPub.run("bedroom", temp)
        print("The current temperature is: %s C" % temp)
        maxTemp = input("Enter the maximum temperature: ")
        print("The maximum temperature is: " + maxTemp)
        minTemp = input("Enter the minimum temperature: ")
        print("The minimum temperature is: " + minTemp)
        temperature = (temp)
        maximum = float(maxTemp)
        minimum = float(minTemp)
        
        if temperature > maximum:
            notification = "Too Hot"
            print("The notification variable is now " + notification)
            return notification
        elif temperature < minimum:
            notification = "Too Cold"
            print("The notification variable is now " + notification)
            return notification
        else:
            notification = "Just Right"
            print("The notification variable is now " + notification)
            return notification
        





    
    