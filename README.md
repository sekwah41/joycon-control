joycon-interface

I will not make a guide on how to use or set this all up. This was more for fun, a proof of concept, ease of use,
testing and to show off to some friends.

Designed to be auto started on a RaspberryPi hosting it's own WiFi hotspot.

This can technically be fully done on a phone but OnePlus and certain other manufacturers as they don't have a Bluetooth HID Profile
and I don't want to buy a new phone just to toy with this.

I couldn't be asked to write an android app from scratch for something I don't plan to continue maintaining.

Originally I wanted to make a 100% hardware only solution with a dial but I didn't feel it was worth using a whole pi and making a case for now.

To run you need to use

Install the libs needed first using `pip install -r requirements.txt` then follow setup in `/joycon`

As some of the underlying scripts needs python3  
`sudo python3 startup.py`
