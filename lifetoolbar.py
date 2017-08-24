import tkinter as tk
from tkinter.ttk import Combobox

import patterns

class LifeToolbar(tk.Frame):
	"""Represents the toolbar in the Game of Life GUI"""
	
	def __init__(self, master, canvas):
		"""Initialize this toolbar with buttons and a dropdown menu

		Keyword arguments:
		master -- window on which the toolbar is built
		canvas -- canvas associated with this toolbar"""
		super().__init__()

		self.master = master
		self.canvas = canvas

		self.initialize_buttons()

		self.initialize_dropdown()

	def initialize_buttons(self):
		"""Initializes all the buttons on this toolbar"""
		self.randomize = tk.Button(self.master, text = 'Randomize', 
			width = 10, command = self.canvas.randomize)
		self.randomize.grid(row = 1, column = 2)

		self.clear = tk.Button(self.master, text = 'Clear', width = 10, 
			command = self.canvas.clear)
		self.clear.grid(row = 1, column = 3)

		self.play = tk.Button(self.master, text = 'Play', width = 10, 
			command = self.canvas.start)
		self.play.grid(row = 1, column = 0)

		self.pause = tk.Button(self.master, text = 'Pause', width = 10, 
			command = self.canvas.pause)
		self.pause.grid(row = 1, column = 1)

	def initialize_dropdown(self):
		"""Initializes the dropdown menu for selecting patterns"""
		self.box_value = tk.StringVar(self.master, 'Choose Pattern')
		self.box = Combobox(self.master, textvariable = self.box_value)
		self.box['values'] = list(patterns.pattern_map.keys())
		self.box.grid(row = 1, column = 4)