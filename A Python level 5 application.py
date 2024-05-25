import tkinter
import calendar

yy = int(input("What year is it? "))
mm = 2

num_days = calendar.monthrange(yy, mm)[1]

mm = 0
mm = int(input("What month is it in number form?"))

if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
    num_days = 31
elif mm == 2:
    num_days = num_days
else:
    num_days = 30

x = 0
y = 0 

root = tkinter.Tk()
root.title("Planner")

for i in range(num_days):
    label_date = tkinter.Label(root, text="skibidi")
    label_date.grid(column=x, row=y)

    x = x
    y = y+1

    entry_date = tkinter.Entry(root)
    entry_date.grid(column=x, row=y)

    x = x+1
    y = 0