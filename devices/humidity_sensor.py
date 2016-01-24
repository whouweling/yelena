from devices.base import SensorDevice
import time


class HumiditySensor(SensorDevice):

    def __init__(self, name, id):
        super(HumiditySensor, self).__init__(name)
        self.id = id
        self.humidity = None

    def detected(self, humidity):
        self.humidity = humidity
        self.log("detected humidity %s" % humidity)

    def get_status(self):
        return self.humidity
