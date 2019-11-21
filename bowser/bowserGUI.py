#!/usr/bin/env python3
from tkinter import *
from typing import List

import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from contentFlagger import ALL_CONTENT_FLAGGERS, ContentFlagger

matplotlib.use('TkAgg')

from bowserScraper import BOARDS_4PLEBS


def greet():
	print("Greetings!")


def nothing():
	print("I do nothing!")


def get_selected_listbox_items(listbox: Listbox) -> List[str]:
	"""Get all selected listbox items from a listbox"""
	return [listbox.get(idx) for idx in listbox.curselection()]


def apply_listbox_selections_to_array(listbox: Listbox, array: List[object]) -> List[object]:
	"""Given a listbox and an array, return which objects are selected by that listbox."""
	selections: List[int] = listbox.curselection()

	found = []

	for i in selections:
		found.append(array[i])

	return found


class PlotClassExample:
	def __init__(self, window):
		self.window = window
		self.button = Button(window, text="Show example plot", command=self.plot_new_window)
		self.button.pack()


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
	def __init__(self, master, contentFlaggers: List[ContentFlagger]):
		# Parent frame that houses us.
		self.master = master

		# List of ContentFlagger objects we can use.
		self.contentFlaggers = contentFlaggers

		# Frame we store our options in.
		self.frame_options = Frame(self.master, relief=SUNKEN)
		self.frame_options.pack()

		# Board selection
		self.label_boards = Label(self.frame_options, text="Select one or more boards:")
		self.label_boards.grid(column=0, row=0, pady=(0,2))

		# List of boards the user wants to save to a CSV file.
		self.listbox_boards = Listbox(self.frame_options, selectmode=EXTENDED, exportselection=False)
		self.listbox_boards.grid(column=0, row=1, sticky=EW)

		# Add all boards
		for item in BOARDS_4PLEBS:
			self.listbox_boards.insert(END, item)

		# Flagger selection
		self.label_flaggers = Label(self.frame_options, text="Select one or more flaggers to flag content:")
		self.label_flaggers.grid(column=0, row=2, pady=(21,2))

		# List of all flaggers the user wishes to use.
		self.listbox_flaggers = Listbox(self.frame_options, selectmode=EXTENDED, exportselection=False)
		self.listbox_flaggers.grid(column=0, row=3, sticky=EW)


		# Add panes for options
		self.bowserOptionsPane = BowserOptionsPane(master, contentFlaggers=ALL_CONTENT_FLAGGERS)

		# For testing graph control
		self.frame_graph_control = Frame(self.master, relief=SUNKEN)
		self.plotClassExample = PlotClassExample(self.frame_graph_control)

		# When clicked, generate a CSV file.
		self.button_generate = Button(master, text="Generate CSV", command=self.generate_csv)

		# Quits when clicked.
		self.button_close = Button(master, text="Close", command=master.quit)

		# Pack and organize 
		self.button_close.pack(side=BOTTOM)
		self.button_generate.pack(side=LEFT, fill=X)
		self.frame_graph_control.pack(side=RIGHT)

	def generate_csv(self):
		print("TODO!")

		boards = (self.bowserOptionsPane.get_selected_boards())
		if not boards:
			print("Dude! select some boards!")
		elif len(boards) == 1:
			print("also you can use CTRL")

		if boards:
			print(boards)

		contentFlaggers = self.bowserOptionsPane.get_selected_content_flaggers()
		if not contentFlaggers:
			print("dude! select some content flaggers!")
		elif len(boards) == 1:
			print("also you can use CTRL")

		if contentFlaggers:
			for contentFlagger in contentFlaggers:
				print(contentFlagger.description)

if __name__ == '__main__':
	root = Tk()
	my_gui = BowserMainGUI(root)
	root.mainloop()
