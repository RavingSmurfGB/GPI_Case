from inputs import get_gamepad



def write_file(data, mode):

        with open("button_output.txt", mode) as file:
                file.write(str(data)) # the data is writen to file

write_file("", "w")

while True:
    events = get_gamepad()
    for event in events: #
        event_list = [event.ev_type, event.code, event.state]
        print(event_list)
        write_file(event_list, "a")
