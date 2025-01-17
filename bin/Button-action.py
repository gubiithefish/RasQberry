#!/usr/bin/env python3

# add to /etc/rc.local with
# /usr/bin/python3 /home/pi/.local/bin/Button-action.py
# Button 1: GPIO Button 16 / LED 12, RasQ-LED clear / LED start
# fyi: GPIO Button 24 / LED 23  also works

# pressed / held logic can be improved according to https://gpiozero.readthedocs.io/en/stable/faq.html#how-do-i-use-button-when-pressed-and-button-when-held-together


# better for shutdown/reboot: https://gist.github.com/lbussy/9e81cbcc617952f1250e353bd42e7775
# Add the following three lines to your /boot/config.txt:
# enable shutdown/reboot on GPIO 3; and LED power indicator on GPIO 4
# dtoverlay=gpio-shutdown,gpio_pin=3
# gpio=4=op,dh


from gpiozero import Button, LED
from signal import pause
from time import sleep
from subprocess import Popen
#import os


Button.was_held = False

def pressed1():
    for x in range(2):
      led1.off()
      sleep(0.2)
      led1.on()
      sleep(0.2)
    #print("pressed1")
    #os.system("touch /home/pi/pressed1")
    Popen(["/usr/bin/python3", "/home/pi/.local/bin/rq_LED-off.py"])

def released1(btn):
    if not btn.was_held:
        pressed1()
    btn.was_held = False
    led1.off()
    #print("released1")
    #os.system("touch /home/pi/released1")

def held1(btn):
    btn.was_held = True
    for x in range(5):
      led1.off()
      sleep(0.1)
      led1.on()
      sleep(0.1)
    #print("held1")
    #os.system("touch /home/pi/held1")
    Popen(["/usr/bin/sudo", "-u", "pi", "-H", "/usr/bin/python3", "/home/pi/RasQberry/demos/bin/RasQ-LED.py"])


button1 = Button(16, hold_time=2)
led1 = LED(12)

#button1.when_pressed = pressed1
button1.when_held = held1
button1.when_released = released1

pause()