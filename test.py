
from genericpath import exists


def file_handle(path, *data):
    if len(data) == 0: # This checks if the tuple data is empty
        mode = "r"
    else:
        mode = "w"
   

    with open(path, mode) as file:
        if len(data) == 1:
            file.write(data[0])
        else:
            #print(file.read())
            return file.read()


de_path = "GPI_Case/save_state.txt"


print(file_handle(de_path))


#file_handle(de_path, "HEY")

#file_handle(de_path)

'''
with open("GPI_Case/save_state.txt") as file: # Use file to refer to the file object

    data = file.read()

    print(data)

with open("GPI_Case/save_state.txt", "w") as file: # Use file to refer to the file object
    file.write("hey")

    

with open("GPI_Case/save_state.txt") as file: # Use file to refer to the file object

    data = file.read()

    print(data)

'''