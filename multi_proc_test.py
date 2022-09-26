import multiprocessing, time
from pynput.keyboard import Listener as KeyboardListener

def hi_loop():
    while True:
        print("hi")
        time.sleep(1)

end_key = "/"

def keyboard_release(key):
    global gameplanArray
    # This function monitors for key presses, if it matches the end_key, it will write the gameplanArray to the file and close the program

    key = key.char

    if key == end_key:
        print("The recorder will now end, saving to file...")
        proc.terminate()  # sends a SIGTERM




if __name__ == '__main__':
    multiprocessing.freeze_support()#Required for script to run

    keyboard_listener= KeyboardListener(on_press=keyboard_release)



    


    proc = multiprocessing.Process(target=hi_loop, args=())
    proc.start()
    
    # Start the threads and join them so the script doesn't end earlyd
    keyboard_listener.start()

    # Terminate the process
    #time.sleep(5)
    