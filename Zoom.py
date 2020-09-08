import keyboard
import time
import subprocess
import pandas as pd
from datetime import datetime
import pyautogui


def automate():
    print('Automation Started')
    # reading the meeting details from csv file
    df = pd.read_csv('meetingschedule.csv')
    df_new = pd.DataFrame()

    # reading zoom path details
    pt = open('path.txt', 'r+')
    pth = pt.readline()
    pth = pth.replace('/', '\\\\')

    while(True):
        # convert current time system to text
        timestr = datetime.now().strftime("%H:%M")

        # Check if the current time is mentioned in the Dataframe
        if timestr in df.Time.values:
            df_new = df[df['Time'].astype(str).str.contains(timestr)]

            # Open the Zoom app with the path provided
            subprocess.Popen(pth)
            time.sleep(5)
            # Locate the position of the join button on the screen
            position = pyautogui.locateOnScreen("buttons\\join_button_1.png")
            print(position)
            # Move the cursor to the position of the button
            pyautogui.moveTo(position)
            # Perform click operation
            pyautogui.click()
            # Waitng for above process to complete
            time.sleep(5)

            # Write the meeting ID from the dataframe onto the Zoom App
            keyboard.write(str(df_new.iloc[0, 1]))
            time.sleep(5)

            # For tapping the Turn off audio option on Zoom app
            position = pyautogui.locateOnScreen("buttons\\capture.png")
            pyautogui.moveTo(position)
            pyautogui.click()
            time.sleep(5)

            # For tapping the Turn off video option on Zoom app
            position = pyautogui.locateOnScreen("buttons\\capture.png")
            pyautogui.moveTo(position)
            pyautogui.click()
            time.sleep(5)

            # For tapping on the Join button
            position = pyautogui.locateOnScreen("buttons\\join_button_2.png")
            pyautogui.moveTo(position)
            pyautogui.click()
            time.sleep(15)

            # Reads the Meeting Passcode from the dataframe and enters into the zoom app
            keyboard.write(str(df_new.iloc[0, 2]))
            time.sleep(5)

            # For finally joining the meeting
            position = pyautogui.locateOnScreen("buttons\\join_meeting.png")
            pyautogui.moveTo(position)
            pyautogui.click()

            # Wait for two minute before the next iteration starts
            time.sleep(120)
