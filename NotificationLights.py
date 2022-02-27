# Import SenseHat.
from sense_hat import SenseHat

# Import GetTemperature module.
from GetTemperature import GetTemperature

# Setting variable names for temperature methods.
Temp = GetTemperature()

# Module for sending red or blue lights to the RaspberryPi if the temperature is too hot or too cold.
class NotificationLights:
    
    notification = (Temp.getTemp())
    
    B = [0, 0, 255] # Blue
    R = [255, 0, 0] # Red
    G = [0, 255, 0] # Green
    O = [0, 0, 0]  # Off
    
    # Lights for testing i.e. green.
    green_lights = [
    O, O, O, O, O, O, O, O,
    O, G, G, G, G, G, G, O,
    O, G, G, G, G, G, G, O,
    O, G, G, O, O, O, O, O,
    O, G, G, O, O, G, G, O,
    O, G, G, G, G, G, G, O,
    O, G, G, G, G, G, G, O,
    O, O, O, O, O, O, O, O 
    ]
    
    # Lights for testing i.e. red.
    red_lights = [
    O, O, O, O, O, O, O, O,
    O, R, R, O, O, R, R, O,
    O, R, R, O, O, R, R, O,
    O, R, R, R, R, R, R, O,
    O, R, R, R, R, R, R, O,
    O, R, R, O, O, R, R, O,
    O, R, R, O, O, R, R, O,
    O, O, O, O, O, O, O, O 
    ]
    
    # Lights for testing i.e. blue.
    blue_lights = [
    O, O, O, O, O, O, O, O,
    O, B, B, B, B, B, B, O,
    O, B, B, B, B, B, B, O,
    O, B, B, O, O, O, O, O,
    O, B, B, O, O, O, O, O,
    O, B, B, B, B, B, B, O,
    O, B, B, B, B, B, B, O,
    O, O, O, O, O, O, O, O 
    ]

    # Lights for testing i.e. off.
    no_lights = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O 
    ]

    # Initiates SenseHat
    def __init__(self):
        self.sense = SenseHat()
    
    # Sets green lights.
    def greenLights(self):
        # self.colour = "green"
        self.sense.set_pixels(self.green_lights)
    
    # Sets red lights.
    def redLights(self):
        # self.colour = "red"
        self.sense.set_pixels(self.red_lights)
    
    # Sets blue lights.
    def blueLights(self):
        # self.colour = "blue":
        self.sense.set_pixels(self.blue_lights)
        
    # Turns lights off.
    def offLights(self):
        # self.colour = "off":
        self.sense.set_pixels(self.no_lights)
        
    # Determines lights to set and calls light methods.
    def setLights(self):
        self.notification = Temp.getTemp()
        print("The notification value for the lights is " + self.notification)
        if self.notification == "Too Hot":
            self.redLights()
        elif self.notification == "Too Cold":
            self.blueLights()
        else:
            self.greenLights()



