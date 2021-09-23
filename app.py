from tkinter import *
import bot

#Creates a Window Object
app = Tk()

app.title('Flight Searcher - Globalduniya Canada')
app.geometry('1080x720')

# Departing From Location
departingFrom = StringVar()
departingFrom_label = Label(app, text='Departing From: ', font=('bold' ,14), pady=20, padx=25)
departingFrom_label.grid(row=0, column=0)
departingFrom_entry = Entry(app, textvariable=departingFrom)
departingFrom_entry.grid(row=0, column=1)

# Arriving To Location
arrivingTo = StringVar()
arrivingTo_label = Label(app, text='Arriving To: ', font=('bold' ,14), pady=20, padx=25)
arrivingTo_label.grid(row=0, column=2)
arrivingTo_entry = Entry(app, textvariable=arrivingTo)
arrivingTo_entry.grid(row=0, column=3)

# Departing Day
departingDay = StringVar()
departingDay_label = Label(app, text='Departing Day: ', font=('bold' ,14), pady=20, padx=25)
departingDay_label.grid(row=1, column=0)
departingDay_entry = Entry(app, textvariable=departingDay)
departingDay_entry.grid(row=1, column=1)

# Departing Month
departingMonth = StringVar()
departingMonth_label = Label(app, text='Departing Month: ', font=('bold' ,14), pady=20, padx=25)
departingMonth_label.grid(row=1, column=2)
departingMonth_entry = Entry(app, textvariable=arrivingTo)
departingMonth_entry.grid(row=1, column=3)

# Arriving Day
arrivingDay = StringVar()
arrivingDay_label = Label(app, text='Arriving Day: ', font=('bold' ,14), pady=20, padx=25)
arrivingDay_label.grid(row=2, column=0)
arrivingDay_entry = Entry(app, textvariable=arrivingDay)
arrivingDay_entry.grid(row=2, column=1)

# Arriving Month
arrivingMonth = StringVar()
arrivingMonth_label = Label(app, text='Arriving Month: ', font=('bold' ,14), pady=20, padx=25)
arrivingMonth_label.grid(row=2, column=2)
arrivingMonth_entry = Entry(app, textvariable=arrivingMonth)
arrivingMonth_entry.grid(row=2, column=3)

# Adult Quantity
adult = StringVar()
adult_label = Label(app, text='Adult: ', font=('bold' ,14), pady=20, padx=25)
adult_label.grid(row=3, column=0)
adult_entry = Entry(app, textvariable=adult, width = 10)
adult_entry.grid(row=3, column=1)

# Child Quantity
child = StringVar()
child_label = Label(app, text='Child: ', font=('bold' ,14), pady=20, padx=25)
child_label.grid(row=3, column=2)
child_entry = Entry(app, textvariable=child, width = 10)
child_entry.grid(row=3, column=3)

# Infant Quantity
infant = StringVar()
infant_label = Label(app, text='Infant: ', font=('bold' ,14), pady=20, padx=25)
infant_label.grid(row=3, column=4)
infant_entry = Entry(app, textvariable=infant, width = 10)
infant_entry.grid(row=3, column=5)

# Connections

CONNECTION_OPTIONS = [
"Direct Flights",
"1 MAXIMUM",
"2 MAXIMUM",
"3 MAXIMUM"
] 
connections_label = Label(app, text='Connections: ', font=('bold' ,14),padx=25, pady=20)
connections_label.grid(row=4, column=0)
connections = StringVar()
connections.set(CONNECTION_OPTIONS[0]) # default value
connections_menu = OptionMenu(app, connections, *CONNECTION_OPTIONS)
connections_menu.grid(row=4, column =1)

# Search Button
search_button = Button(app, text="Search", height=3, width=15, command = bot.search)
search_button.grid(row=5, column=2)

#Search Button +- 3 days
search_button_3 = Button(app, text="Search +-3", height=3, width=15, command = bot.search3Days)
search_button_3.grid(row=5, column=3)




#Start Program
app.mainloop()




 

