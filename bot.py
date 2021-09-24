from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


import config as credentials
PATH = "C:\Program Files (x86)\chromedriver.exe"


def travelBrands_execute(departingFrom, arrivingTo, departingDay, departingMonth, arrivingDay, arrivingMonth, adult, child, infant, connections):
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

    #Single Way
    oneWay = driver.find_element_by_id('OW')
    oneWay.click()
    
    outbound_from = driver.find_element_by_id('OrigineAller')
    outbound_from.send_keys(departingFrom)
    outbound_to = driver.find_element_by_id('DestinationAller')
    outbound_to.send_keys(arrivingTo)
    departing_day = driver.find_element_by_id('JourAller')
    departing_day.send_keys(departingDay)
    departing_month = driver.find_element_by_xpath("//select[@name='MoisAller']/option[text()='" + departingMonth + "']")
    departing_month.click()
    
    if not arrivingDay == "":
        arriving_day = driver.find_element_by_id('JourRetourAR')
        arriving_day.send_keys(arrivingDay)
        arriving_month = driver.find_element_by_xpath("//select[@name='MoisRetourAR']/option[text()='" + arrivingMonth + "']")
        arriving_month.click()

    total_adults = driver.find_element_by_xpath("//input[@name='PAXADL']")
    total_adults.clear()
    total_adults.send_keys(adult)
    
    total_childs = driver.find_element_by_xpath("//input[@name='PAXENF']")
    total_childs.clear()
    total_childs.send_keys(child)
    
    total_infants = driver.find_element_by_xpath("//input[@name='PAXBEB']")
    total_infants.clear()
    total_infants.send_keys(infant)
    
    flight_connection = driver.find_element_by_xpath("//select[@name='MaxConn']/option[text()='" + connections + "']")
    flight_connection.click()

    submit_button = driver.find_element_by_xpath('//*[(@id = "search-other")]//div//input')
    submit_button.click()

def royalScenic_execute():
    driver = webdriver.Chrome(PATH)
    driver.get(credentials.ROYALSCENIC['link'])

    agency_name = driver.find_element_by_id("username")
    agency_name.send_keys(credentials.ROYALSCENIC['user'])

    agency_pass = driver.find_element_by_id("password")
    agency_pass.send_keys(credentials.ROYALSCENIC['pass'])
    
    agency_pass.send_keys(Keys.RETURN)

    #Single Way
    oneWay = driver.find_element_by_id('rbFlightOneWay')
    oneWay.click()

    outbound_from = driver.find_element_by_id('departure-airport-1')
    outbound_from.send_keys('Vancouver')
    time.sleep(0.5)
    outbound_from.send_keys(Keys.ARROW_DOWN)
    
    outbound_to = driver.find_element_by_id('arrival-airport-1')
    outbound_to.send_keys('toronto')
    time.sleep(0.5)
    outbound_to.send_keys(Keys.ARROW_DOWN)

    departureDate = driver.find_element_by_id('departure-date-1')
    departureDate.send_keys('10/22/2021') #MMDDYYYY

    totalAdults = driver.find_element_by_xpath("//select[@id='noofAdult']/option[text()='" + '2' + "']")
    totalAdults.click()
