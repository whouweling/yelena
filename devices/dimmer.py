from devices.base import Device
from devices.base import get_device


class Dimmer(Device):

    def __init__(self, name, id, comm):
        super(Dimmer, self).__init__(name)
        self.id = id
        self.comm = comm
        self.status = None
        self.level = 255

    def switch(self, to):
        if to != self.status:
            get_device(self.comm).switch(self, to)
            if to:
                self.log("switched on")
            else:
                self.log("switched off")
        self.status = to

    def dim(self):
        get_device(self.comm).dim(self)

    def undim(self):
        get_device(self.comm).undim(self)

    def get_status(self):
        return self.status
