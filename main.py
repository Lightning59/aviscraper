# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# load the page at the given URL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time
import random


def islastpage(browser:webdriver.Firefox) -> bool:
    search=browser.find_element(By.CLASS_NAME,"bndvwr__ctr_index")
    text=search.text
    text=text.replace(" ","")
    current,last=text.split("/")
    return current==last




with open("pass.conf",'r') as passfile:
    username=passfile.readline()[0:-1]
    password=passfile.readline()
passfile.close()



screenWidth, screenHeight = pyautogui.size()
standardPause = 2  # seconds for sleep
monthDict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
             9: "September", 10: "October", 11: "November", 12: "December"}

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

decade = (year // 10) * 10
decadeText = str(decade) + 's'
monthDayText = monthDict[month]+" "+str(day)

browser = webdriver.Firefox()
browser.get('http://archive.aviationweek.com/')
actions = ActionChains(browser)
time.sleep(standardPause)

while True:
    usrInput=input("logged in and ready to browse issues?")
    if usrInput=="y":
        break
    elif usrInput=="n":
        search=browser.find_element(By.XPATH,"//a[contains(text(),'Login')]")
        search.click()

        time.sleep(standardPause)

        search= browser.find_element(By.ID,"email")
        search.send_keys(username)
        time.sleep(random.random())
        search = browser.find_element(By.ID, "password")
        search.send_keys(password)
        time.sleep(random.random())
        search = browser.find_element(By.ID,"btn-login")
        search.click()
        break


time.sleep(standardPause*10)

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
time.sleep(standardPause*2)
search=browser.find_element(By.XPATH,"//img[@title='Publication | "+monthDayText+" "+str(year)+"']")
time.sleep(standardPause)
search.click()


time.sleep(standardPause)
search = browser.find_element(By.CSS_SELECTOR, ".red > .visible")
time.sleep(standardPause)
search.click()
time.sleep(standardPause+random.random())

onlastpage=False
while not onlastpage:
    ## get page number (for pyautoGUI)
    ### pyautoGUI save page
    time.sleep(standardPause+random.random())
    onlastpage = islastpage(browser)
    search = browser.find_element(By.CLASS_NAME,"bndvwr__button--arrow--right")
    search.click()


