from tkinter import *
from tkinter import ttk

gui = Tk()

def buttonpress():
	print("this is working")
	pv = int(pv_value.get())
	payment = int(payment_value.get())
	fv = int(fv_value.get())
	rate = int(rate_value.get())
	t = int(time_value.get())

	print(pv, payment, fv, rate, t)
	solution = 0
	if pv == 0:
		solution = fv/((1+(rate/100))**t)
		print(solution)
	elif fv == 0:
		solution = pv*((1+rate/100)**t)
	elif payment == 0:
		if rate > 0:
				solution = ((rate/100)*pv)/(1-((1+rate/100)**-t))

	equals_value.set(solution)

def clearpress():
	pv_value.set(0)
	payment_value.set(0)
	fv_value.set(0)
	rate_value.set(0)
	time_value.set(0)
	equals_value.set(0)

equals_value = StringVar(value = 0)
pv_value = StringVar(value = 0)
payment_value = StringVar(value = 0)
fv_value = StringVar(value = 0)
rate_value = StringVar(value = 0)
time_value = StringVar(value = 0)

gui.title("Calculator")
gui.geometry("552x230")

equals_entry = Entry(gui, textvariable = equals_value, width = 80).grid(row = 1, column = 1, columnspan = 3)

pv_entry = Entry(gui, textvariable = pv_value, width = 25).grid(row = 2, column = 1)
pv_Label = Label(gui, text = "Present Value").grid(row = 2, column = 2)

payment_entry = Entry(gui, textvariable = payment_value, width = 25).grid(row = 3, column = 1)
payment_Label = Label(gui, text = "Payment").grid(row = 3, column = 2)

fv_entry = Entry(gui, textvariable = fv_value, width = 25).grid(row = 4, column = 1)
fv_Label = Label(gui, text = "Future Value").grid(row = 4, column = 2)

rate_entry = Entry(gui, textvariable = rate_value, width = 25).grid(row = 5, column = 1)
rate_Label = Label(gui, text = "Rate (%)").grid(row = 5, column = 2)

time_entry = Entry(gui, textvariable = time_value, width = 25).grid(row = 6, column = 1)
time_Label = Label(gui, text = "Time (in years)").grid(row = 6, column = 2)

calcuate = Button(gui, text = "Calculate", command = buttonpress).grid(row = 2, column = 3)
calcuate = Button(gui, text = "Clear All", command = clearpress).grid(row = 4, column = 3)


gui.mainloop()