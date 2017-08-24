import tkinter as tk
import numpy as np

import model

GRID_SIZE = 100             # number of tiles across and down the canvas
UPDATE_INTERVAL = 50        # how long to wait between updates to animation

WIDTH = 500                 # width of the canvas
HEIGHT = 500                # height of the canvas
BORDER_WIDTH = 5            # width of the canvas' borders
BACKGROUND_COLOR = 'grey'   # color of the canvas' background
TILE_COLOR = 'black'        # color of tiles on the canvas

class LifeCanvas(tk.Canvas):

    def __init__(self, master):
        """Initializes a LifeCanvas on the given master window

        Keyword arguments:
        master -- window on which to place the canvas
        """
        super().__init__(master, width = WIDTH, height = HEIGHT, 
                         borderwidth = BORDER_WIDTH, background = BACKGROUND_COLOR)

        self.master = master
        self.loop = None

        self.current_grid = np.zeros(GRID_SIZE * GRID_SIZE).reshape(GRID_SIZE, GRID_SIZE)
        self.tiles = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    def randomize(self):
        """Randomizes the selected tiles on this canvas"""
        self.current_grid = model.random_grid(GRID_SIZE)
        self.update_tiles()

    def clear(self):
        """Clears all selected tiles on this canvas"""
        self.current_grid = model.empty_grid(GRID_SIZE)
        self.update_tiles()

        if self.loop:
            self.master.after_cancel(self.loop)
            self.loop = None

    def start(self):
        """Starts the game of life with current tiles placed"""
        if not self.loop:
            self.start_loop()

    def start_loop(self):
        """Continuously updates the tiles on the canvas using Conway's rules"""
        self.current_grid = model.update(self.current_grid)
        self.update_tiles()
        self.loop = self.master.after(UPDATE_INTERVAL, self.start_loop)

    def pause(self):
        """Pauses the current game of life"""
        if self.loop:
            self.master.after_cancel(self.loop)
            self.loop = None

    def add_pattern(self, x, y, pattern):
        """Adds the given pattern centered on x, y to the current grid

        Keyword arguments:
        x -- x location at which to place the pattern
        y -- y location at which to place the pattern
        pattern -- pattern to be placed
        """

        col_width, row_height = self.get_tile_dimensions()
        col = x // col_width        # column to place the pattern
        row = y // row_height       # row to place the pattern
        
        try:
            model.add_pattern(row, col, self.current_grid, pattern)
        except ValueError:
            print("Invalid Location")
        else:
            self.update_tiles()
            
    def get_tile_dimensions(self):
        """Returns the current column width and row height of the squares
         in this canvas"""
        col_width = self.winfo_width() // GRID_SIZE
        row_height = self.winfo_height() // GRID_SIZE
        return col_width, row_height

    def update_tiles(self):
        """Copies the current grid into the current tiles array"""
        col_width, row_height = self.get_tile_dimensions()

        # loop over each row and column
        # a 1 in the grid indicates a tile should be added to the tiles
        # a 0 in the grid indicates a tile should be removed from tiles
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.current_grid[row, col] == 1 and not self.tiles[row][col]:
                    # if there should be a tile but is not, make one
                    self.tiles[row][col] = self.create_rectangle(col * col_width, 
                        row * row_height, (col + 1) * col_width, (row + 1) * row_height, 
                        fill = TILE_COLOR, outline = BACKGROUND_COLOR)
                elif self.current_grid[row, col] == 0 and self.tiles[row][col]:
                    # if there should not be a tile but is one, remove it
                    self.delete(self.tiles[row][col])
                    self.tiles[row][col] = None