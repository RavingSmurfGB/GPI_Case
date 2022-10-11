from inputs import get_gamepad




def write_file(data):
    with open("button_output.txt", "w") as file:
            file.write(data) # the data is writen to file


events = get_gamepad()
for event in events: #

    print(event.ev_type, event.code, event.state)
    write_file(event.ev_type, event.code, event.state)
