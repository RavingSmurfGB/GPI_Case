from inputs import get_gamepad



def write_file(data, mode):

        with open("button_output.txt", mode) as file:
                file.write(str(data) +  "\n") # the data is writen to file


write_file("", "w")

while True:
    events = get_gamepad()
    for event in events: #
        if event.ev_type == "Absolute":
            event_list = [event.ev_type, event.code, event.state]

            print(event_list)
            write_file(event_list, "a")
