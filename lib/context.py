import time


class Context():

   def __init__(self):
      self._context = {}
      self._last_change = {}
      self._last_seen = {}
      self._timeout = {}

   def update(self, key, value, timeout=None):
      self._last_seen[key] = time.time()
      if not key in self._context or self._context[key] != value  \
         or (key in self._timeout and self._timeout[key] < time.time()):

         self._context[key] = value
         self._last_change[key] = time.time()
         if timeout:
            self._timeout[key] = time.time() + timeout
         print("Context: '{key}' changed to '{value}'".format(key=key,
                                                              value=value))
   def get(self, key):

      if not key in self._context:
         return None

      if key in self._timeout and self._timeout[key] < time.time():
         return None

      return self._context[key]

   def last_seen(self, key):
      if not key in self._last_seen:
         return None

      return time.time() - self._last_seen[key]

   def serialize(self):
      return self._context