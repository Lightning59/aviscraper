import pyautogui
import time


def saveimage(imagenamepath: str) -> None:

    '''
    Saves the image with the filename and path passed. Requires that user window is active in a full screen avweek
    browser with image in the center of the screen and no other user input (like touching the mouse) will occur during
    during execution
    :param imagenamepath: Valid absolute file location for image including the filename to be saved.
    :return: Returns nothing mearly performs action - will result in a saved jpg in appropriate folder.
    '''

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
