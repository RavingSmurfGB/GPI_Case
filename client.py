from inputs import get_gamepad



#Get Save State 
with open("save_state.txt") as file: # Use file to refer to the file object

   data = file.read()

   'if data = normtal_boot'
    # Launch normal boot
    'elif data = lock_boot
    #Launch game and change hotkey in /opt/retropie/configs/all/retroarch/autoconfig To ensure user cannot exit out of game




while True: # Await code input
    events = get_gamepad()
    for event in events:
        #if event equals code
            #create list and append latest events to it
        print(event.ev_type, event.code, event.state)


#1 Use threading to only capture gamepad events 

inside cat /opt/retropie/configs/all/autostart.sh

while pgrep omxplayer >/dev/null; do sleep 1; done
#/home/pi/scripts/themerandom.sh
bash /opt/retropie/configs/imp/boot.sh > /dev/null 2>&1 & #auto
emulationstation #auto


##### We ADD THIS line and remove emulation station to boot into a game
/opt/retropie/supplementary/runcommand/runcommand.sh 0 _SYS_ snes '/home/pi/RetroPie/roms/snes/The Legend of Zelda - A Link to the Past (U) [!].smc'