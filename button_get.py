from pynput.keyboard import Listener as KeyboardListener




def keyboard_release(key):
    global gameplanArray
    # This function monitors for key presses, if it matches the end_key, it will terminate the multiproc proc 

    key = key.char

    print(key)

keyboard_listener= KeyboardListener(on_press=keyboard_release)
keyboard_listener.start()
keyboard_listener.join()

