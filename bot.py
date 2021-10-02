from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


import config as credentials
PATH = "C:\Program Files (x86)\chromedriver.exe"


def travelBrands_execute(departingFrom, arrivingTo, departingFullDate, arrivingFullDate, adult, child, infant, connections, singleOrRound, threeDays):
    driver = webdriver.Chrome(PATH)
    #Mazimize current window
    driver.maximize_window()
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
        
def tripPro_execute(departingFrom, arrivingTo, departingFullDate, arrivingFullDate, adult, child, infant, singleOrRound):
    
    driver = webdriver.Chrome(PATH)
    driver.get(credentials.TRIPPRO['link'])

    agency_name = driver.find_element_by_id("username")
    agency_name.send_keys(credentials.TRIPPRO['user'])

    agency_pass = driver.find_element_by_id("password")
    agency_pass.send_keys(credentials.TRIPPRO['pass'])
    agency_pass.send_keys(Keys.RETURN)
    
    #Flight Button
    driver.find_element_by_id('menu-items-Flights').click()

    if int(singleOrRound) ==0:
        driver.find_element_by_id('et_trip_type_0').click()
    else:
        driver.find_element_by_id('et_trip_type_1').click()
        arrivalDate = driver.find_element_by_id('departure-date-2')
        arrivalDate.send_keys(arrivingFullDate.strftime('%m/%d/%Y')) #MMDDYYYY

    outbound_from = driver.find_element_by_id('origin')
    outbound_from.send_keys(departingFrom)
    time.sleep(1)
    outbound_to = driver.find_element_by_id('destination')
    outbound_to.send_keys(arrivingTo)
    time.sleep(1)

    departureDate = driver.find_element_by_id('fromDate')
    departureDate.send_keys(departingFullDate.strftime('%m/%d/%Y')) #MMDDYYYY

    #PASSENGERS
    totalAdults = driver.find_element_by_id("adultCount")
    totalAdults.send_keys(int(adult))

    if(int(child) >=1):
        totalChildren = driver.find_element_by_id("childCount")
        totalChildren.send_keys(int(child))
        
    if(int(infant) >=1):
        totalInfants = driver.find_element_by_id("infantCount")
        totalInfants.send_keys(int(infant))  

    submitButton = driver.find_element_by_id('searchFlightButton')
    submitButton.click()
    
def airNet_execute(departingFrom, arrivingTo, departingFullDate, arrivingFullDate, adult, child, infant, singleOrRound):
    driver = webdriver.Chrome(PATH)
    #Mazimize current window
    driver.maximize_window()
    driver.get(credentials.AIRNET['link'])
    agency_name = driver.find_element_by_id("txtUser")
    agency_name.send_keys(credentials.AIRNET['user'])

    agency_pass = driver.find_element_by_id("txtPassword")
    agency_pass.send_keys(credentials.AIRNET['pass'])
    agency_pass.send_keys(Keys.RETURN)
    
    time.sleep(4)
    if int(singleOrRound) ==0:
        driver.find_element_by_id('PNL1O').click()
    else:
        driver.find_element_by_id('PNL1R').click()

        returningOutbound_from = driver.find_element_by_id('txtDepCity2')
        returningOutbound_from.send_keys(departingFrom)
        time.sleep(1)
        returningOutbound_from.send_keys(Keys.ARROW_DOWN)

        returningOutbound_to = driver.find_element_by_id('txtArrCity2')
        returningOutbound_to.send_keys(arrivingTo)
        time.sleep(1)
        returningOutbound_to.send_keys(Keys.ARROW_DOWN)

        arrivalDate = driver.find_element_by_id('txtDate2')
        driver.execute_script('document.getElementById("txtDate2").removeAttribute("readonly")')
        arrivalDate.clear()
        arrivalDate.send_keys(arrivingFullDate.strftime('%d-%b-%Y')) #MMDDYYYY

    
    outbound_from = driver.find_element_by_id('txtDepCity1')
    outbound_from.send_keys(departingFrom)
    time.sleep(1.5)
    outbound_from.send_keys(Keys.ARROW_DOWN)


    outbound_to = driver.find_element_by_id('txtArrCity1')
    outbound_to.send_keys(arrivingTo)
    time.sleep(1.5)
    outbound_to.send_keys(Keys.ARROW_DOWN)


    departureDate = driver.find_element_by_id('txtDate1')
    driver.execute_script('document.getElementById("txtDate1").removeAttribute("readonly")')
    departureDate.clear()
    departureDate.send_keys(departingFullDate.strftime('%d-%b-%Y')) #MMDDYYYY
    

    #PASSENGERS
    totalAdults = driver.find_element_by_id("ddlPaxADT")
    totalAdults.send_keys(int(adult))

    if(int(child) >=1):
        totalChildren = driver.find_element_by_id("ddlPaxCHD")
        totalChildren.send_keys(int(child))
        
    if(int(infant) >=1):
        totalInfants = driver.find_element_by_id("ddlPaxINF")
        totalInfants.send_keys(int(infant))  

    submitButton = driver.find_element_by_id('btnSearchP')
    submitButton.click()
    
def royalScenic_execute(departingFrom, arrivingTo, departingFullDate, arrivingFullDate, adult, child, infant, singleOrRound, threeDays):
    driver = webdriver.Chrome(PATH)
    #Mazimize current window
    driver.maximize_window()
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