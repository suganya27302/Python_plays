import pyautogui
import time
while True:
    time.sleep(2)
    pyautogui.typewrite("hi")
    pyautogui.press('enter')


    # the cursor should be present where the message should be sent