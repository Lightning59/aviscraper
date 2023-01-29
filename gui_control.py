import pyautogui
import time


def saveimage(imagenamepath: str) -> None:
    time.sleep(1)
    screen_width, screen_height = pyautogui.size()

    pyautogui.moveTo(screen_width / 2, screen_height / 2)
    time.sleep(.2)
    pyautogui.rightClick()
    time.sleep(.2)
    pyautogui.moveTo(screen_width / 2 + 50, screen_height / 2 + 50)
    time.sleep(.2)
    pyautogui.click()
    time.sleep(.2)

    pyautogui.typewrite(imagenamepath)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(.2)
    pyautogui.press("enter")
    time.sleep(.5)
