# to update screen resolution, see line 5 of ./interface.py
# to update the number of attempts for connecting to time server, see line 20 of ./clock.py

import interface
import pygame # redundant, but forces pydroid to use pygame display instead of terminal
import clock, traffic

testLight = traffic.init_light("230676481", 3)

status = ""
while interface.running():
    currentTime = clock.updateTime(0.1) + 0 # refresh period (sec), offset (sec)

    # if the status changed, play audio and update the screen
    if (testLight.getStatus(currentTime) != status):
        status = testLight.getStatus(currentTime)
        interface.updateStatus(status)
        print("Status of " + testLight.id + ": " + status)

interface.pygame.quit()
