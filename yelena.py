#!/usr/bin/env python3

VERSION = "0.3"

import sys

try:
    import settings
except ImportError:
    print("Error: missing 'settings.py'")
    sys.exit(1)

from lib.context import Context
from lib.core import Core
from lib.webserver import Webserver

import logging

if __name__ == '__main__':

    logging.info("Yelena, version {version} starting ...".format(version=VERSION))

    context = Context()
    core = Core(context=context)
    webserver = Webserver(core=core,
                          context=context)
    webserver.start()

    core.start()
