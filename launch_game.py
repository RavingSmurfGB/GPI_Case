
import subprocess, time
from datetime import datetime




def toggle_screen(toggle):
    subprocess.call(["vcgencmd", "display_power", toggle])

#time.sleep(20)

subprocess.call(["/opt/retropie/supplementary/runcommand/runcommand.sh","0" ,"_SYS_", "snes", "'test.smc'"])
#/opt/retropie/supplementary/runcommand/runcommand.sh 0 _SYS_ snes '/home/pi/RetroPie/roms/snes/The Legend of Zelda - A Link to the Past (U) [!].smc'

time.sleep(15)
toggle_screen("0")
time.sleep(1)
toggle_screen("1")
