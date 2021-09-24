from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


import config as credentials
PATH = "C:\Program Files (x86)\chromedriver.exe"


def travelBrands_execute(departingFrom, arrivingTo, departingFullDate, arrivingFullDate, adult, child, infant, connections, singleOrRound, threeDays):
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

    #driver.get('https://res.intair.com/resa/cota/index.php?Login_Type=&B2B=5d501a5d-0755-410d-84f5-3f316fd341d6')
    driver.get("https://login.en.travelbrandsagent.com/redirecttosinglesignonsubscriber.ashx?subscriber=https://www.travelbrandsagent.com/sso/air/launch.asp&lang=EN&type=AIRCAD")
    #Single Way
    if singleOrRound == 0:
        driver.find_element_by_id('OW').click()
        
    
    outbound_from = driver.find_element_by_id('OrigineAller')
    outbound_from.send_keys(departingFrom)
    outbound_to = driver.find_element_by_id('DestinationAller')
    outbound_to.send_keys(arrivingTo)
    departing_day = driver.find_element_by_id('JourAller')
    departing_day.send_keys(departingFullDate.strftime("%d"))

    departing_month = driver.find_element_by_xpath(
        "//select[@name='MoisAller']/option[text()='" 
        + departingFullDate.strftime("%B") 
        + " " 
        + departingFullDate.strftime("%Y") 
        + "']")

    departing_month.click()
    
    if not arrivingFullDate == "":
        arriving_day = driver.find_element_by_id('JourRetourAR')
        arriving_day.send_keys(arrivingFullDate.strftime("%d"))
        arriving_month = driver.find_element_by_xpath(
            "//select[@name='MoisRetourAR']/option[text()='" 
            + arrivingFullDate.strftime("%B") 
            + " "
            + arrivingFullDate.strftime("%Y") 
            + "']")
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

    if threeDays:
        driver.find_element_by_id('PlusMoins3Jours1').click()
    else:
        driver.find_element_by_xpath('//*[(@id = "search-other")]//div//input').click()
        


def royalScenic_execute(departingFrom, arrivingTo, departingFullDate, arrivingFullDate, adult, child, infant, singleOrRound, threeDays):
    driver = webdriver.Chrome(PATH)
    driver.get(credentials.ROYALSCENIC['link'])

    agency_name = driver.find_element_by_id("username")
    agency_name.send_keys(credentials.ROYALSCENIC['user'])

    agency_pass = driver.find_element_by_id("password")
    agency_pass.send_keys(credentials.ROYALSCENIC['pass'])
    
    agency_pass.send_keys(Keys.RETURN)

    #Single Way
    if(int(singleOrRound) == 0):
        driver.find_element_by_id('rbFlightOneWay').click()
    else: #Round Trip
        driver.find_element_by_id('rbFlightReturn').click()
        arrivalDate = driver.find_element_by_id('departure-date-2')
        arrivalDate.send_keys(arrivingFullDate.strftime('%m/%d/%Y')) #MMDDYYYY

    outbound_from = driver.find_element_by_id('departure-airport-1')
    outbound_from.send_keys(departingFrom)
    time.sleep(0.5)
    outbound_from.send_keys(Keys.ARROW_DOWN)
    
    outbound_to = driver.find_element_by_id('arrival-airport-1')
    outbound_to.send_keys(arrivingTo)
    time.sleep(0.5)
    outbound_to.send_keys(Keys.ARROW_DOWN)

    departureDate = driver.find_element_by_id('departure-date-1')
    departureDate.send_keys(departingFullDate.strftime('%m/%d/%Y')) #MMDDYYYY

    #PASSENGERS
    totalAdults = driver.find_element_by_xpath("//select[@id='noofAdult']/option[text()='" + adult + "']")
    totalAdults.click()

    if(int(child) >=1):
        totalChildren = driver.find_element_by_xpath("//select[@id='noOfChildren']/option[text()='" + child + "']")
        totalChildren.click()
        time.sleep(0.1)
        #Default Child age is assumed to be 7
        for childCount in range(int(child)):
            childId = "ChildAge" + str((childCount +1))
            driver.find_element_by_xpath("//select[@id='" + childId + "']/option[text()='" + ' 7' + "']").click()

    if(int(infant) >=1):
        totalInfants = driver.find_element_by_xpath("//select[@id='noOfInfant']/option[text()='" + infant + "']")
        totalInfants.click()    
        #Default Child age is assumed to be 7
        time.sleep(0.1)
        for infantCount in range(int(infant)):
            infantId = "InfantAge" + str((childCount +1))
            driver.find_element_by_xpath("//select[@id='" + infantId + "']/option[text()='" + '< 2 (lap)' + "']").click()

    submitButton = driver.find_element_by_id('btnSearchNow')
    submitButton.click()
    
    #search 3 days
    if threeDays: 
        submit3days = driver.find_element_by_id('flexible-dates-search')
        submit3days.click()