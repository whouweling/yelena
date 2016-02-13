from datetime import datetime
import logging

from devices.base import get_device
from devices.base import devices


class Action:

    def execute(self):
        raise NotImplementedError()


class SwitchAction(Action):

    def __init__(self, device, switch):
        self.device = device
        self.switch = switch

    def execute(self):
        logging.debug("executing action switch '%s' on device '%s' to '%s'" % (self.__class__.__name__,
                                                                               self.device,
                                                                               self.switch))

        get_device(self.device).switch(self.switch)


class SwitchAllAction(Action):

    def __init__(self, switch, type):
        self.switch = switch
        self.type = type

    def execute(self):
        for device in devices:
            if isinstance(device, self.type):
                logging.debug("executing action switch '%s' on device '%s' to '%s'" % (self.__class__.__name__,
                                                                                   device,
                                                                                   self.switch))

                device.switch(self.switch)

