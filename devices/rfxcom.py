from devices.base import CommsDevice
import asyncio
from asyncio import get_event_loop
from rfxcom import protocol
from rfxcom.transport import AsyncioTransport
from rfxcom.protocol import TempHumidity
from devices.base import devices
import binascii
from devices.temp_sensor import TempSensor
from devices.humidity_sensor import HumiditySensor
from devices.motion_sensor import MotionSensor
from devices.twilight_sensor import TwilightSensor
import threading
import logging
import settings
import time

from devices.light import Light
from devices.dimmer import Dimmer


class RFXCom(CommsDevice):

    def __init__(self, name, dev):
        super(RFXCom, self).__init__(name)

        def run_event_loop():
             loop = asyncio.new_event_loop()
             asyncio.set_event_loop(loop)
             self.rfxcom = AsyncioTransport(dev,
                                          loop,
                                          callback=self.handler)
             #time.sleep(1)
             #self.rfxcom.write(b'\r\x00\x00\x01\x03S\x00\xff\x0e/\x00\x00\x00\x00')
             loop.run_forever()

        threading.Thread(target=run_event_loop).start()

    def handler(self, packet):

        print(packet)

        if isinstance(packet, TempHumidity):
           for device in devices:
             if isinstance(device, TempSensor):
                if device.id == packet.data['id']:
                  device.detected(packet.data['temperature'])

             if isinstance(device, HumiditySensor):
                if device.id == packet.data['id']:
                  device.detected(packet.data['humidity_status'])

        # Each packet will have a dictionary which contains parsed data.
        print(packet.data)

        command = binascii.hexlify(packet.raw)

        for device in devices:
            try:
                # TODO: need to properly decode the protocol here, this is just lazy :-)
                if hasattr(device, "id") and device.id in command:

                    if isinstance(device, MotionSensor):
                        device.detected()

                    if isinstance(device, TwilightSensor):
                        device.detected(command[21] == 102)

            except TypeError:
                pass

    def switch(self, device, to):

      if device.status == to:
          return

      dim='00'
      logging.info("%s: switching '%s' to '%s'" % (self.name, device.name, to))

      if to:

          if isinstance(device, Light):
             level = "01"

          if isinstance(device, Dimmer):
             level = "02"
             dim = hex(device.level)[2:4]

      else:
          level = "00"

      self.send_command(device, level, dim)

    def send_command(self, device, level, dim):

      command = '0b11000a{id}0a{level}{dim}00'.format(id=device.id,
                                                      level=level,
                                                      dim=dim)
      if not settings.DISARM:
         for i in range(1):
            logging.info("%s: sending command '%s'" % (self.name, command))
            self.rfxcom.write(binascii.unhexlify(command))

    def undim(self, device):

       device.level += 50
       if device.level > 255:
         device.level = 255

       if device.status:
            dim = hex(device.level)[2:4]
            self.send_command(device, "02", dim)

    def dim(self, device):

       device.level -= 50
       if device.level < 1:
         device.level = 1

       if device.status:
            dim = hex(device.level)[2:4]
            self.send_command(device, "02", dim)
