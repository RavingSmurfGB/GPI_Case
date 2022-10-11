from inputs import get_gamepad



def write_file(data, mode):

        with open("button_output.txt", mode) as file:
                file.write(str(data) +  "\n") # the data is writen to file


write_file("", "w")

keys = {# This dictionary provides translation for 
    "UP" : ['ABS_Y', -32768],
    "LEFT" : ['ABS_X', -32768],
    "RIGHT" : ['ABS_X', 32767],
    "DOWN" : ['ABS_Y', 32767],
    "X" : ['BTN_NORTH', 1],
    "Y" : ['BTN_WEST', 1],
    "B" : ['BTN_SOUTH', 1],
    "A" : ['BTN_EAST', 1],
    "SELECT" : ['BTN_SELECT', 1],
    "START" : ['BTN_START', 1],
    "LTRIGGER" : ['BTN_TL', 1],
    "RTRIGGER" : ['BTN_TR', 1]
}



while True:
    events = get_gamepad()
    for event in events: #
        if event.code != "SYN_REPORT":
            if event.state != 0 and event.state != -1:
                for translation, raw_button, test in keys:
                    if raw_button == [event.code, event.state]:
                        print(translation)
                event_list = [event.code, event.state]

                print(event_list)
                write_file(event_list, "a")






#### D PAD
# UP - ['ABS_Y', -32768]
# LEFT - ['ABS_X', -32768]
# RIGHT - ['ABS_X', 32767]
# DOWN - ['ABS_Y', 32767]


#### Button PAD
# X - ['BTN_NORTH', 1]
# Y - ['BTN_WEST', 1]
# B - ['BTN_SOUTH', 1]
# A - ['BTN_EAST', 1]

# SELECT - ['BTN_SELECT', 1]
# START - ['BTN_START', 1]

# LEFT TRIGGER - ['BTN_TL', 1]
# RIGHT TRIGGER - ['BTN_TR', 1]