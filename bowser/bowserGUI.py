from tkinter import Tk, Label, Button, Listbox, END, EXTENDED, Frame, SUNKEN

from bowserScraper import BOARDS_4PLEBS


def greet():
	print("Greetings!")


def nothing():
	print("I do nothing!")


class BowserOptionsPane:
	def __init__(self, parent):

		self.parent = parent

		self.frame_options = Frame(self.parent, width=200, height=200, relief=SUNKEN)
		self.frame_options.pack()

		self.listbox_boards = Listbox(self.frame_options, selectmode=EXTENDED)
		'''List of boards the user wants to save to a CSV file'''
		self.listbox_boards.pack()

		# add all boards
		for item in BOARDS_4PLEBS:
			self.listbox_boards.insert(END, item)


class BowserMainGUI:
	def __init__(self, master):
		self.master = master
		master.title("A simple GUI")

		self.label_hello_world = Label(master, text="This is our first GUI!")
		self.label_hello_world.pack()

		self.button_greet = Button(master, text="Greet", command=greet)
		self.button_greet.pack()

		self.BowserOptionsPane = BowserOptionsPane(master)

		self.button_generate = Button(master, text="Generate CSV", command=nothing)
		'''When clicked, generate a CSV file.'''
		self.button_generate.pack()

		self.button_close = Button(master, text="Close", command=master.quit)
		'''Quits when clicked.'''
		self.button_close.pack()


if __name__ == '__main__':
	root = Tk()
	my_gui = BowserMainGUI(root)
	root.mainloop()
