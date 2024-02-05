# Name: Danison Zhang
# Description: The Reckober (calculator project)
# Date: 2/15 (due)

from tkinter import *
from button_data import button_data

WIDTH = 400
HEIGHT = 650
ROWS = 6
COL = 4
class MainGUI(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        self.eval = False
        self.setupGUI()
    
    @property
    def eval(self):
        return self._eval
    @eval.setter
    def eval(self, value: bool):
        self._eval = value
    
    def setupGUI(self):
        # the display is where it displays what we are typing
        self.display = Label(
            self, # this is the parent
            text="",
            anchor=E,
            bg="white",
            fg="black",
            height = 1,
            font=("TexGyreAdventor", 50)
        )
        
        self.display.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky=E+W+N+S
        )
        
        # configuration of rows and columns
        for row in range(ROWS):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(COL):
            Grid.columnconfigure(self, col, weight=1)
        
        for button in button_data:
            self.make_button(
            button["row"],
            button["column"],
            button["value"]
        )
            
        self.pack(fill=BOTH, expand=1)
        
        
    def make_button(self, row, col, value):
        bg_color = "#dddddd"
        if value == "=":
            bg_color = "blue"
            
        if value in ["(", ")", "AC", "**", "+", "-", "*", "/", "<-", "%"]:
            bg_color = "#999999"
        
        button = Button(
            self,
            font=("TexGyreAdventor", 30),
            text=value,
            fg="black",
            bg=bg_color, # works for pc, but not mac
            highlightbackground=bg_color, # ths works on macs
            borderwidth=0,
            highlightthickness=0,
            width=5,
            activebackground="white",
            command=lambda: self.process(value)
        )
        
        # Creates each button and puts them on the gui
        if value == "=":
            button.grid(row=row, column=col, columnspan=2, sticky=NSEW)
        else:
            button.grid(row=row, column=col, sticky=NSEW)
        
    def clear_display(self):
        self.display["text"] = ""
        
    def set_display(self, value):
        self.display["text"] = value
        
    def append_display(self, value):
        self.display["text"] += value
    
    def backspace(self):
        current = self.display["text"]
        new_value = current[1:]
        self.display["text"] = new_value
        
    def evaluate(self):
        expr = self.display["text"]
        try:
            result = str(eval(expr))
            self.set_display(result)
            self.eval = True
        except:
            self.set_display("ERROR")
            
    # processes the action according to the button value
    def process(self, button):
        if self.display["text"] == "ERROR":
            self.clear_display()
        
        # This is to determine whether or not we clear the display,
        # If the user does a calculation then wants to do a calculation on that,
        # then the screen won't be cleared, but if they input a number,
        # then it automatically clears
        try:
            is_int = isinstance(int(button), int)
        except:
            is_int = False
        if self.eval == True and is_int:
            self.clear_display()
            self.eval = False
        
        # This does the function according to what button is pressed
        if button == "AC":
            self.clear_display()
        elif button == "=":
            self.evaluate()
            print(self.eval)
        elif button == "<-":
            self.backspace()
        elif 11 <= len(self.display["text"]) < 14:
            self.append_display(".")
        elif len(self.display["text"]) < 11:
            self.append_display(button)
            self.eval = False
            print(self.eval)
    
    # TODO: Assignment:
    #  ! Clear the display at all appropriate times
    #  ! just evaluated something
    #  ! just got an error
    # !2. Add functionality
    # !check phone for layout, equal sign spans over two columns
    # !3. Limit display to 14 char, if longer, then put . . . at the end or use scientific notation
    # !ie. 12345678901...
    # TODO: calculate numbers with results bigger than 14 char
    

## Main
window = Tk()
window.title("The Reckoner")
window.geometry(f"{WIDTH}x{HEIGHT}")
p = MainGUI(window)
window.mainloop()
