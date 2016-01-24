
import logging
from devices.base import CommsDevice


class DummyCom(CommsDevice):

    def switch(self, device, to):
        logging.debug("%s: would switch '%s' to '%s'" % (self.name,
                                                         device.name,
                                                         to))

    def dim(self, device):
        device.level -= 10
        logging.debug("%s: would dim '%s' to level '%s'" % (self.name,
                                                            device.name,
                                                            device.level))

    def undim(self, device):
        device.level += 10
        logging.debug("%s: would dim '%s' to level '%s'" % (self.name,
                                                            device.name,
                                                            device.level))