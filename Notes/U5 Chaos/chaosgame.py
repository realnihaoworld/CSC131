from random import choice, randint
from tkinter import *

# constants
WIDTH = 1000
HEIGHT = 1000
POINT_COLORS = ["black", "red", "green", "blue"]
POINT_RADIUS = 0
NUM_POINTS = 5000

class ChaosGame(Canvas):

    def __init__(self, parent): # parent is the container (window)
        Canvas.__init__(self, parent, bg="white")
        self.pack(fill=BOTH, expand=1)
    
    # sierpenski triangle
    def plot_all_points(self, num_points):
        v1 = [0, HEIGHT - 1]
        v2 = [(WIDTH -1) / 2, 0]
        v3 = [WIDTH - 1, HEIGHT - 1]
        vertices = [v1, v2, v3]
        self.plot_point(v1[0], v1[1])
        self.plot_point(v2[0], v2[1])
        self.plot_point(v3[0], v3[1])
        
        p1 = choice(vertices)
        p2 = choice(vertices)
        
        mid = [(p1[0] + p2[0])/2, (p1[1] + p2[1])/2]
        
        self.plot_point(mid[0], mid[1])
        
        for _ in range(num_points):
            p1 = choice(vertices)
            new_mid = [(p1[0] + mid[0])/2, (p1[1] + mid[1])/2]
            self.plot_point(new_mid[0], new_mid[1])
            mid = new_mid
        
    def plot_point(self, x0, y0):
        rand_color = choice(POINT_COLORS)
        x1 = x0 + POINT_RADIUS * 2
        y1 = y0 + POINT_RADIUS * 2
        self.create_oval(x0, y0, x1, y1, outline=rand_color, fill=rand_color)
        
window = Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")
window.title("Yo")
p = ChaosGame(window)
p.plot_all_points(NUM_POINTS)
window.mainloop()