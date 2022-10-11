from inputs import get_gamepad



def write_file(data, mode):

        with open("button_output.txt", mode) as file:
                file.write(str(data) +  "\n") # the data is writen to file


write_file("", "w")

while True:
    events = get_gamepad()
    for event in events: #
        if event.code == "SYN_REPORT":
            #if event.state != 0 or event.state != -1:
            event_list = [event.code, event.state]

            print(event_list)
            write_file(event_list, "a")

# UP - ['ABS_Y', -32768]
# LEFT - ['ABS_X', -32768]
# RIGHT - ['ABS_X', 32767]
# DOWN - ['ABS_Y', 32767]

