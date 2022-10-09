import time, os

with open("save_state.txt") as file: # Use file to refer to the file object

    data = file.read()

    print(data)

    if data == "normal_boot":
        ' launch emulation station shell script and hang'
        os.system("./launch_game.sh")
        while True:
            time.sleep(1)
        pass


    elif data == "lock_boot":
        os.system("./launch_emulationstation.sh")
        'launch shell script with the following and proceed'
        # Also change controlls - but controls only reload with reboot....
        #/opt/retropie/supplementary/runcommand/runcommand.sh 0 _SYS_ snes '/home/pi/RetroPie/roms/snes/The Legend of Zelda - A Link to the Past (U) [!].smc'
        pass