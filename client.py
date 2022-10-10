from inputs import get_gamepad
import os, time




#ISSUES
#
# Turning the system off from the lock_boot state will launch into emulation station or terminal
#   Find a way to detect the button turn off and use that instead of the hang to fully shutdown...
#       The system uses a safe shutdown script which may be usefull in figuring this out
#       https://github.com/RetroFlag/retroflag-picase

def file_handle(path, *data): 
    # This function handles reading and writing of files
    #   An example of reading could be:
    #       print(file_handle("/home/pi/GPI_Case/save_state.txt"))
    #   An example of writing could be:
    #       file_handle("/home/pi/GPI_Case/save_state.txt", "lock_boot")

    if len(data) == 0: # This checks if the tuple data is empty
        mode = "r" #If so it set's mode to be "r" which open's the file later on in read mode
    else:
        mode = "w" # Set's mode to be in write mode
   

    with open(path, mode) as file:
        if len(data) == 1: # If there is data in the variable data, 
            file.write(data[0]) # the data is writen to file
        else:
            return file.read() #if there was no data, we will simply read the file and return it for later use


#Get Save State 
state = file_handle("/home/pi/GPI_Case/save_state.txt") # Here we get what is in save_state.txt


if state == "normal_boot":
    # If save_state.txt returns "normal_boot" then we launch emulation station, change save_state.txt to lock_boot for the next launch of the system
    # Also we need to change the control's for the hotkey as explained here : https://retropie.org.uk/docs/RetroArch-Configuration/
    # Once this is done, we hang the code so that emulation station does not exit
    
    os.system("/home/pi/GPI_Case/launch_emulationstation.sh")
    file_handle("/home/pi/GPI_Case/save_state.txt", "lock_boot")
    # We also need to change the controls for hotkey here as it will only impact next boot !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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