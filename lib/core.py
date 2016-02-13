import json
import threading
from datetime import datetime
import time
import requests
import binascii

from devices.base import devices
from devices.base import get_device
from lib.rule import rules
from lib.log import get_logger
from lib.util import to_date_time

import settings

class Core():

   def __init__(self, context):
     super(Core, self).__init__()
     self.context = context
     self.alarm_switch = False
     self.last_rule = None
     context.update("ai", False)

   def start(self):
    while True:
      if self.context.get("ai"):
        for rule in rules:
            if rule.check():
                if self.last_rule != rule:
                    rule.activate()
                    get_logger().event("rule", "rule '%s' activated" % rule.name)
                    self.context.update("auto-status", rule.name)
                    self.last_rule = rule
                break

      for device in devices:
          device.run()

      time.sleep(3)

   def notify(self, msg):
      print(" *** {msg}".format(msg=msg))

   def execute(self, action, target=None):

       if action == "switch":
            device = get_device(target)
            device.switch(not device.get_status())
            get_logger().event("rule", "manually switched '%s' to '%s'" % (device.name, ("on" if device.get_status() else "off")))


       if action == "dim":
            device = get_device(target)
            device.dim()

       if action == "undim":
           device = get_device(target)
           device.undim()

       if action == "toggle_ai":
           self.context.update("ai", not self.context.get("ai"))


