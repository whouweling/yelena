import time

from devices.base import SensorDevice

class TwilightSensor(SensorDevice):

    def __init__(self, name, id, timeout=600):
        super(TwilightSensor, self).__init__(name)
        self.id = id
        self.twilight = None

    def switch(self, status):
        self.twilight = status

    def detected(self, twilight):
        self.twilight = twilight
        if twilight:
            self.log("detected darkness")
        else:  
            self.log("detected light")

    def get_status(self):
        return self.twilight
