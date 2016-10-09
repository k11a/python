import tkinter
import random

# Globals
WIDTH = 800
HEIGHT = 600
SEG_SIZE = 40
percent_snake_of_screen_for_win = 80
ADD_SNAKE_PER_APPLE = 20
PAUSE_BETWEEN_FRAME = 150

IN_GAME = True
# Win game if snake take 50% of screen
SNAKE_LENGTH_WIN_GAME = WIDTH/SEG_SIZE*HEIGHT/SEG_SIZE*percent_snake_of_screen_for_win/100
WIN_GAME = False


# Helper functions
def create_block():
    """ Creates an apple to be eaten """
    global BLOCK
    posx = SEG_SIZE * random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE)
    posy = SEG_SIZE * random.randint(1, (HEIGHT-SEG_SIZE) / SEG_SIZE)
    BLOCK = c.create_oval(posx, posy,
                          posx+SEG_SIZE, posy+SEG_SIZE,
                          fill="red")

def create_percent():
    global prcnt
    prcnt = c.create_text(WIDTH/2, 20,
                      text=str(int(len(s.segments)/SNAKE_LENGTH_WIN_GAME*100))+"%",
                      font="Arial 20 bold",
                      fill="blue")

def main():
    """ Handles game process """
    global IN_GAME
    global WIN_GAME
    if IN_GAME:
        s.move()
        c.delete(prcnt)
        create_percent()
        head_coords = c.coords(s.segments[-1].instance)
        x1, y1, x2, y2 = head_coords
        # Check for collision with gamefield edges
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False
        # Eating apples
        elif head_coords == c.coords(BLOCK):
            for index in range(1,ADD_SNAKE_PER_APPLE):
                s.add_segment()
            index2 = 0
            whileend = False
            while index2 < 4 and not whileend:
                whileend = True
                index2 += 1
                c.delete(BLOCK)
                create_block()
                for index in range(len(s.segments)-1):
                    if c.coords(BLOCK) == c.coords(s.segments[index].instance):
                        whileend = False

        # Wining
        elif len(s.segments)>SNAKE_LENGTH_WIN_GAME:
            IN_GAME = False
            WIN_GAME = True
        # Self-eating
        else:
            for index in range(len(s.segments)-1):
                if head_coords == c.coords(s.segments[index].instance):
                    IN_GAME = False
        s.save_vector()
        root.after(PAUSE_BETWEEN_FRAME, main)

    # Not IN_GAME -> stop game and print message
    else:
        if WIN_GAME:
            c.create_text(WIDTH/2, HEIGHT/2,
                      text="Congratulations\nYou have WON!!!",
                      font="Arial 30 bold",
                      fill="red")
        else:
            c.create_text(WIDTH/2, HEIGHT/2,
                      text="GAME OVER!",
                      font="Arial 20 bold",
                      fill="red")



class Segment(object):
    """ Single snake segment """
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x+SEG_SIZE, y+SEG_SIZE,
                                           fill="white")


class Snake(object):
    """ Simple Snake class """
    def __init__(self, segments):
        self.segments = segments
        # possible moves
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        # initial movement direction
        self.vector = self.mapping["Right"]
        self.prev_vector = (1, 0)

    def move(self):
        """ Moves the snake with the specified vector"""
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
            c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,
                 x1+self.vector[0]*SEG_SIZE, y1+self.vector[1]*SEG_SIZE,
                 x2+self.vector[0]*SEG_SIZE, y2+self.vector[1]*SEG_SIZE)

    def add_segment(self):
        """ Adds segment to the snake """
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        self.segments.insert(0, Segment(x, y))

    def change_direction(self, event):
        """ Changes direction of snake """
#        if event.keysym in self.mapping:
#            self.vector = self.mapping[event.keysym]
        if event.keysym == "Left" and not self.prev_vector == (1,0):
            self.vector = (-1, 0)
        elif event.keysym == "Right" and not self.prev_vector == (-1,0):
            self.vector = (1, 0)
        elif event.keysym == "Up" and not self.prev_vector == (0,1):
            self.vector = (0, -1)
        elif event.keysym == "Down" and not self.prev_vector == (0,-1):
            self.vector = (0, 1)

    def save_vector(self):
        self.prev_vector = self.vector

# Setting up window
root = tkinter.Tk()
root.title("Best Game by MSV")
root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, 200, 100))

c = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg="#003300")
c.grid()
# catch keypressing
c.focus_set()
# creating segments and snake
segments = [Segment(SEG_SIZE, SEG_SIZE),
            Segment(SEG_SIZE*2, SEG_SIZE),
            Segment(SEG_SIZE*3, SEG_SIZE)]
s = Snake(segments)
create_percent()
# Reaction on keypress
c.bind("<KeyPress>", s.change_direction)

create_block()
main()
root.mainloop()
