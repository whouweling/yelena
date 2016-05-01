from datetime import datetime
from devices.base import get_device
import time

class Condition:

    def check(self):
        raise NotImplementedError()


class TimeCondition(Condition):

    def __init__(self, time, when):

        self.when = when

        (hours, minutes) = time.split(":")

        self.minute = int(hours) * 60 + int(minutes)

    def check(self):

        now = datetime.now()

        if self.when == "before":
            if now.hour * 60 + now.minute < self.minute:
                return True
        else:
            if now.hour * 60 + now.minute > self.minute:
                return True

        return False


class SensorCondition(Condition):

    def __init__(self, device=None, status=None):
        self.device = device
        self.status = status

    def check(self):
        return get_device(self.device).get_status() == self.status


class MotionDetectedCondition(Condition):

    def __init__(self, device=None, timeout=60):
        self.device = device
        self.timeout = timeout

    def check(self):
        sensor = get_device(self.device)
        if not sensor.motion:
           return False

        return time.time() < (sensor.motion + self.timeout)


