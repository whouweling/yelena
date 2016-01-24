from datetime import datetime


def to_date_time(string):

   now = datetime.now()
   (hours, minutes) = string.split(":")
   return datetime(year=now.year, month=now.month, day=now.day,hour=int(hours), minute=int(minutes))
