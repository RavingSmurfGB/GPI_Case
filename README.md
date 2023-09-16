# GPI_Case

This repository documents my efforts to modify a Raspbery pi to run with the Retro Flag GPI case

 A play through the retropie system

To enable enter this file /opt/retropie/configs/all/autostart.sh
- emulationstation #auto
+ python /home/pi/GPI_Case/client.py

Also configure exec permissions for launch_emulationstation.sh launch_game.sh and client.py

The workflow should be:

1. By Defualt on startup a game should launch and not alow the user to exit.
2. Upon Entering a set code, the next bootup should be changed into booting into emulation station
3. Once the device has booted it should set the next boot into the locked game - as described in step 1



Usefull information:

CHANGING THE LAUNCHER SETTINGS CAN BE DONE VIA - Can also start the python file for this script
sudo nano /opt/retropie/configs/all/autostart.sh


perhaps save what start state should be in a file somewehre


Investigate controller stuffs:
         /opt/retropie/configs/all/retroarch-joypads/* # This one in game
        /home/pi/.emulationstation/es_input.cfg # this one in menu



