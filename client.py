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
            #have someway to detect key combo
        print(event.ev_type, event.code, event.state)