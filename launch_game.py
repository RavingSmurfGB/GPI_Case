
import subprocess, time
from datetime import datetime




def toggle_screen(toggle):
    subprocess.call(["vcgencmd", "display_power", toggle])

time.sleep(2)

subprocess.call(["/opt/retropie/supplementary/runcommand/runcommand.sh" ,"_SYS_", "snes", "'/home/pi/RetroPie/roms/snes/test.smc'"])
#

time.sleep(15)
toggle_screen("0")
time.sleep(1)
toggle_screen("1")
