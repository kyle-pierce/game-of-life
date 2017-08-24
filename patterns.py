import numpy as np

class Pattern:
	"""Represents a single predefined pattern in the Game of Life"""

	def __init__(self, template):
		"""Initializes a Pattern with the given template

		Keyword arguments:
		template -- template for this pattern
		"""
		self._element_data = template
		self._width = len(template)
		self._height = len(template[0])

	def pattern(self):
		"""Returns a numpy array representing the stored template"""
		return self._element_data

	def width(self):
		"""Returns the width of the stored template"""
		return self._width

	def height(self):
		"""Returns the height of the stored template"""
		return self._height

# STILL LIFE
BLOCK = np.array([[1, 1],
				  [1, 1]])

BEEHIVE = np.array([[0, 1, 1, 0],
					[1, 0, 0, 1],
					[0, 1, 1, 0]])

LOAF = np.array([[0, 1, 1, 0],
				 [1, 0, 0, 1],
				 [0, 1, 0, 1],
				 [0, 0, 1, 0]])

BOAT = np.array([[1, 1, 0],
				 [1, 0, 1],
				 [0, 1, 0]])

TUB = np.array([[0, 1, 0],
				[1, 0, 1],
				[0, 1, 0]])

# OSCILLATORS
BLINKER = np.array([[1, 1, 1]])

TOAD = np.array([[0, 1, 1, 1],
				 [1, 1, 1, 0]])

BEACON = np.array([[1, 1, 0, 0],
				   [1, 1, 0, 0],
				   [0, 0, 1, 1],
				   [0, 0, 1, 1]])

PULSAR = np.array([[0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
				   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				   [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
				   [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
				   [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
				   [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
				   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				   [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
				   [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
				   [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
				   [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
				   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				   [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]])

PENTADECATHLON = np.array([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
						   [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
						   [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]])

# SPACESHIPS
GLIDER = np.array([[0, 0, 1], 
				   [1, 0, 1],
				   [0, 1, 1]])

LWSS = np.array([[1, 0, 0, 1, 0],
				 [0, 0, 0, 0, 1],
				 [1, 0, 0, 0, 1],
				 [0, 1, 1, 1, 1]])

# GUNS					1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34, 35, 36 
GLIDER_GUN = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
					   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
					   [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					   [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# mapping from names to templates
pattern_map = {'Block' : BLOCK, 'Beehive' : BEEHIVE, 'Loaf' : LOAF, 'Boat' : BOAT,
			   'Tub' : TUB, 'Blinker' : BLINKER, 'Toad' : TOAD, 'Beacon' : BEACON,
			   'Pulsar' : PULSAR, 'Pentadecathlon' : PENTADECATHLON, 'Glider' : GLIDER,
			   'Spaceship' : LWSS, 'Glider Gun' : GLIDER_GUN}

def get(pattern_name):
	"""Returns a new Pattern associated with the given name

	Keyword arguments:
	pattern_name -- requested pattern; assumes is a valid template name
	"""
	return Pattern(pattern_map[pattern_name])