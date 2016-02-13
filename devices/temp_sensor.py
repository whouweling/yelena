import time

from devices.base import SensorDevice


class TempSensor(SensorDevice):

    def __init__(self, name, id):
        super(TempSensor, self).__init__(name)
        self.id = id
        self.temp = None

    def detected(self, temp):
        self.temp = temp
        self.log("temp %s" % temp)

    def get_status(self):
        return self.temp
