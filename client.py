from inputs import get_gamepad
import os, time


def file_handle(path, *data): 
    # This function handles reading and writing of files
    #   An example of reading could be:
    #       print(file_handle("/home/pi/GPI_Case/save_state.txt"))
    #   An example of writing could be:
    #       file_handle("/home/pi/GPI_Case/save_state.txt", "lock_boot")

    if len(data) == 0: # This checks if the tuple data is empty
        mode = "r" 
    else:
        mode = "w"
   

    with open(path, mode) as file:
        if len(data) == 1:
            file.write(data[0])
        else:
            return file.read()


de_path = "GPI_Case/save_state.txt"

file_handle(de_path)


#Get Save State 
state = file_handle("/home/pi/GPI_Case/save_state.txt")

if state == "normal_boot":
    ' launch emulation station shell script and hang'
    
    os.system("/home/pi/GPI_Case/launch_emulationstation.sh")
    file_handle("/home/pi/GPI_Case/save_state.txt", "lock_boot")
    # We also need to change the controls for hotkey here as it will only impact next boot
    while True:
        time.sleep(1)



elif state == "lock_boot":
    os.system("/home/pi/GPI_Case/launch_game.sh")
    'launch shell script with the following and proceed'


while True: # Await code input
    key_combo = [] # Up, Up, Down, Down, Left, Right, Left, Right, O, X.
    event_list = []
    events = get_gamepad()
    for event in events:


        if len(event_list) > 9:
            event_list.pop(0)


        event_list.append(event) #Change the event to be something proper....
        print(event.ev_type, event.code, event.state)

        if key_combo in event_list:
            #change the boot stuffs...

#inside cat /opt/retropie/configs/all/autostart.sh

#while pgrep omxplayer >/dev/null; do sleep 1; done
#/home/pi/scripts/themerandom.sh
#bash /opt/retropie/configs/imp/boot.sh > /dev/null 2>&1 & #auto
#emulationstation #auto