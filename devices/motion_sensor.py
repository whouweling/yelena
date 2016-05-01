from devices.base import SensorDevice
import time


class MotionSensor(SensorDevice):

    def __init__(self, name, id, timeout=10):
        super(MotionSensor, self).__init__(name)
        self.id = id
        self.motion = None
        self.timeout = timeout

    def detected(self):
        if self.motion:
           if time.time() < (self.motion + self.timeout):
              self.log("motion detected")
        self.motion = time.time()

    def switch(self, to):
        self.motion = time.time()

    def get_status(self):

        if not self.motion:
            return False

        if time.time() < (self.motion + self.timeout):
            return True

        return False
