# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#load the page at the given URL
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://archive.aviationweek.com/')