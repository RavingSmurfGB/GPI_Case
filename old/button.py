from inputs import get_gamepad




def write_file(data):
    try:
        with open("button_output.txt", "w") as file:
                file.write(data) # the data is writen to file
    except FileNotFoundError:
        with open("button_output.txt", "x") as file:
            file.write()


events = get_gamepad()
for event in events: #

    print(event.ev_type, event.code, event.state)
    write_file(event.ev_type, event.code, event.state)
