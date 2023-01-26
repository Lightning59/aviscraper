# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# load the page at the given URL
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

while True:
    UserInput = input("Issue date YYYMMDD")
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

browser = webdriver.Firefox()
browser.get('http://archive.aviationweek.com/')

time.sleep(2)

search = browser.find_element(By.XPATH, "//a[contains(text(),'Browse Issues')]")
search.click()
