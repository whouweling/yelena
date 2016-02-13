
from devices.base import SensorDevice
import subprocess
import time


class PresenceDetector(SensorDevice):

    def __init__(self, name, ipaddress, timeout=60):
        super(PresenceDetector, self).__init__(name)
        self.ipaddress = ipaddress
        self.timeout = timeout
        self.last_detected = None

    def switch(self, status):
        self.status = status
        self.last_detected = time.time()

    def run(self):
        for ip in self.ipaddress:
          status, result = subprocess.getstatusoutput("ping -c1 -w2 " + ip)
          if status == 0:
             self.last_detected = time.time()
             return

    def get_status(self):

        if not self.last_detected:
          return False

        return time.time() < (self.last_detected + self.timeout)
