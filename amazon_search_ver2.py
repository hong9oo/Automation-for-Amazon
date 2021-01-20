from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib.request
import csv
import pyautogui

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from bs4 import BeautifulSoup
import requests
from itertools import chain
import operator



button = pyautogui.confirm('Scrape Amazon?', 'Amazon Search Rank ver2 - created by JH')
if button == 'OK':
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=chrome_options)


    ###################@@@@@@@@@@@@@@@@ DE @@@@@@@@@@@@@@@@###################
    ###################@@@@@@@@@@@@@@@@ DE @@@@@@@@@@@@@@@@###################
    ###################@@@@@@@@@@@@@@@@ DE @@@@@@@@@@@@@@@@###################
    ###################@@@@@@@@@@@@@@@@ DE @@@@@@@@@@@@@@@@###################
    ###################@@@@@@@@@@@@@@@@ DE @@@@@@@@@@@@@@@@###################

    def search_de():
        de_list = []
        url = 'https://www.amazon.de'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods pro hülle')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id('sp-cc-accept').click()
        time.sleep(2)

        for x in range(1, 21):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    de_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    de_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    de_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    de_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    de_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    de_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    de_list.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        de_list.insert(0, "*** airpods pro hülle ***")
        return sorted(de_list)

    def search_de_two():
        de_list_two = []
        url = 'https://www.amazon.de'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods pro case')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 21):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    de_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    de_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    de_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    de_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    de_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    de_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    de_list_two.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        de_list_two.insert(0, "*** airpods pro case ***")
        return sorted(de_list_two)


    def search_de_three():
        de_list_three = []
        url = 'https://www.amazon.de'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('apple airpods pro hülle')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 21):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    de_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    de_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    de_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    de_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    de_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    de_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    de_list_three.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        de_list_three.insert(0, "*** apple airpods pro hülle ***")
        return sorted(de_list_three)

    ################################ Airpods 1 & 2 ################################

    def search_de_no_pro():
        de_list_four = []
        url = 'https://www.amazon.de'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods case')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 21):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text

                if item.startswith("Spigen") and "Pro" not in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    de_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    de_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    de_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    de_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    de_list_four.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        de_list_four.insert(0, "*** airpods case ***")
        return sorted(de_list_four)


    def search_de_no_pro_two():
        de_list_five = []
        url = 'https://www.amazon.de'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods 2 hülle')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 21):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" not in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    de_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    de_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    de_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    de_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    de_list_five.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        de_list_five.insert(0, "*** airpods 2 hülle ***")
        return sorted(de_list_five)


    def search_de_no_pro_three():
        de_list_six = []
        url = 'https://www.amazon.de'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('apple airpods hülle')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 21):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" not in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    de_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    de_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    de_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    de_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    de_list_six.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        de_list_six.insert(0, "*** apple airpods hülle ***")
        return sorted(de_list_six)


    def search_de_galaxy_one():
        de_list_seven = []
        url = 'https://www.amazon.de'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('galaxy buds live hülle')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 6):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    de_list_seven.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    de_list_seven.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    de_list_seven.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    de_list_seven.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    de_list_seven.append(pgn)
            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        de_list_seven.insert(0, "*** galaxy buds live hülle ***")
        return sorted(de_list_seven)


    def search_de_galaxy_two():
        de_list_eight = []
        url = 'https://www.amazon.de'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('galaxy buds live case')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 6):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    de_list_eight.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    de_list_eight.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    de_list_eight.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    de_list_eight.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    de_list_eight.append(pgn)
            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        de_list_eight.insert(0, "*** galaxy buds live case ***")
        return sorted(de_list_eight)


    def search_de_galaxy_three():
        de_list_nine = []
        url = 'https://www.amazon.de'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('galaxy buds live zubehör')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 6):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    de_list_nine.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    de_list_nine.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    de_list_nine.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    de_list_nine.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    de_list_nine.append(pgn)
            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        de_list_nine.insert(0, "*** galaxy buds live zubehör ***")
        return sorted(de_list_nine)

    ###################@@@@@@@@@@@@@@@@ UK @@@@@@@@@@@@@@@@###################
    ###################@@@@@@@@@@@@@@@@ UK @@@@@@@@@@@@@@@@###################
    ###################@@@@@@@@@@@@@@@@ UK @@@@@@@@@@@@@@@@###################
    ###################@@@@@@@@@@@@@@@@ UK @@@@@@@@@@@@@@@@###################
    ###################@@@@@@@@@@@@@@@@ UK @@@@@@@@@@@@@@@@###################

    def search_uk():
        uk_list = []
        url = 'https://www.amazon.co.uk'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods pro case')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id('sp-cc-accept').click()
        time.sleep(2)

        for x in range(1, 17):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    uk_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    uk_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    uk_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    uk_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    uk_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    uk_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    uk_list.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        uk_list.insert(0, "*** airpods pro case ***")
        return sorted(uk_list)


    def search_uk_two():
        
        uk_list_two = []

        url = 'https://www.amazon.co.uk'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods pro case cover')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 17):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    uk_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    uk_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    uk_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    uk_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    uk_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    uk_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    uk_list_two.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        uk_list_two.insert(0, "*** airpods pro case cover ***")
        return sorted(uk_list_two)


    def search_uk_three():
        uk_list_three = []
        url = 'https://www.amazon.co.uk'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods pro cover')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 21):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    uk_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    uk_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    uk_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    uk_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    uk_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    uk_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    uk_list_three.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        uk_list_three.insert(0, "*** airpods pro cover ***")
        return sorted(uk_list_three)

    ################################ Airpods 1 & 2 ################################

    def search_uk_no_pro():
        uk_list_four = []
        url = 'https://www.amazon.co.uk'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods case')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 21):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" not in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    uk_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    uk_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    uk_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    uk_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    uk_list_four.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        uk_list_four.insert(0, "*** airpods case ***")
        return sorted(uk_list_four)


    def search_uk_no_pro_two():
        uk_list_five = []
        url = 'https://www.amazon.co.uk'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods case cover')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 21):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" not in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    uk_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    uk_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    uk_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    uk_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    uk_list_five.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        uk_list_five.insert(0, "*** airpods case cover ***")
        return sorted(uk_list_five)


    def search_uk_no_pro_three():
        uk_list_six = []
        url = 'https://www.amazon.co.uk'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('apple airpods case')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 21):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" not in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    uk_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    uk_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    uk_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    uk_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    uk_list_six.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        uk_list_six.insert(0, "*** apple airpods case ***")
        return sorted(uk_list_six)


    def search_uk_galaxy_one():
        uk_list_seven = []
        url = 'https://www.amazon.co.uk'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('galaxy buds live case')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 21):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    uk_list_seven.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    uk_list_seven.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    uk_list_seven.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    uk_list_seven.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    uk_list_seven.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        uk_list_seven.insert(0, "*** galaxy buds live case ***")
        return sorted(uk_list_seven)


    def search_uk_galaxy_two():
        uk_list_eight = []
        url = 'https://www.amazon.co.uk'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('galaxy buds live case cover')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 21):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    uk_list_eight.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    uk_list_eight.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    uk_list_eight.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    uk_list_eight.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    uk_list_eight.append(pgn)
            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        uk_list_eight.insert(0, "*** galaxy buds live case cover ***")
        return sorted(uk_list_eight)


    def search_uk_galaxy_three():
        uk_list_nine = []
        url = 'https://www.amazon.co.uk'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('galaxy buds live skin')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 14):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-medium a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    uk_list_nine.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    uk_list_nine.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    uk_list_nine.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    uk_list_nine.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    uk_list_nine.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        uk_list_nine.insert(0, "*** galaxy buds live skin ***")
        return sorted(uk_list_nine)

    ################################ FR ################################
    ################################ FR ################################
    ################################ FR ################################
    ################################ FR ################################

    def search_fr():
        fr_list = []
        url = 'https://www.amazon.fr'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('coque airpods pro')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id('sp-cc-accept').click()
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    fr_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    fr_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    fr_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    fr_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    fr_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    fr_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    fr_list.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        fr_list.insert(0, "*** coque airpods pro ***")
        return sorted(fr_list)


    def search_fr_two():
        fr_list_two = []
        url = 'https://www.amazon.fr'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods pro case')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    fr_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    fr_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    fr_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    fr_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    fr_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    fr_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    fr_list_two.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        fr_list_two.insert(0, "*** airpods pro case ***")
        return sorted(fr_list_two)


    def search_fr_three():
        fr_list_three = []
        url = 'https://www.amazon.fr'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('etui airpods pro')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    fr_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    fr_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    fr_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    fr_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    fr_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    fr_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    fr_list_three.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        fr_list_three.insert(0, "*** etui airpods pro ***")
        return sorted(fr_list_three)

    ################################ Airpods 1 & 2 ################################

    def search_fr_no_pro():
        fr_list_four = []
        url = 'https://www.amazon.fr'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('coque airpods')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" not in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    fr_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    fr_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    fr_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    fr_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    fr_list_four.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        fr_list_four.insert(0, "*** coque airpods ***")
        return sorted(fr_list_four)



    def search_fr_no_pro_two():
        fr_list_five = []
        url = 'https://www.amazon.fr'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('coque airpods 2')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" not in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    fr_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    fr_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    fr_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    fr_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    fr_list_five.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        fr_list_five.insert(0, "*** coque airpods 2 ***")
        return sorted(fr_list_five)


    def search_fr_no_pro_three():
        fr_list_six = []
        url = 'https://www.amazon.fr'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('etui airpods')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" not in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    fr_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    fr_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    fr_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    fr_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    fr_list_six.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        fr_list_six.insert(0, "*** etui airpods ***")
        return sorted(fr_list_six)


    def search_fr_galaxy_one():
        fr_list_seven = []
        url = 'https://www.amazon.fr'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('galaxy buds live case')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 6):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    fr_list_seven.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    fr_list_seven.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    fr_list_seven.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    fr_list_seven.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    fr_list_seven.append(pgn)
            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        fr_list_seven.insert(0, "*** galaxy buds live case ***")
        return sorted(fr_list_seven)


    def search_fr_galaxy_two():
        fr_list_eight = []
        url = 'https://www.amazon.fr'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('coque galaxy buds live')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    fr_list_eight.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    fr_list_eight.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    fr_list_eight.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    fr_list_eight.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    fr_list_eight.append(pgn)
            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        fr_list_eight.insert(0, "*** coque galaxy buds live ***")
        return sorted(fr_list_eight)


    def search_fr_galaxy_three():
        fr_list_nine = []
        url = 'https://www.amazon.fr'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('etui galaxy buds live')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    fr_list_nine.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    fr_list_nine.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    fr_list_nine.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    fr_list_nine.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    fr_list_nine.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        fr_list_nine.insert(0, "*** etui galaxy buds live ***")
        return sorted(fr_list_nine)

    #####################@@@@@@@@@@@@@@@@@@@ IT @@@@@@@@@@@@@@@@@@@#####################
    #####################@@@@@@@@@@@@@@@@@@@ IT @@@@@@@@@@@@@@@@@@@#####################
    #####################@@@@@@@@@@@@@@@@@@@ IT @@@@@@@@@@@@@@@@@@@#####################
    #####################@@@@@@@@@@@@@@@@@@@ IT @@@@@@@@@@@@@@@@@@@#####################
    #####################@@@@@@@@@@@@@@@@@@@ IT @@@@@@@@@@@@@@@@@@@#####################

    def search_it():
        it_list = []
        url = 'https://www.amazon.it'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('cover airpods pro')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id('sp-cc-accept').click()
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    it_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    it_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    it_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    it_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    it_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    it_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    it_list.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        it_list.insert(0, "*** cover airpods pro ***")
        return sorted(it_list)


    def search_it_two():
        it_list_two = []
        url = 'https://www.amazon.it'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('custodia airpods pro')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    it_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    it_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    it_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    it_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    it_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    it_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    it_list_two.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        it_list_two.insert(0, "*** custodia airpods pro ***")
        return sorted(it_list_two)


    def search_it_three():
        it_list_three = []
        url = 'https://www.amazon.it'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods pro cover')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    it_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    it_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    it_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    it_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    it_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    it_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    it_list_three.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        it_list_three.insert(0, "*** airpods pro cover ***")
        return sorted(it_list_three)

    ################################ Airpods 1 & 2 ################################

    def search_it_no_pro():
        it_list_four = []
        url = 'https://www.amazon.it'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('cover airpods')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "1 & 2" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    it_list_four.append(pgn)
                if item.startswith("Spigen") and "1 & 2" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    it_list_four.append(pgn)
                if item.startswith("Spigen") and "1 & 2" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    it_list_four.append(pgn)
                if item.startswith("Spigen") and "1 & 2" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    it_list_four.append(pgn)
                if item.startswith("Spigen") and "1 & 2" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    it_list_four.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        it_list_four.insert(0, "*** cover airpods ***")
        return sorted(it_list_four)


    def search_it_no_pro_two():
        it_list_five = []
        url = 'https://www.amazon.it'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('custodia airpods')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "1 & 2" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    it_list_five.append(pgn)
                if item.startswith("Spigen") and "1 & 2" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    it_list_five.append(pgn)
                if item.startswith("Spigen") and "1 & 2" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    it_list_five.append(pgn)
                if item.startswith("Spigen") and "1 & 2" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    it_list_five.append(pgn)
                if item.startswith("Spigen") and "1 & 2" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    it_list_five.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        it_list_five.insert(0, "*** custodia airpods ***")
        return sorted(it_list_five)


    def search_it_no_pro_three():
        it_list_six = []
        url = 'https://www.amazon.it'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods cover')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "1 & 2" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    it_list_six.append(pgn)
                if item.startswith("Spigen") and "1 & 2" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    it_list_six.append(pgn)
                if item.startswith("Spigen") and "1 & 2" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    it_list_six.append(pgn)
                if item.startswith("Spigen") and "1 & 2" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    it_list_six.append(pgn)
                if item.startswith("Spigen") and "1 & 2" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    it_list_six.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        it_list_six.insert(0, "*** airpods cover ***")
        return sorted(it_list_six)


    def search_it_galaxy_one():
        it_list_seven = []
        url = 'https://www.amazon.it'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('cover galaxy buds live')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    it_list_seven.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    it_list_seven.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    it_list_seven.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    it_list_seven.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    it_list_seven.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        it_list_seven.insert(0, "*** cover galaxy buds live ***")
        return sorted(it_list_seven)


    def search_it_galaxy_two():
        it_list_eight = []
        url = 'https://www.amazon.it'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('custodia galaxy buds live')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    it_list_eight.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    it_list_eight.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    it_list_eight.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    it_list_eight.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    it_list_eight.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        it_list_eight.insert(0, "*** custodia galaxy buds live ***")
        return sorted(it_list_eight)


    def search_it_galaxy_three():
        it_list_nine = []
        url = 'https://www.amazon.it'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('galaxy buds live cover')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    it_list_nine.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    it_list_nine.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    it_list_nine.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    it_list_nine.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    it_list_nine.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        it_list_nine.insert(0, "*** galaxy buds live cover ***")
        return sorted(it_list_nine)

    ###################@@@@@@@@@@@@@@@@ ES @@@@@@@@@@@@@@@@###################
    ###################@@@@@@@@@@@@@@@@ ES @@@@@@@@@@@@@@@@###################
    ###################@@@@@@@@@@@@@@@@ ES @@@@@@@@@@@@@@@@###################
    ###################@@@@@@@@@@@@@@@@ ES @@@@@@@@@@@@@@@@###################
    ###################@@@@@@@@@@@@@@@@ ES @@@@@@@@@@@@@@@@###################

    def search_es():
        es_list = []
        url = 'https://www.amazon.es'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('funda airpods pro')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id('sp-cc-accept').click()
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    es_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    es_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    es_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    es_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    es_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    es_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    es_list.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        es_list.insert(0, "*** funda airpods pro ***")
        return sorted(es_list)


    def search_es_two():
        es_list_two = []
        url = 'https://www.amazon.es'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods pro case')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    es_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    es_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    es_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    es_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    es_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    es_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    es_list_two.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        es_list_two.insert(0, "*** airpods pro case ***")
        return sorted(es_list_two)


    def search_es_three():
        es_list_three = []
        url = 'https://www.amazon.es'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods pro funda')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    es_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    es_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    es_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    es_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    es_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    es_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    es_list_three.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        es_list_three.insert(0, "*** airpods pro funda ***")
        return sorted(es_list_three)

    ################################ Airpods 1 & 2 ################################

    def search_es_no_pro():
        es_list_four = []
        url = 'https://www.amazon.es'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('funda airpods')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" not in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    es_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    es_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    es_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    es_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    es_list_four.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        es_list_four.insert(0, "*** funda airpods ***")
        return sorted(es_list_four)


    def search_es_no_pro_two():
        es_list_five = []
        url = 'https://www.amazon.es'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('fundas airpods')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" not in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    es_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    es_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    es_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    es_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    es_list_five.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        es_list_five.insert(0, "*** fundas airpods ***")
        return sorted(es_list_five)


    def search_es_no_pro_three():
        es_list_six = []
        url = 'https://www.amazon.es'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('funda airpods 2')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" not in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    es_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    es_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    es_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    es_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    es_list_six.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        es_list_six.insert(0, "*** funda airpods 2 ***")
        return sorted(es_list_six)


    def search_es_galaxy_one():
        es_list_seven = []
        url = 'https://www.amazon.es'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('funda galaxy buds live')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    es_list_seven.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    es_list_seven.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    es_list_seven.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    es_list_seven.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    es_list_seven.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        es_list_seven.insert(0, "*** funda galaxy buds live ***")
        return sorted(es_list_seven)


    def search_es_galaxy_two():
        es_list_eight = []
        url = 'https://www.amazon.es'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('funda buds live')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    es_list_eight.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    es_list_eight.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    es_list_eight.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    es_list_eight.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    es_list_eight.append(pgn)
            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        es_list_eight.insert(0, "*** funda buds live ***")
        return sorted(es_list_eight)


    def search_es_galaxy_three():
        es_list_nine = []
        url = 'https://www.amazon.es'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('galaxy buds live funda')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    es_list_nine.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    es_list_nine.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    es_list_nine.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    es_list_nine.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    es_list_nine.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        es_list_nine.insert(0, "*** galaxy buds live funda ***")
        return sorted(es_list_nine)

    ###################@@@@@@@@@@@@@@@@ NL @@@@@@@@@@@@@@@@###################
    ###################@@@@@@@@@@@@@@@@ NL @@@@@@@@@@@@@@@@###################
    ###################@@@@@@@@@@@@@@@@ NL @@@@@@@@@@@@@@@@###################
    ###################@@@@@@@@@@@@@@@@ NL @@@@@@@@@@@@@@@@###################
    ###################@@@@@@@@@@@@@@@@ NL @@@@@@@@@@@@@@@@###################

    def search_nl():
        nl_list = []
        url = 'https://www.amazon.nl'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods pro case')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id('sp-cc-accept').click()
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    nl_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    nl_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    nl_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    nl_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    nl_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    nl_list.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    nl_list.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        nl_list.insert(0, "*** airpods pro case ***")
        return sorted(nl_list)


    def search_nl_two():
        nl_list_two = []
        url = 'https://www.amazon.nl'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods pro hoesje')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    nl_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    nl_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    nl_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    nl_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    nl_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    nl_list_two.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    nl_list_two.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        nl_list_two.insert(0, "*** airpods pro hoesje ***")
        return sorted(nl_list_two)


    def search_nl_three():
        nl_list_three = []
        url = 'https://www.amazon.nl'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods pro accessoires')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    nl_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    nl_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    nl_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CS]"
                    pgn += item
                    nl_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    nl_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Slim" in item:
                    pgn = f"PAGE: [{x}]===[SA IP]"
                    pgn += item
                    nl_list_three.append(pgn)
                if item.startswith("Spigen") and "Pro" in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    nl_list_three.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        nl_list_three.insert(0, "*** airpods pro accessoires ***")
        return sorted(nl_list_three)

    ################################ Airpods 1 & 2 ################################

    def search_nl_no_pro():
        nl_list_four = []
        url = 'https://www.amazon.nl'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods case')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" not in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    nl_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    nl_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    nl_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    nl_list_four.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    nl_list_four.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        nl_list_four.insert(0, "*** airpods case ***")
        return sorted(nl_list_four)


    def search_nl_no_pro_two():
        nl_list_five = []
        url = 'https://www.amazon.nl'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods hoesje')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" not in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    nl_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    nl_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    nl_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    nl_list_five.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    nl_list_five.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        nl_list_five.insert(0, "*** airpods hoesje ***")
        return sorted(nl_list_five)


    def search_nl_no_pro_three():
        nl_list_six = []
        url = 'https://www.amazon.nl'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('airpods 2 case')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Pro" not in item and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    nl_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Tough" in item:
                    pgn = f"PAGE: [{x}]===[TA]"
                    pgn += item
                    nl_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    nl_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    nl_list_six.append(pgn)
                if item.startswith("Spigen") and "Pro" not in item and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    nl_list_six.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        nl_list_six.insert(0, "*** airpods 2 case ***")
        return sorted(nl_list_six)


    def search_nl_galaxy_one():
        nl_list_seven = []
        url = 'https://www.amazon.nl'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('galaxy buds live case')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    nl_list_seven.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    nl_list_seven.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    nl_list_seven.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    nl_list_seven.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    nl_list_seven.append(pgn)
            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        nl_list_seven.insert(0, "*** galaxy buds live case ***")
        return sorted(nl_list_seven)


    def search_nl_galaxy_two():
        nl_list_eight = []
        url = 'https://www.amazon.nl'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('galaxy buds live skin')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 5):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    nl_list_eight.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    nl_list_eight.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    nl_list_eight.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    nl_list_eight.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    nl_list_eight.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        nl_list_eight.insert(0, "*** galaxy buds live skin ***")
        return sorted(nl_list_eight)


    def search_nl_galaxy_three():
        nl_list_nine = []
        url = 'https://www.amazon.nl'
        driver.get(url)

        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys('galaxy buds live hoesje')
        time.sleep(2)
        driver.find_element_by_css_selector('.nav-input').send_keys(Keys.ENTER)
        time.sleep(2)

        for x in range(1, 8):
            titles = driver.find_elements_by_xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]')
            for t in titles:
                item = t.text
                if item.startswith("Spigen") and "Silicon" in item:
                    pgn = f"PAGE: [{x}]===[SF]"
                    pgn += item
                    nl_list_nine.append(pgn)
                if item.startswith("Spigen") and "Rugged" in item:
                    pgn = f"PAGE: [{x}]===[RA]"
                    pgn += item
                    nl_list_nine.append(pgn)
                if item.startswith("Spigen") and "Classic" in item:
                    pgn = f"PAGE: [{x}]===[CF]"
                    pgn += item
                    nl_list_nine.append(pgn)
                if item.startswith("Spigen") and "Urban" in item:
                    pgn = f"PAGE: [{x}]===[UF]"
                    pgn += item
                    nl_list_nine.append(pgn)
                if item.startswith("Spigen") and "Ultra" in item:
                    pgn = f"PAGE: [{x}]===[UH]"
                    pgn += item
                    nl_list_nine.append(pgn)

            driver.find_element_by_css_selector('.a-last').click()
            time.sleep(3)
        nl_list_nine.insert(0, "*** galaxy buds live hoesje ***")
        return sorted(nl_list_nine)


    ################################ DE Airpods Pro ################################
    de_df = pd.DataFrame(search_de(), columns = [':::DE:::'])
    de_df_two = pd.DataFrame(search_de_two(), columns = [':::DE:::'])
    de_df_three = pd.DataFrame(search_de_three(), columns = [':::DE:::'])

    ################################ DE Airpods 1 & 2 ##############################
    de_df_four = pd.DataFrame(search_de_no_pro(), columns = [':::DE:::'])
    de_df_five = pd.DataFrame(search_de_no_pro_two(), columns = [':::DE:::'])
    de_df_six = pd.DataFrame(search_de_no_pro_three(), columns = [':::DE:::'])

    ################################ DE Galaxy Buds ################################
    de_df_seven = pd.DataFrame(search_de_galaxy_one(), columns = [':::DE:::'])
    de_df_eight = pd.DataFrame(search_de_galaxy_two(), columns = [':::DE:::'])
    de_df_nine = pd.DataFrame(search_de_galaxy_three(), columns = [':::DE:::'])


    ################################ UK Airpods Pro ################################
    uk_df = pd.DataFrame(search_uk(), columns = [':::UK:::'])
    uk_df_two = pd.DataFrame(search_uk_two(), columns = [':::UK:::'])
    uk_df_three = pd.DataFrame(search_uk_three(), columns = [':::UK:::'])

    ################################ UK Airpods 1 & 2 ##############################
    uk_df_four = pd.DataFrame(search_uk_no_pro(), columns = [':::UK:::'])
    uk_df_five = pd.DataFrame(search_uk_no_pro_two(), columns = [':::UK:::'])
    uk_df_six = pd.DataFrame(search_uk_no_pro_three(), columns = [':::UK:::'])

    ################################ UK Galaxy Buds ################################
    uk_df_seven = pd.DataFrame(search_uk_galaxy_one(), columns = [':::UK:::'])
    uk_df_eight = pd.DataFrame(search_uk_galaxy_two(), columns = [':::UK:::'])
    uk_df_nine = pd.DataFrame(search_uk_galaxy_three(), columns = [':::UK:::'])


    ################################ FR Airpods Pro ################################
    df = pd.DataFrame(search_fr(), columns = [':::FR:::'])
    df_two = pd.DataFrame(search_fr_two(), columns = [':::FR:::'])
    df_three = pd.DataFrame(search_fr_three(), columns = [':::FR:::'])

    ################################ FR Airpods 1 & 2 ##############################
    df_four = pd.DataFrame(search_fr_no_pro(), columns = [':::FR:::'])
    df_five = pd.DataFrame(search_fr_no_pro_two(), columns = [':::FR:::'])
    df_six = pd.DataFrame(search_fr_no_pro_three(), columns = [':::FR:::'])

    ################################ FR Galaxy Buds ################################
    df_seven = pd.DataFrame(search_fr_galaxy_one(), columns = [':::FR:::'])
    df_eight = pd.DataFrame(search_fr_galaxy_two(), columns = [':::FR:::'])
    df_nine = pd.DataFrame(search_fr_galaxy_three(), columns = [':::FR:::'])


    ################################ IT Airpods Pro ################################

    it_df = pd.DataFrame(search_it(), columns = [':::IT:::'])
    it_df_two = pd.DataFrame(search_it_two(), columns = [':::IT:::'])
    it_df_three = pd.DataFrame(search_it_three(), columns = [':::IT:::'])

    ################################ IT Airpods 1 & 2 ##############################
    it_df_four = pd.DataFrame(search_it_no_pro(), columns = [':::IT:::'])
    it_df_five = pd.DataFrame(search_it_no_pro_two(), columns = [':::IT:::'])
    it_df_six = pd.DataFrame(search_it_no_pro_three(), columns = [':::IT:::'])

    ################################ IT Galaxy Buds ################################
    it_df_seven = pd.DataFrame(search_it_galaxy_one(), columns = [':::IT:::'])
    it_df_eight = pd.DataFrame(search_it_galaxy_two(), columns = [':::IT:::'])
    it_df_nine = pd.DataFrame(search_it_galaxy_three(), columns = [':::IT:::'])


    ################################ ES Airpods Pro ################################
    es_df = pd.DataFrame(search_es(), columns = [':::ES:::'])
    es_df_two = pd.DataFrame(search_es_two(), columns = [':::ES:::'])
    es_df_three = pd.DataFrame(search_es_three(), columns = [':::ES:::'])

    ################################ ES Airpods 1 & 2 ##############################
    es_df_four = pd.DataFrame(search_es_no_pro(), columns = [':::ES:::'])
    es_df_five = pd.DataFrame(search_es_no_pro_two(), columns = [':::ES:::'])
    es_df_six = pd.DataFrame(search_es_no_pro_three(), columns = [':::ES:::'])

    ################################ ES Galaxy Buds ################################
    es_df_seven = pd.DataFrame(search_es_galaxy_one(), columns = [':::ES:::'])
    es_df_eight = pd.DataFrame(search_es_galaxy_two(), columns = [':::ES:::'])
    es_df_nine = pd.DataFrame(search_es_galaxy_three(), columns = [':::ES:::'])


    ################################ NL Airpods Pro ################################
    nl_df = pd.DataFrame(search_nl(), columns = [':::NL:::'])
    nl_df_two = pd.DataFrame(search_nl_two(), columns = [':::NL:::'])
    nl_df_three = pd.DataFrame(search_nl_three(), columns = [':::NL:::'])

    ################################ NL Airpods 1 & 2 ##############################
    nl_df_four = pd.DataFrame(search_nl_no_pro(), columns = [':::NL:::'])
    nl_df_five = pd.DataFrame(search_nl_no_pro_two(), columns = [':::NL:::'])
    nl_df_six = pd.DataFrame(search_nl_no_pro_three(), columns = [':::NL:::'])

    ################################ NL Galaxy Buds ################################
    nl_df_seven = pd.DataFrame(search_nl_galaxy_one(), columns = [':::NL:::'])
    nl_df_eight = pd.DataFrame(search_nl_galaxy_two(), columns = [':::NL:::'])
    nl_df_nine = pd.DataFrame(search_nl_galaxy_three(), columns = [':::NL:::'])


    frames_total = pd.concat([df, df_two, df_three, df_four, df_five, df_six, df_seven, df_eight, df_nine, 
    it_df, it_df_two, it_df_three, it_df_four, it_df_five, it_df_six, it_df_seven, it_df_eight, it_df_nine,
    es_df, es_df_two, es_df_three, es_df_four, es_df_five, es_df_six, es_df_seven, es_df_eight, es_df_nine,
    de_df, de_df_two, de_df_three, de_df_four, de_df_five, de_df_six, de_df_seven, de_df_eight, de_df_nine,
    uk_df, uk_df_two, uk_df_three, uk_df_four, uk_df_five, uk_df_six, uk_df_seven, uk_df_eight, uk_df_nine,
    nl_df, nl_df_two, nl_df_three, nl_df_four, nl_df_five, nl_df_six, nl_df_seven, nl_df_eight, nl_df_nine
    ])


    frames_total.to_csv('amazon_list.csv', index=True)

    frames_total = pd.read_csv("amazon_list.csv")
    frames_total.shape


    driver.close()

    pyautogui.alert('Amazon search rank has been generated.')