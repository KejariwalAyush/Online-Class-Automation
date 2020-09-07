import keyboard
import time
import subprocess
import pandas as pd
from datetime import datetime
import pyautogui

# reading the meeting details
df = pd.read_csv('meetingschedule.csv')
df_new = pd.DataFrame()

while(True):
    # Check the current system time
    timestr = datetime.now().strftime("%H:%M")

    # df_new = df[df['Time'].astype(str).str.contains("19:50")]
    # print(df_new.iloc[0, 1])
    # break

    # Check if the current time is mentioned in the Dataframe
    if timestr in df.Time.values:
        df_new = df[df['Time'].astype(str).str.contains(timestr)]

        # Open the Zoom app
        subprocess.Popen(
            "C:\\Users\\Kejariwal\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
        time.sleep(5)
        # Locate the position of the join button on the screen
        position = pyautogui.locateOnScreen("join_button_1.png")
        print(position)
        # Move the cursor to the position of the button
        pyautogui.moveTo(position)
        # Perform click operation
        pyautogui.click()
        time.sleep(5)

        # Write the meeting ID from the dataframe onto the Zoom App
        keyboard.write(str(df_new.iloc[0, 1]))
        time.sleep(5)

        # For tapping the Turn off video option on Zoom app
        # position = pyautogui.locateOnScreen("turn_off_vid_button_1.png")
        position = pyautogui.locateOnScreen("capture.png")
        pyautogui.moveTo(position)
        pyautogui.click()
        time.sleep(2)

        # For tapping the Turn off audio option on Zoom app
        position = pyautogui.locateOnScreen("capture.png")
        pyautogui.moveTo(position)
        pyautogui.click()
        time.sleep(5)

        # For tapping on the Join button
        position = pyautogui.locateOnScreen("join_button_2.png")
        pyautogui.moveTo(position)
        pyautogui.click()
        time.sleep(15)

        # Reads the Meeting Passcode from the dataframe and enters into the zoom app
        keyboard.write(str(df_new.iloc[0, 2]))
        time.sleep(5)

        # For finally joining the meeting
        position = pyautogui.locateOnScreen("join_meeting.png")
        pyautogui.moveTo(position)
        pyautogui.click()

        # Wait for one minute before the next iteration starts
        time.sleep(60)
