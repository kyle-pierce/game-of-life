import numpy as np
import patterns

ON = 1				# value of an ON location on the grid
OFF = 0				# value of an OFF location on the grid
VALS = [ON, OFF]	# all possible states for a cell

# methods related to initializing and adding patterns to the grid

def random_grid(size):
	"""Returns a grid of size x size randomly-chosen values.

	Keyword arguments:
	size -- size of the requested grid
	"""
	random_array = np.random.choice(VALS, size * size, p = [0.2, 0.8])
	return random_array.reshape(size, size)

def empty_grid(size):
	"""Returns a grid of size x size empty values.

	Keyword arguments:
	size -- size of the requested grid
	"""
	return np.zeros(size * size).reshape(size, size)

def add_pattern(x, y, grid, pattern):
	"""Adds the given pattern centered on (x, y) to the given grid.

	Keyword arguments:
	x -- x location for the center of the pattern
	y -- y locations for the center of the pattern
	grid -- grid on which to place the pattern
	pattern -- pattern to be placed
	"""
	x = (x - pattern.width() // 2)	# adjust x coordinate
	y = (y - pattern.height() // 2)		# adjust y coordinate
	grid[x:x + pattern.width(), y:y + pattern.height()] = pattern.pattern()

def update(grid):
	"""Applies Conway's rules to the given grid once.

	Keyword arguments:
	grid -- the grid to be updated
	"""

	# store the size for convenience
	size = len(grid)

	# copy the grid so we can update an index as soon as calculating neighbors
	new_grid = grid.copy()

	# for each index, total the ON neighbors and add value to the new grid
	for row in range(size):
		for col in range(size):
			# sum the neighbors (number of ON neighbors)
			total = sum_neighbors(grid, row, col)

			# apply Conway's rules of life
			if (grid[row, col] == ON):
				# over/underpolulation kills 
				if (total < 2) or (total > 3):
					new_grid[row, col] = OFF
			else:
				# normal population -> prosperous
				if total == 3:
					new_grid[row, col] = ON

	# return the updated grid
	return new_grid

def sum_neighbors(grid, row, col):
	"""Returns the sum of the neighbors of [row, col] on the given grid.

	Keyword arguments:
	row -- row of the cell whose neighbors are to be summed
	col -- column of the cell whose neighbors are to be summed
	"""
	size = len(grid)
	total = int((grid[row, (col - 1) % size] + grid[row, (col + 1) % size] +
		         grid[(row - 1) % size, col] + grid[(row + 1) % size, col] +
		         grid[(row - 1) % size, (col - 1) % size] + grid[(row - 1) % 
		         size, (col + 1) % size] +
		         grid[(row + 1) % size, (col - 1) % size] + grid[(row + 1) % 
		         size, (col + 1) % size]) / ON)
	return total;