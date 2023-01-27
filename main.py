# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# load the page at the given URL
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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

while True:
    usrInput=input("logged in and ready to browse issues?")
    if usrInput=="y" or "Y":
        break


time.sleep(standardPause)

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