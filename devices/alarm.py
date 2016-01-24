
from devices.base import SensorDevice
import subprocess
from devices.base import devices
from devices.base import get_device
from devices.light import Light
from devices.dimmer import Dimmer

import time

class Alarm(SensorDevice):


    def __init__(self, name, notify=None, timeout=None):
        self.notify = None
        super(Alarm, self).__init__(name)
        self.state_on = True
        self.alarm = False
        self.notify = notify
        self.timeout = timeout
        self.last_activated = None


    def switch(self, status):

        if not self.alarm and status:
            self.log("alarm activated")
            self.last_activated = time.time()

        if self.alarm and not status:
            self.log("alarm de-activated")

        self.alarm = status

    def log(self, msg):
        super(Alarm, self).log(msg)
        if self.notify:
            get_device(self.notify).notify(msg)

    def run(self):

        if self.alarm:

            if time.time() < (self.last_activated + self.timeout):

                for device in devices:
                    if isinstance(device, Light) or isinstance(device, Dimmer):
                        device.switch(self.state_on)

                self.state_on = not self.state_on

    def get_status(self):
        return self.alarm