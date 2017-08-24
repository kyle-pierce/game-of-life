"""Components for interacting with the user in the Game of Life"""

PROMPT = ' >> '	# prompt symbol

def printIntro():
	"""Prints the introduction to the Game of Life"""
	print()
	print('Welcome to Conway\'s Game of Life!  This program explores the capabilities of')
	print('cellular automota based on a few simple rules.  You can choose the initial')
	print('settings of the world or choose a randomly generated one! ')

def printMenu():
	"""Prints the main menu"""
	print()
	print('Please select one of the following options:')
	print(' * (I)nfo on Conway\'s Game of Life')
	print(' * (G)enerate World')
	print(" * (S)ettings")
	print(' * (Q)uit')

def printWorldOptions(world_options):
	"""Prints the currently supported types of worlds"""
	print()
	print('Please select the type of world you\'d like:')
	for world_type in world_options:
		print(' * (' + world_type.title() + ') World')

def printInfo():
	"""Prints information about the Game of Life"""
	print()
	print('In the 1940\'s, Jon von Neumann developed a complex mathematical model for a computer')
	print('world which behaves similarly to biological life.  In the 1960\'s, John Conway set')
	print('out to create a much simpler model.  In 1970, Conway\'s Game of Life first appeared')
	print('in \"Scientific American\".  Here are his four simple rules:')
	print(' 1) Any live cell with fewer than two neighbors dies by underpopulation')
	print(' 2) Any live cell with two or three neighbors lives on')
	print(' 3) Any live cell with more than three neighbors dies by overpopulation')
	print(' 4) Any dead cell with exactly three neighbors becomes alive by reproduction')

def printAndUpdateSettings(size, update_interval, all_settings):
	"""Prints the current settings of the game"""
	print()
	print('Current Settings:')
	print(' World Size:      ' + str(size))
	print(' Update Interval: ' + str(update_interval))
	print()

	return updateSettings(size, update_interval, all_settings)

def updateSettings(size, update_interval, all_settings):
	"""Potentially updates the settings of the game at the user's request"""
	changeSettings = yesTo('Would you like to change these settings?')

	while (changeSettings): 
		print('Which setting would you like to change?')
		setting = getResponse(all_settings)

		if ('size' in setting.lower()):
			size = updateSetting(size, setting)
		else:
			update_interval = updateSetting(update_interval, setting)

		print()
		print('Setting successfully changed!')
		changeSettings = yesTo('Change more settings?')

	return size, update_interval

def updateSetting(old_value, setting_name):
	"""Asks the user for the new value for the given setting with given previous value,
	returning the updated value"""
	print('Current value of ' + setting_name + ': ' + str(old_value))
	print('Please enter the new value ...')
	return int(input(PROMPT))

def getResponse(response_options):
	"""Reads a response to the user until their response can be found in the given response options"""
	response = input(PROMPT).lower()
	while (response not in response_options):
		print('Invalid response! Try again ...')
		response = input(PROMPT).lower()
		print() 
	return response

def yesTo(prompt):
	"""Returns True if user responds with a word beginning with 'y' to the given prompt and
	False otherwise"""
	print(prompt + '(y/n)')
	return input(PROMPT).lower().startswith('y')