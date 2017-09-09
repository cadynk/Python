from tkinter import *
from tkinter import ttk

class Calculator:
	calc_value = 0.0
	divtrigger = False
	multtrigger = False
	addtrigger = False
	subtrigger = False

	def __init__(self,gui):
		self.entry_value = StringVar (gui, value = "")
		gui.title("Calculator")
		gui.geometry("552x230")
		style = ttk.Style()
		style.configure("TButton",font = "serif 12",padding = 10)
		style.configure("TEntry", font = "Serif 12", padding = 10)

		self.number_entry = ttk.Entry(gui, textvariable = self.entry_value, width = 85)
		self.number_entry.grid(row = 0, columnspan = 6, padx = 10)
		
		self.button9 = ttk.Button(gui, text = "9", command = lambda: self.buttonpress("9")).grid(row = 2, column = 3)
		self.button8 = ttk.Button(gui, text = "8", command = lambda: self.buttonpress("8")).grid(row = 2, column = 2)
		self.button7 = ttk.Button(gui, text = "7", command = lambda: self.buttonpress("7")).grid(row = 2, column = 1)
		self.button6 = ttk.Button(gui, text = "6", command = lambda: self.buttonpress("6")).grid(row = 3, column = 3)
		self.button5 = ttk.Button(gui, text = "5", command = lambda: self.buttonpress("5")).grid(row = 3, column = 2)
		self.button4 = ttk.Button(gui, text = "4", command = lambda: self.buttonpress("4")).grid(row = 3, column = 1)
		self.button3 = ttk.Button(gui, text = "3", command = lambda: self.buttonpress("3")).grid(row = 4, column = 3)
		self.button2 = ttk.Button(gui, text = "2", command = lambda: self.buttonpress("2")).grid(row = 4, column = 2)
		self.button1 = ttk.Button(gui, text = "1", command = lambda: self.buttonpress("1")).grid(row = 4, column = 1)
		self.button0 = ttk.Button(gui, text = "0", command = lambda: self.buttonpress("0")).grid(row = 5, column = 2)
		self.buttonadd = ttk.Button(gui, text = "+", command = lambda: self.mathpress("+")).grid(row = 4, column = 4)
		self.buttonsub = ttk.Button(gui, text = "-", command = lambda: self.mathpress("-")).grid(row = 5, column = 4)
		self.buttonmult = ttk.Button(gui, text = "*", command = lambda: self.mathpress("*")).grid(row = 3, column = 4)
		self.buttondiv = ttk.Button(gui, text = "/", command = lambda: self.mathpress("/")).grid(row = 2, column = 4)
		self.buttonclear = ttk.Button(gui, text = "CE", command = lambda: self.clearpress("CE")).grid(row = 5, column = 1)
		self.buttonequal = ttk.Button(gui, text = "=", command = lambda: self.equalpress()).grid(row = 5, column = 3)

	def buttonpress (self, value):
		entry_value_concatenate = self.number_entry.get()
		entry_value_concatenate += value
		self.number_entry.delete(0,"end")
		self.number_entry.insert(0,entry_value_concatenate)

	def mathpress (self,value):
		if self.isfloat(str(self.number_entry.get())):
			divtrigger = False
			multtrigger = False
			addtrigger = False
			subtrigger = False
			self.calc_value = float(self.entry_value.get())
			if value == "/":
				self.divtrigger = True
			elif value == "*":
				self.multtrigger = True
			elif value == "-":
				self.subtrigger = True	
			else:
				value == "+"
				self.addtrigger = True

		self.number_entry.delete(0,"end")

	def equalpress(self):
		if self.addtrigger or self.subtrigger or self.multtrigger or self.divtrigger:
			if self.addtrigger:
				solution = self.calc_value + float(self.entry_value.get())
			elif self.subtrigger:
				solution = self.calc_value - float(self.entry_value.get())
			elif self.multtrigger:
				solution = self.calc_value * float(self.entry_value.get())
			else:
				solution = self.calc_value / float(self.entry_value.get())
		else: solution = float(self.number_entry.get())

		self.number_entry.delete(0, "end")
		self.number_entry.insert(0,solution)
	def clearpress(self,value):
		divtrigger = False
		multtrigger = False
		addtrigger = False
		subtrigger = False
		self.calc_value = ""
		self.number_entry.delete(0,"end")

	def isfloat(self,str_val):
		try:
			float(str_val)
			return True
		except ValueError:
			return False		
gui = Tk()
calc = Calculator(gui)
gui.mainloop()