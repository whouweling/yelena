import json
import requests

from devices.base import Device


class Notifier(Device):

    def __init__(self, name, key):
        super(Notifier, self).__init__(name)
        self.id = id
        self.key = key

    def notify(self, msg):
        res = requests.post("https://api.parse.com/1/functions/notify",
                            data=json.dumps({"key": self.key, "text": msg}),
                            headers={
                               "X-Parse-Application-Id": "HQrMLZDevpTv2J1raSC6KATvlpNqqePPecUE0EgG",
                               "X-Parse-REST-API-Key": "ivgV8ZoA0kyOOLWKms3M0wxYUxyUw4tfGgbj6DFd",
                               "Content-Type": "application/json"
                            })
        if res.status_code == 200:
            self.log("notified: '%s'" % msg)
        else:
            self.log("notified: failed to notify: error %s" % res.status_code)

    def get_status(self):
        return True
