from devices.base import SensorDevice
import time


class TempSensor(SensorDevice):

    def __init__(self, name, id):
        super(TempSensor, self).__init__(name)
        self.id = id
        self.temp = None

    def detected(self, temp):
        self.temp = temp
        self.log("detected temp %s" % temp)

    def get_status(self):
        return self.temp
