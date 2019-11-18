from tkinter import Tk, Label, Button


class MyFirstGUI:
	def __init__(self, master):
		self.master = master
		master.title("A simple GUI")

		self.label = Label(master, text="This is our first GUI!")
		self.label.pack()

		self.greet_button = Button(master, text="Greet", command=self.greet)
		self.greet_button.pack()

		self.generate_button = Button(master, text="Generate CSV", command=lambda: print("I do nothing!"))
		'''When clicked, generate a CSV file.'''
		self.generate_button.pack()

		self.close_button = Button(master, text="Close", command=master.quit)
		self.close_button.pack()

	def greet(self):
		print("Greetings!")


if __name__ == '__main__':
	root = Tk()
	my_gui = MyFirstGUI(root)
	root.mainloop()
