from tkinter import *
from tkcalendar import Calendar
from datetime import datetime

root = Tk()

root.geometry("600x600")

#Tells the program the date
yy = int(input("What year is it?"))
mm = int(input("What month is it in number form?"))
dd = int(input("What is the date?"))

cal = Calendar(root, selectmode = 'day', year = yy, month = mm, day = dd)

cal.pack(pady = 10)

#Creates a variable to store the event
var = StringVar()

#Creates a text file to store family events
def grad_date():
    booking = open('test.txt', 'a')
    event = var.get()
    #Saves event in file
    booking.write(f"{event}, {cal.get_date()}\n")
    booking.close()
    with open(r'test.txt', 'r') as booking:
        lines = booking.readlines()
        for line in lines:
            event, date = line.strip().split(', ')
            date_format = '%m/%d/%y'
            date_obj = datetime.strptime(date, date_format).date()
            cal.calevent_create(date_obj, event, 'event')

    cal.tag_config('event', background="red", foreground="white")
    var.set("")

#Creates button to run function for saving non-family events and creates entry for input
Button(root, text = "Save entry", command = grad_date).pack(pady = 20)
label_entry = Label(root, text="Enter event").pack(pady=10)
event_entry = Entry(root, textvariable=var).pack(pady=10)

date = Label(root, text = "")
date.pack(pady = 10)

#Checking file for previously saved non-family events
with open(r'family.txt', 'r') as booking:
    lines = booking.readlines()
    for line in lines:
        event, date = line.strip().split(', ')
        date_format = '%m/%d/%y'
        date_obj = datetime.strptime(date, date_format).date()
        cal.calevent_create(date_obj, event, 'event')
        cal.tag_config('event', background="red", foreground="white")


#Creates variable for family events
var2 = StringVar()

#Creates a text file to store family events
def grad_date_2():
    booking2 = open('family.txt', 'a')
    event2 = var2.get()
    #Saves event in file
    booking2.write(f"{event2}, {cal.get_date()}\n")
    booking2.close()
    with open(r'family.txt', 'r') as booking2:
        lines = booking2.readlines()
        for line in lines:
            event2, date = line.strip().split(', ')
            date_format2 = '%m/%d/%y'
            date_obj2 = datetime.strptime(date, date_format2).date()
            cal.calevent_create(date_obj2, event2, 'event2')

    cal.tag_config('event2', background="green", foreground="white")
    var2.set("")

#Creates button to run function for saving family events and creates entry for input
Button(root, text = "Save entry (family)", command = grad_date_2).pack(pady = 20)
family_label_entry = Label(root, text="Enter family event").pack(pady=10)
family_event_entry = Entry(root, textvariable=var2).pack(pady=10)

date = Label(root, text = "")
date.pack(pady = 10)

#Checking file for previously saved family events
with open(r'family.txt', 'r') as booking:
    lines = booking.readlines()
    for line in lines:
        event2, date = line.strip().split(', ')
        date_format2 = '%m/%d/%y'
        date_obj2 = datetime.strptime(date, date_format2).date()
        cal.calevent_create(date_obj2, event2, 'event2')
        cal.tag_config('event2', background="green", foreground="white")

root.mainloop()