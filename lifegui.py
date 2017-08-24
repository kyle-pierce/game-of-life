import patterns
import lifecanvas as lc
import lifetoolbar as lt

class GameOfLifeGUI:
    """The GUI for the Game of Life, including a canvas and toolbar"""

    def __init__(self, master):
        """Initialize the GUI on the given widnow

        Keyword arguments:
        master -- window on which to build this GUI
        """
        self.master = master
        master.title('Conway\'s Game of Life')

        # initialize the canvas, place in GUI, bind the keypressed
        self.canvas = lc.LifeCanvas(master)
        self.canvas.grid(row = 0, column = 0, columnspan = 5)
        self.canvas.bind("<Button-1>", self.add_pattern)

        # initialize the toolbar and place in GUI
        self.toolbar = lt.LifeToolbar(master, self.canvas)
        self.toolbar.grid(row = 1, column = 0)

    def add_pattern(self, event):
        """Adds the selected Pattern in the toolbar to the clicked location

        Keyword arguments:
        event -- mouseclick on location where pattern should be placed
        """
        if (self.toolbar.box_value.get() in patterns.pattern_map.keys()):
            pattern = patterns.get(self.toolbar.box_value.get())
            self.canvas.add_pattern(event.x, event.y, pattern)