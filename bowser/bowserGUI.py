from tkinter import *
from typing import List

import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

matplotlib.use('TkAgg')

from bowserScraper import BOARDS_4PLEBS


def greet():
	print("Greetings!")


def nothing():
	print("I do nothing!")


class PlotClassExample:
	def __init__(self, window):
		self.window = window
		self.box = Entry(window)
		self.button = Button(window, text="Show example plot", command=self.plot_new_window)
		self.box.pack()
		self.button.pack()

	def plot_new_window(self):
		x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
		v = np.array([16, 16.31925, 17.6394, 16.003, 17.2861, 17.3131, 19.1259, 18.9694, 22.0003, 22.81226])
		p = np.array([16.23697, 17.31653, 17.22094, 17.68631, 17.73641, 18.6368,
					  19.32125, 19.31756, 21.20247, 22.41444, 22.11718, 22.12453])

		fig = Figure(figsize=(6, 6))
		axis = fig.add_subplot(111)
		axis.scatter(v, x, color='red')
		axis.plot(p, range(2 + max(x)), color='blue')
		axis.invert_yaxis()

		axis.set_title("Estimation Grid", fontsize=16)
		axis.set_ylabel("Y", fontsize=14)
		axis.set_xlabel("X", fontsize=14)

		new_window = Toplevel(root)

		canvas = FigureCanvasTkAgg(fig, master=new_window)
		canvas.get_tk_widget().pack()
		canvas.draw()


class BowserOptionsPane:
	def __init__(self, master):
		self.master = master

		self.frame_options = Frame(self.master, width=200, height=200, relief=SUNKEN)
		self.frame_options.pack()

		self.listbox_boards = Listbox(self.frame_options, selectmode=EXTENDED)
		'''List of boards the user wants to save to a CSV file'''
		self.listbox_boards.pack()

		# add all boards
		for item in BOARDS_4PLEBS:
			self.listbox_boards.insert(END, item)

	def get_selected_boards(self) -> List[str]:
		return [self.listbox_boards.get(idx) for idx in self.listbox_boards.curselection()]


class BowserMainGUI:

	def generate_csv(self):
		print("TODO!")

		print(self.bowserOptionsPane.get_selected_boards())

	def __init__(self, master):
		self.master = master
		master.title("A simple GUI")

		self.label_hello_world = Label(master, text="This is our first GUI!")
		self.label_hello_world.pack()

		self.frame_graph_control = Frame(self.master, relief=SUNKEN)
		'''Test graph controls.'''
		self.frame_graph_control.pack()

		# Add a plot to the plot frame.
		self.plotClassExample = PlotClassExample(self.frame_graph_control)

		self.button_greet = Button(master, text="Greet", command=greet)
		self.button_greet.pack()

		self.bowserOptionsPane = BowserOptionsPane(master)

		self.button_generate = Button(master, text="Generate CSV", command=self.generate_csv)
		'''When clicked, generate a CSV file.'''
		self.button_generate.pack()

		self.button_close = Button(master, text="Close", command=master.quit)
		'''Quits when clicked.'''
		self.button_close.pack()


if __name__ == '__main__':
	root = Tk()
	my_gui = BowserMainGUI(root)
	root.mainloop()
