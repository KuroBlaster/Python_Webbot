from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import config as credentials
PATH = "C:\Program Files (x86)\chromedriver.exe"


def travelBrands_execute():
    driver = webdriver.Chrome(PATH)
    driver.get(credentials.TRAVELBRANDS['link'])
    #Close a tab: driver.close()
    #close the browseer: driver.quit()
    #Get the webpage title: driver.title

    agency_number = driver.find_element_by_id("Number")

    agency_number.send_keys(credentials.TRAVELBRANDS['agency_number'])

    agency_name = driver.find_element_by_id("AgentName")
    agency_name.send_keys(credentials.TRAVELBRANDS['user'])

    agency_pass = driver.find_element_by_id("Password")
    agency_pass.send_keys(credentials.TRAVELBRANDS['pass'])
    agency_pass.send_keys(Keys.RETURN)

    driver.get('https://res.intair.com/resa/cota/index.php?Login_Type=&B2B=5d501a5d-0755-410d-84f5-3f316fd341d6')

    #Round Trip Section
    outbound = driver.find_element_by_id('OrigineAller')
    outbound.send_keys()

def search():
    return 1

def search3Days():
    return 1




#One Way Section