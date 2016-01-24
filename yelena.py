import binascii
import sys

from lib.context import Context
from lib.core import Core
from lib.webserver import Webserver

from datetime import datetime

import logging


import settings


context = Context()

core = Core(context=context)

webserver = Webserver(core=core,
                      context=context)
webserver.start()

core.start()
