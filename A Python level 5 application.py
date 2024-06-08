# import tkinter
# import calendar

# yy = int(input("What year is it? "))
# mm = 2

# num_days = calendar.monthrange(yy, mm)[1]

# mm = 0
# mm = int(input("What month is it in number form?"))

# if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
#     num_days = 31
# elif mm == 2:
#     num_days = num_days
# else:
#     num_days = 30

# x = 0
# y = 0 

# root = tkinter.Tk()
# root.title("Planner")

# def make_table():
#     x = 1
#     y = 0
#     d = 

#     for i in range(num_days):
#         label_date = tkinter.Label(root, text=)
#         label_date.grid(column=x, row=y)

#         x = x
#         y = y+1

#         entry_date = tkinter.Entry(root)
#         entry_date.grid(column=x, row=y)

#         x = x+1
#         y = 0
#         i = 1        

# button_create = tkinter.Button(root,text = "create",command = (make_table))
# button_create.grid(column=0, row=0)

# root.mainloop()


from tkinter import *
from tkcalendar import Calendar

root = Tk()

root.geometry("400x400")

yy = int(input("What year is it?"))
mm = int(input("What month is it in number form?"))
dd = int(input("What is the date?"))

cal = Calendar(root, selectmode = 'day', year = yy, month = mm, day = dd)

cal.pack(pady = 20)

var = StringVar()

def grad_date():
    booking = open('test.txt', 'a')
    event = var.get()
    booking.write(f"{event}, {cal.get_date()}.\n")
    booking.close()

Button(root, text = "Get date", command = grad_date).pack(pady = 20)
label_entry = Label(root, text="Enter event").pack(pady=10)
event_entry = Entry(root, textvariable=var).pack(pady=10)

date = Label(root, text = "")
date.pack(pady = 20)

root.mainloop()