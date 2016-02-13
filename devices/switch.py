from devices.base import SwitchDevice
from devices.base import get_device


class Switch(SwitchDevice):

    def __init__(self, name, id, comm):
        super(Switch, self).__init__(name)
        self.id = id
        self.status = None
        self.comm = comm

    def switch(self, to):
        if to != self.status:
            get_device(self.comm).switch(self, to)
            if to:
                self.log("switched on")
            else:
                self.log("switched off")
        self.status = to

    def get_status(self):
        return self.status
