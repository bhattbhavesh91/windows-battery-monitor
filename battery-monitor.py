import os
import psutil
import time
import winsound

def generate_sound(inp):
    if inp == 1:
        frequency = 2500
        duration = 5000
        winsound.Beep(frequency, duration)
    elif inp == 2:
        beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
        beep(3)

def check_battery_percentage(inp_sound_value):
    battery = psutil.sensors_battery()
    bat_pct = battery.percent
    bat_plug = battery.power_plugged
    if (bat_pct >= 95) and (bat_plug == True):
        print("Stop Charging")
        generate_sound(inp_sound_value)
    else:
        print("Continue Charging")


def main():
    while True:
        check_battery_percentage(1)
        time.sleep(30)

if __name__ == "__main__":
    main()
