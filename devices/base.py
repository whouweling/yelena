
from lib.log import get_logger

devices = []

class UnkownDeviceError(Exception):
    pass

def get_device(name):
    for device in devices:
        if device.name == name:
            return device
    raise UnkownDeviceError(name)

class Device():

    def __init__(self, name):
        self.name = name
        devices.append(self)
        self.log("registered")

    def log(self, msg):
        get_logger().event("device", "{name}: {msg}".format(
            name=self.name,
            msg=msg
        ))

    def run(self):
        pass

    def set_status(self, *args, **kwargs):
        raise NotImplementedError()

    def get_status(self):
        return None

    def switch(self, to):
        pass


class SensorDevice(Device):
    pass


class SwitchDevice(Device):
    pass

class CommsDevice(Device):
    pass