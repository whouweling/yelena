# Yelena
Basic Python based home automation, build for RFXCom and KlikAanKlikUit

**Warning:** If you are looking for easy-to-use out of the box home automation, this isn't what you are looking for! Try something like http://www.openhab.org/

![Screenshot of the webinterface](/screenshot.png?raw=true "Screenshot of the webinterface")

**What is this?**

Basic Python based home automation, features:

 - Switching lights
 - Dimming 
 - Presence detectors (are the home owners around; uses ping to detect if known phones are connected to WIFI)
 - Motion sensor
 - Twilight sensor
 - Temp & Hum sensor
 - RFXCom + Lighting5 protocol (KlikAanKlikUit)
 - Basic alarm function
 - Very basic rule engine
 - Simple webinterface

Currently supports RFXCom only (since that is what I use at home) but should be easy to extend with other transceivers / protocols.

All configuration is done in Python itself, including the rules for automatic switching.

The current rule based automation needs some improvement. The current setup does not handle confliting rules well.

