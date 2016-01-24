
# This is an example configuration for Yelena, showing how to define devices & rules.

from devices.light import Light
from devices.dimmer import Dimmer
from devices.motion_sensor import MotionSensor
from devices.presense_detector import PresenceDetector
from devices.twilight_sensor import TwilightSensor
from devices.humidity_sensor import HumiditySensor
from devices.temp_sensor import TempSensor
from devices.base import get_device
from devices.rfxcom import RFXCom
from devices.dummy_com import DummyCom
from devices.alarm import Alarm
from devices.notifier import Notifier
from lib.action import SwitchAction, SwitchAllAction
from lib.rule import Rule
from lib.trigger import SensorTrigger, TimeTrigger, MotionDetectedTrigger



import logging
logging.getLogger().setLevel(logging.DEBUG)

#RFXCom(name="rfxcom1",
#       dev='/dev/serial/by-id/usb-RFXCOM_RFXtrx433_A1Z7CACP-if00-port0')

# The dummy com let's you run Yelena without connected RFXCom hardware
DummyCom(name="rfxcom1")

Notifier(name="push_notification", key="ThzPs3ZnCx")

Dimmer(name="bank",
       id="010a0b21",
       comm="rfxcom1")

Light(name="studio",
      id="010a0b13",
      comm="rfxcom1")

Light(name="aanrecht",
      id="010a0b15",
      comm="rfxcom1")

Dimmer(name="eettafel",
      id="010a0b14",
      comm="rfxcom1")

Dimmer(name="keuken",
       id="010a0b17",
       comm="rfxcom1")

Dimmer(name="zolder-plafond",
       id="010a0b18",
       comm="rfxcom1")

Light(name="zolder-staand",
      id="010a0b12",
      comm="rfxcom1")

Light(name="achterdeur",
      id="010a0b16",
      comm="rfxcom1")

Light(name="hal",
      id="010a0b19",
      comm="rfxcom1")

MotionSensor(name="motion1",
             id=b'01069d9a0a')

TwilightSensor(name="twilight1",
               id=b'00e103c60a')

PresenceDetector(name="presence1", ipaddress=["192.168.1.36", "192.168.1.52"], timeout=60*15)

Alarm(name="alarm1",
      notify="push_notification",
      timeout=30)

TempSensor(name='temp_outside', id='0x360E')
HumiditySensor(name='hum_outside', id='0x360E')


Rule(
    name="aanwezig-avond",
    triggers=[
        SensorTrigger(device="presence1",
                      status=True),
        MotionDetectedTrigger(device="motion1",
                              timeout=60*15),
        SensorTrigger(device="twilight1",
                      status=True),
        TimeTrigger(time="16:00",
                    when="after")
    ],
    actions=[
        SwitchAction(device="eettafel",
                     switch=True),
        SwitchAction(device="bank",
                     switch=True),
        SwitchAction(device="studio",
                     switch=True),
        SwitchAction(device="keuken",
                     switch=True),
        SwitchAction(device="aanrecht",
                     switch=True),

        SwitchAction(device="alarm1",
                     switch=False),
    ]
)


Rule(
    name="aanwezig-donker-overdag",
    triggers=[
        SensorTrigger(device="presence1",
                      status=True),
        MotionDetectedTrigger(device="motion1",
                              timeout=60*15),
        SensorTrigger(device="twilight1",
                      status=True),
        TimeTrigger(time="16:00",
                    when="before")
    ],
    actions=[
        SwitchAction(device="eettafel",
                     switch=True),
        SwitchAction(device="alarm1",
                     switch=False),
    ]
)



Rule(
    name="indringer",
    triggers=[
        MotionDetectedTrigger(device="motion1",
                              timeout=30),
        SensorTrigger(device="presence1",
                      status=False),
    ],
    actions=[
        SwitchAction(device="alarm1",
                     switch=True),
    ]
)


Rule(
    name="niemand-thuis-avond",
    triggers=[

        SensorTrigger(device="presence1",
                      status=False),

        TimeTrigger(time="16:00",
                    when="after"),

        TimeTrigger(time="23:30",
                    when="before"),
    ],
    actions=[


        SwitchAllAction(switch=False,
                        type=Light),

        SwitchAllAction(switch=False,
                        type=Dimmer),

        SwitchAction(device="studio",
                     switch=True),
        SwitchAction(device="bank",
                     switch=True),
        SwitchAction(device="keuken",
                     switch=True),

        SwitchAction(device="alarm1",
                     switch=False),
    ]
)

Rule(
    name="rust-stand",
    triggers=[
        SensorTrigger(device="motion1",
                      status=False),
        TimeTrigger(time="00:10",
                    when="after"),
    ],
    actions=[
        SwitchAction(device="alarm1",
                     switch=False),

        SwitchAllAction(switch=False,
                        type=Light),

        SwitchAllAction(switch=False,
                        type=Dimmer),

        SwitchAction(device="alarm1",
                     switch=False),

    ]
)


WEBSERVER_PORT = 8000
NOTIFY = False
DISARM = False
