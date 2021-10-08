from tkinter import *
import bot

import threading
import datetime

def search (threeDays = False):
    departingFullDate = datetime.datetime(
    int(departingYear.get()), 
    int(departingMonth.get()), 
    int(departingDay.get())
    )
    
    if(int(singleOrRound.get()) !=0):
        arrivingFullDate = datetime.datetime(
            int(arrivingYear.get()), 
            int(arrivingMonth.get()), 
            int(arrivingDay.get()))
    else:
        arrivingFullDate = ''
    
    googleFlights = threading.Thread(
                target = bot.googleFlights_execute, 
                args = (departingFrom.get(), 
                arrivingTo.get(), 
                departingFullDate,
                arrivingFullDate,
                adult.get(), 
                child.get(), 
                infant.get(), 
                connections.get(),
                int(singleOrRound.get()),
                threeDays
        ))
    googleFlights.start()

    travelBrands = threading.Thread(
                target = bot.travelBrands_execute, 
                args = (departingFrom.get(), 
                arrivingTo.get(), 
                departingFullDate,
                arrivingFullDate,
                adult.get(), 
                child.get(), 
                infant.get(), 
                connections.get(),
                int(singleOrRound.get()),
                threeDays
        ))
    travelBrands.start()
    
    #RoyalScenic
        
    royalScenic = threading.Thread(
                target = bot.royalScenic_execute, 
                args = (departingFrom.get(), 
                arrivingTo.get(), 
                departingFullDate, 
                arrivingFullDate, 
                adult.get(), 
                child.get(), 
                infant.get(), 
                singleOrRound.get(), 
                threeDays))

    royalScenic.start()

    '''
    tripPro = threading.Thread(
        target = bot.tripPro_execute, 
        args = (departingFrom.get(), 
            arrivingTo.get(), 
            departingFullDate, 
            arrivingFullDate, 
            adult.get(), 
            child.get(), 
            infant.get(), 
            singleOrRound.get()))

    tripPro.start()
    '''

    airNet = threading.Thread(
                target = bot.airNet_execute, 
                args = (departingFrom.get(), 
                    arrivingTo.get(), 
                    departingFullDate, 
                    arrivingFullDate, 
                    adult.get(), 
                    child.get(), 
                    infant.get(), 
                    singleOrRound.get()))

    airNet.start()
    
def search3Days():
    search(threeDays = True)


#Creates a Window Object
app = Tk()

app.title('Flight Searcher - Globalduniya Canada')
app.geometry('1200x500')

#Single or Round Ticket
singleOrRound = StringVar(value='0')
singleOrRound_label = Label(app, text='0 For Single/ 1 For Round: ', font=('bold' ,14), pady=20, padx=25)
singleOrRound_label.grid(row=0, column=0)
singleOrRound_entry = Entry(app, textvariable=singleOrRound)
singleOrRound_entry.grid(row=0, column=1)

# Departing From Location
departingFrom = StringVar(value='Vancouver')
departingFrom_label = Label(app, text='Departing From: ', font=('bold' ,14), pady=20, padx=25)
departingFrom_label.grid(row=1, column=0)
departingFrom_entry = Entry(app, textvariable=departingFrom)
departingFrom_entry.grid(row=1, column=1)

# Arriving To Location
arrivingTo = StringVar(value='Delhi')
arrivingTo_label = Label(app, text='Arriving To: ', font=('bold' ,14), pady=20, padx=25)
arrivingTo_label.grid(row=1, column=2)
arrivingTo_entry = Entry(app, textvariable=arrivingTo)
arrivingTo_entry.grid(row=1, column=3)

# Departing Day
departingDay = StringVar()
departingDay_label = Label(app, text='Departing Day(DD): ', font=('bold' ,14), pady=20, padx=25)
departingDay_label.grid(row=2, column=0)
departingDay_entry = Entry(app, textvariable=departingDay)
departingDay_entry.grid(row=2, column=1)

# Departing Month
departingMonth = StringVar()
departingMonth_label = Label(app, text='Departing Month(MM): ', font=('bold' ,14), pady=20, padx=25)
departingMonth_label.grid(row=2, column=2)
departingMonth_entry = Entry(app, textvariable=departingMonth)
departingMonth_entry.grid(row=2, column=3)

# Departing Year
departingYear = StringVar()
departingYear_label = Label(app, text='Departing Year(YYYY): ', font=('bold' ,14), pady=20, padx=25)
departingYear_label.grid(row=2, column=4)
departingYear_entry = Entry(app, textvariable=departingYear)
departingYear_entry.grid(row=2, column=5)

# Arriving Day
arrivingDay = StringVar()
arrivingDay_label = Label(app, text='Arriving Day(DD): ', font=('bold' ,14), pady=20, padx=25)
arrivingDay_label.grid(row=3, column=0)
arrivingDay_entry = Entry(app, textvariable=arrivingDay)
arrivingDay_entry.grid(row=3, column=1)

# Arriving Month
arrivingMonth = StringVar()
arrivingMonth_label = Label(app, text='Arriving Month(MM): ', font=('bold' ,14), pady=20, padx=25)
arrivingMonth_label.grid(row=3, column=2)
arrivingMonth_entry = Entry(app, textvariable=arrivingMonth)
arrivingMonth_entry.grid(row=3, column=3)

# Arriving Year
arrivingYear = StringVar()
arrivingYear_label = Label(app, text='Arriving Year(YYYY): ', font=('bold' ,14), pady=20, padx=25)
arrivingYear_label.grid(row=3, column=4)
arrivingYear_entry = Entry(app, textvariable=arrivingYear)
arrivingYear_entry.grid(row=3, column=5)

# Adult Quantity
adult = StringVar()
adult_label = Label(app, text='Adult: ', font=('bold' ,14), pady=20, padx=25)
adult_label.grid(row=4, column=0)
adult_entry = Entry(app, textvariable=adult, width = 10)
adult_entry.grid(row=4, column=1)

# Child Quantity
child = StringVar(value='0')
child_label = Label(app, text='Child: ', font=('bold' ,14), pady=20, padx=25)
child_label.grid(row=4, column=2)
child_entry = Entry(app, textvariable=child, width = 10)
child_entry.grid(row=4, column=3)

# Infant Quantity
infant = StringVar(value='0')
infant_label = Label(app, text='Infant: ', font=('bold' ,14), pady=20, padx=25)
infant_label.grid(row=4, column=4)
infant_entry = Entry(app, textvariable=infant, width = 10)
infant_entry.grid(row=4, column=5)

# Connections

CONNECTION_OPTIONS = [
"Direct flights",
"1 Maximum",
"2 Maximum",
"3 Maximum"
] 
connections_label = Label(app, text='Connections: ', font=('bold' ,14),padx=25, pady=20)
connections_label.grid(row=5, column=0)
connections = StringVar()
connections.set(CONNECTION_OPTIONS[0]) # default value
connections_menu = OptionMenu(app, connections, *CONNECTION_OPTIONS)
connections_menu.grid(row=5, column =1)

# Search Button
search_button = Button(app, text="Search", height=3, width=15, command = search)
search_button.grid(row=6, column=2)

#Search Button +- 3 days
search_button_3 = Button(app, text="Search +-3", height=3, width=15, command = search3Days)
search_button_3.grid(row=6, column=3)

#Start Program
app.mainloop()

 

