# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# load the page at the given URL
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import gui_control
from pdfgen import *
import os


def islastpage(browser_obj: webdriver.Firefox) -> bool:
    """
    returns True when on pag max/max returns false for all max-n/max
    :param browser_obj: a browser object in an avweek session with actual article view open
    :return bool: True=on last page - False=not on last page
    """
    index_element = browser_obj.find_element(By.CLASS_NAME, "bndvwr__ctr_index")
    text = index_element.text
    text = text.replace(" ", "")
    current, last = text.split("/")
    return current == last


def returncurrentpage(browser_obj: webdriver.Firefox) -> str:
    """
    Returns current page number
    :param browser_obj: a browser object in an avweek session with actual article view open
    :return string: string (almost ceratinly intable) of current page number
    """
    index_element = browser_obj.find_element(By.CLASS_NAME, "bndvwr__ctr_index")
    text = index_element.text
    text = text.replace(" ", "")
    current, last = text.split("/")
    return current


# open and load username and password from conf file
with open("pass.conf", 'r') as passfile:
    username = passfile.readline()[0:-1]
    password = passfile.readline()
passfile.close()

# get primary monitor size and set up a standard 2-second pause and month dict for month lookups where required.
standardPause = 3  # seconds for sleep
monthDict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
             9: "September", 10: "October", 11: "November", 12: "December"}
jpegtempfoldername="jpegtemp"

# get a valid issue date from the user (does not validate it's a real day an issue exists for)
while True:
    UserInput = input("Issue date YYYMMDD:  ")
    try:
        assert len(UserInput) == 8
        year = int(UserInput[0:4])
        month = int(UserInput[4:6])
        day = int(UserInput[6:])
        assert 0 < month <= 12
        assert 0 < day <= 31
        break
    except AssertionError:
        print(" Try again YYYMMDD MM=01-12, DD=01-31 ")
    except ValueError:
        print("Try again enter only 0-9: YYMMDD")

try:
    os.mkdir(jpegtempfoldername)
except FileExistsError:
    filelist=os.listdir(jpegtempfoldername)
    for file in filelist:
        os.remove(os.path.join(jpegtempfoldername,file))
    pass

cwd=os.getcwd()


fulljpegtempdir=cwd+"\\"+jpegtempfoldername

# get decade text to select decade menu and month text with month name for individual magazine selection
decade = (year // 10) * 10
decadeText = str(decade) + 's'
monthDayText = monthDict[month] + " " + str(day)

# Open web page and pause and pause for load
browser = webdriver.Firefox()
browser.get('http://archive.aviationweek.com/')
# actions = ActionChains(browser)
time.sleep(standardPause)
browser.fullscreen_window()

while True:
    usrInput = input("logged in and ready to browse issues?")
    if usrInput == "y":
        break
    elif usrInput == "n":
        search = browser.find_element(By.XPATH, "//a[contains(text(),'Login')]")
        search.click()

        time.sleep(standardPause)

        search = browser.find_element(By.ID, "email")
        search.send_keys(username)
        time.sleep(random.random())
        search = browser.find_element(By.ID, "password")
        search.send_keys(password)
        time.sleep(random.random())
        search = browser.find_element(By.ID, "btn-login")
        search.click()
        break

time.sleep(standardPause * 10)

search = browser.find_element(By.XPATH, "//a[contains(text(),'Browse Issues')]")
search.click()

time.sleep(standardPause)

cssDecade = ".the" + decadeText

search = browser.find_element(By.CSS_SELECTOR, cssDecade)
time.sleep(standardPause)
search.click()

time.sleep(standardPause)
search = browser.find_element(By.LINK_TEXT, str(year))
time.sleep(standardPause)
search.click()
time.sleep(standardPause)

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(standardPause * 2)
search = browser.find_element(By.XPATH, "//img[@title='Publication | " + monthDayText + " " + str(year) + "']")
time.sleep(standardPause)
search.click()

time.sleep(standardPause)
search = browser.find_element(By.CSS_SELECTOR, ".red > .visible")
time.sleep(standardPause)
search.click()
time.sleep(standardPause + random.random())

onlastpage = False
while not onlastpage:
    time.sleep(standardPause+random.random())
    pagenumber=returncurrentpage(browser)
    pagenumbertext=fulljpegtempdir+"\\"+pagenumber+".jpg"
    gui_control.saveimage(pagenumbertext)
    time.sleep(standardPause + random.random())
    onlastpage = islastpage(browser)
    search = browser.find_element(By.CLASS_NAME, "bndvwr__button--arrow--right")
    search.click()


while True:
    usrInput = input("logged in and ready to browse issues?")
    if usrInput == "y":
        break

writepdffromjpegs(UserInput,jpegtempfoldername)
