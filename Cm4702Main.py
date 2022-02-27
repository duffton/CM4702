# Import NotificationLights module.
from NotificationLights import NotificationLights
# import Time module.
import time
    
# Setting variable names for lights and temperature methods.
Lights = NotificationLights()

# Testing light setting.
#loop to keep publishing
i = 1 # testng this
while i == 1: #testing this
    Lights.setLights()
    time.sleep(60) #testing this

    if 1 == 0: #testing this
        break #testing this
