from inputs import get_gamepad




def write_file(data):

        with open("button_output.txt", "w") as file:
                file.write(str(data)) # the data is writen to file

        #with open("button_output.txt", "x") as file:
         #   file.write()


events = get_gamepad()
for event in events: #
    event_list = [event.ev_type, event.code, event.state]
    print(event_list)
    write_file(event_list)
