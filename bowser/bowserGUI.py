from tkinter import Tk, Label, Button, Listbox, END

from bowserScraper import BOARDS_4PLEBS


class MyFirstGUI:
	def __init__(self, master):
		self.master = master
		master.title("A simple GUI")

		self.label_hello_world = Label(master, text="This is our first GUI!")
		self.label_hello_world.pack()

		self.button_greet = Button(master, text="Greet", command=self.greet)
		self.button_greet.pack()

		self.button_generate = Button(master, text="Generate CSV", command=lambda: print("I do nothing!"))
		'''When clicked, generate a CSV file.'''
		self.button_generate.pack()

		self.listbox_boards = Listbox(master)
		self.listbox_boards.pack()

		for item in BOARDS_4PLEBS:
			self.listbox_boards.insert(END, item)

		self.button_close = Button(master, text="Close", command=master.quit)
		'''Quits when clicked.'''
		self.button_close.pack()

	def greet(self):
		print("Greetings!")


if __name__ == '__main__':
	root = Tk()
	my_gui = MyFirstGUI(root)
	root.mainloop()
