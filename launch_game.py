
import os, time
from datetime import datetime




#def toggle_screen(toggle):
#    subprocess.call(["vcgencmd", "display_power", toggle])

#time.sleep(2)

os.system("/opt/retropie/supplementary/runcommand/runcommand.sh 0 _SYS_ snes '/home/pi/RetroPie/roms/snes/test.smc'")

time.sleep(5)
os.system("emulationstation")

# We configure sudo nano /opt/retropie/configs/all/autostart.sh
#/opt/retropie/supplementary/runcommand/runcommand.sh 0 _SYS_ snes '/home/pi/RetroPie/roms/snes/test.smc'
# sudo nano /opt/retropie/configs/all/runcommand.cfg
# Then set disable_menu = "1"


#time.sleep(15)
#toggle_screen("0")
#time.sleep(1)
#toggle_screen("1")


#/opt/retropie/configs/all $ sudo nano runcommand.cfg