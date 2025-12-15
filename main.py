import sys
from math import floor, ceil

from dotenv import load_dotenv, dotenv_values
from datetime import datetime, timedelta
from time import sleep
import os
import subprocess
from pynput.mouse import Button, Controller
import pyautogui
from pyautogui import press, typewrite, keyDown, hotkey, keyUp

# screenWidth, screenHeight = pyautogui.size()
# currentMouseX, currentMouseY = pyautogui.position()

load_dotenv()
config = dotenv_values(".env")

hours_to_keep_alive = int(config["NO_OF_HRS_KEEPALIVE"])
sleep_sec = int(config["SLEEP_SEC"])
max_loop_count = int(config["LOOP_COUNT"])
mouse_ctrl = Controller()
logoff_time_str = config["LOGOFF_TIME"]


def endless(max_cnt=1000):
    time_now = datetime.now()
    # time_later = time_now + datetime.timedelta(hours=2)
    time_later = time_now + timedelta(hours=hours_to_keep_alive)
    print('--------------------------------------------------')
    while max_cnt > 0:
        mouse_ctrl.move(1, -1)
        mouse_ctrl.click(Button.left, 1)
        max_cnt -= 1
        time_now = datetime.now()
        time_now_str = time_now.strftime("%H:%M:%S")

        print("time_now:\t" + time_now.strftime("%m/%d/%Y, %I:%M:%S %p"))
        print("time_end:\t" + time_later.strftime("%m/%d/%Y, %I:%M:%S %p"))
        print("time_left:\t" + str(ceil((time_later - time_now).total_seconds() / (60 * 60))) + "hrs")
        print("logoff_time:\t" + logoff_time_str)

        if time_now_str > logoff_time_str:
            print('logging off...')
            print('exiting as time is up...')
            goto_myprofile()
            change_to_offline()
            sys.exit()

        if time_now >= time_later:
            print('exiting as time is up...')
            goto_myprofile()
            change_to_green()
            sys.exit()
            
        print('sleeping for {} seconds, loop count left {}({})'.format(sleep_sec, max_cnt, max_loop_count))
        print('--------------------------------------------------\n')
        sleep(sleep_sec)
    goto_myprofile()
    change_to_green()
    sys.exit()

def open_teams():
    subprocess.call(['open', '/Applications/Microsoft Teams.app'])
    sleep(10)


def goto_mychat():
    sleep(3)
    pyautogui.moveTo(750, 49)
    sleep(3)
    pyautogui.click()
    sleep(3)
    pyautogui.keyDown('command')
    pyautogui.press('a')
    sleep(3)
    pyautogui.keyUp('command')
    sleep(3)
    pyautogui.press('backspace')
    sleep(3)
    pyautogui.write("tharakesh")
    sleep(3)
    pyautogui.moveTo(800, 145)
    sleep(3)
    pyautogui.click()
    sleep(3)
    pyautogui.press('escape')
    sleep(3)
    pyautogui.moveTo(870, 975)
    sleep(3)


def goto_myprofile():
    sleep(3)
    pyautogui.moveTo(1885, 50)
    sleep(3)
    pyautogui.click()
    sleep(3)
    pyautogui.moveTo(1750, 210)
    sleep(3)
    pyautogui.click()
    sleep(3)


def change_to_red():
    sleep(3)
    pyautogui.moveTo(1725, 280)
    pyautogui.click()
    sleep(3)
    pyautogui.press('escape')

def change_to_green():
    sleep(3)
    pyautogui.moveTo(1750, 242)
    pyautogui.click()
    sleep(3)
    pyautogui.press('escape')

def change_to_offline():
    sleep(3)
    pyautogui.moveTo(1750, 415)
    pyautogui.click()
    sleep(3)
    pyautogui.press('escape')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    open_teams()
    goto_myprofile()
    #change_to_offline()
    change_to_red()
    goto_mychat()
    endless(max_loop_count)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
