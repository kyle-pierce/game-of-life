import patterns
import textViewer as viewer
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 1							# default value of an ON location
OFF = 0							# default value of an OFF location
VALS = [ON, OFF]				# values for each location
DEFAULT_SIZE = 100				# default world size
DEFAULT_INTERVAL = 50			# default update interval

# user's options at the main menu
MENU_OPTIONS = ('i', 'g', 's', 'q')
# user's options for world types to generate
WORLD_OPTIONS = ('random', 'block', 'beehive', 'loaf', 'boat', 'tub',
				 'blinker', 'toad', 'beacon', 'pulsar', 'pentadecathlon',
				 'glider', 'spaceship', 'glider gun')
# settings the user can change
SETTINGS = ('size', 'update interval')

def random_grid(grid_size):
	"""returns a grid of grid_size x grid_size random values"""
	return np.random.choice(VALS, grid_size * grid_size, p = [0.2, 0.8]).reshape(grid_size, grid_size)

def add_pattern(x, y, grid, pattern):
	"""adds the given pattern approximately centered on (x, y) to the given grid"""
	grid[x : x + len(pattern), y : y + len(pattern[0])] = pattern

def update(frame_num, img, grid, grid_size):
	"""updates the values in the current grid using Conway's rules"""

	# copy the grid so we can update an index as soon as calculating neighbors
	new_grid = grid.copy()

	# for each index, total the ON neighbors and add value to the new grid
	for i in range(grid_size):
		for j in range(grid_size):
			# sum the neighbors (number of ON neighbors)
			total = sum_neighbors(grid, i, j, grid_size)

			# apply Conway's rules of life
			if (grid[i, j] == ON):
				# over/underpolulation kills 
				if (total < 2) or (total > 3):
					new_grid[i, j] = OFF
			else:
				# normal population -> prosperous
				if total == 3:
					new_grid[i, j] = ON

	# update the image and grid data
	img.set_data(new_grid)
	grid[:] = new_grid[:]

	return img

def sum_neighbors(grid, i, j, grid_size):
	"""returns the total number of ON neighbors of grid[i, j] of size grid_size x grid_size"""
	total = int((grid[i, (j - 1) % grid_size] + grid[i, (j + 1) % grid_size] +
		         grid[(i - 1) % grid_size, j] + grid[(i + 1) % grid_size, j] +
		         grid[(i - 1) % grid_size, (j - 1) % grid_size] + grid[(i - 1) % grid_size, (j + 1) % grid_size] +
		         grid[(i + 1) % grid_size, (j - 1) % grid_size] + grid[(i + 1) % grid_size, (j + 1) % grid_size]) / ON)
	return total;

def initialize_grid(random, grid_size):
	"""returns either a random or glider grid_size x grid_size grid"""
	grid = np.array([])

	# either generate a random world or one with the indicated pattern at the center
	if (random):
		grid = random_grid(grid_size)
	else:
		grid = np.zeros(grid_size * grid_size).reshape(grid_size, grid_size)
		pattern = getPatternFor(response)
		x, y = getLocation(grid_size, pattern)
		add_pattern(x, y, grid, pattern)

	return grid

def getLocation(grid_size, pattern):
	"""Returns the x, y location in the center of a grid with given size to put
	the indicated pattern"""
	x = (grid_size - len(pattern)) // 2
	y = (grid_size - len(pattern[0])) // 2
	return x, y

def getPatternFor(response):
	"""Returns the 2d array pattern indicated by the given response"""
	if (response == 'block'):
		return patterns.BLOCK
	elif (response == 'beehive'):
		return patterns.BEEHIVE
	elif (response == 'loaf'):
		return patterns.LOAF
	elif (response == 'boat'):
		return patterns.BOAT
	elif (response == 'tub'):
		return patterns.TUB
	elif (response == 'blinker'):
		return patterns.BLINKER
	elif (response == 'toad'):
		return patterns.TOAD
	elif (response == 'beacon'):
		return patterns.BEACON
	elif (response == 'pulsar'):
		return patterns.PULSAR
	elif (response == 'pentadecathlon'):
		return patterns.PENTADECATHLON
	elif (response == 'glider'):
		return patterns.GLIDER
	elif (response == 'spaceship'):
		return patterns.LWSS
	elif (response == 'glider gun'):
		return patterns.GLIDER_GUN
	else:
		return None

def initialize_animation(grid, update_interval, n):
	"""initialized the animation using the grid, update interval, and grid size"""
	fig, ax = plt.subplots()
	img = ax.imshow(grid, interpolation = 'nearest')
	return animation.FuncAnimation(fig, update, fargs = (img, grid, n, ), frames = 10,
								 	   interval = update_interval, save_count = 50)

def main():
	"""Runs the game of life, alternating between showing the automotata and prompting the 
	user for what they want to see next"""
	size = DEFAULT_SIZE
	update_interval = DEFAULT_INTERVAL

	viewer.printIntro()
	keepPlaying = True

	while keepPlaying:
		viewer.printMenu()
		response = viewer.getResponse(MENU_OPTIONS)

		if (response == 'i'):
			viewer.printInfo()
		elif (response == 'g'):
			viewer.printWorldOptions(WORLD_OPTIONS)
			response = viewer.getResponse(WORLD_OPTIONS)
			grid = initialize_grid(response, size)
			ani = initialize_animation(grid, update_interval, size)
			plt.show()
		elif (response == 's'):
			size, update_interval = viewer.printAndUpdateSettings(size, update_interval, SETTINGS);
		else:
			keepPlaying = False


# calls the main method
if __name__ == '__main__':
	main()