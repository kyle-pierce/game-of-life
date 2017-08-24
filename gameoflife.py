import tkinter as tk
import lifegui as lg

def main():
    """Begins the Game of Life simulation"""
    root = tk.Tk()
    lg.GameOfLifeGUI(root)
    root.resizable(width = False, height = False)
    root.mainloop()

# calls the main method
if __name__ == '__main__':
    main()
