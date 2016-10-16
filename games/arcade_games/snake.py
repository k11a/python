import tkinter
import random
import sys
import os

# Globals
WIDTH = 800
HEIGHT = 600
SEG_SIZE = 40
percent_snake_of_screen_for_win = 70
ADD_SNAKE_PER_APPLE = 10
SPEED = 6
BUFFER_VECTOR_SIZE = 10

IN_GAME = True
WIN_GAME = False
PAUSE_BETWEEN_FRAME = int(1000/SPEED-50)
SNAKE_LENGTH_WIN_GAME = WIDTH/SEG_SIZE*HEIGHT/SEG_SIZE*percent_snake_of_screen_for_win/100


# Helper functions
def create_block():
    """ Creates an apple to be eaten """
    global BLOCK
    global SPEED
    posx = SEG_SIZE * random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE)
    posy = SEG_SIZE * random.randint(1, (HEIGHT-SEG_SIZE) / SEG_SIZE)
    BLOCK = c.create_oval(posx, posy,
                          posx+SEG_SIZE, posy+SEG_SIZE,
                          fill="red")

def create_percent():
    global prcnt
    prcnt = c.create_text(WIDTH/2, 20,
                      text=str(int(len(s.segments)/SNAKE_LENGTH_WIN_GAME*100)) + "%    SPEED:" + str(SPEED),
                      font="Arial 20 bold",
                      fill="blue")

def main():
    """ Handles game process """
    global IN_GAME
    global WIN_GAME
    global PAUSE_BETWEEN_FRAME
    if IN_GAME:
        s.get_vector_buffer()
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
# increase snake
            for index in range(ADD_SNAKE_PER_APPLE):
                s.add_segment()
# try add apple on freeplace
            index2 = 0
            whileend = False
            while index2 < 10 and not whileend:
                whileend = True
                index2 += 1
                c.delete(BLOCK)
                create_block()
                for index in range(len(s.segments)-1):
                    if c.coords(BLOCK) == c.coords(s.segments[index].instance):
                        whileend = False
                        break

        # Wining
        elif len(s.segments)>SNAKE_LENGTH_WIN_GAME:
            IN_GAME = False
            WIN_GAME = True
        # Self-eating
        else:
            for index in range(len(s.segments)-1):
                if head_coords == c.coords(s.segments[index].instance):
                    IN_GAME = False
        root.after(PAUSE_BETWEEN_FRAME, main)


    # Not IN_GAME -> stop game and print message
    else:
        if WIN_GAME:
            c.create_text(WIDTH/2, HEIGHT/2,
                      text="Congratulations\nYou have WON!!!\n---\n0-9 - speed\nSpace - restart\nEsc - exit",
                      font="Arial 30 bold",
                      fill="red",
                      justify="center")
        else:
            c.create_text(WIDTH/2, HEIGHT/2,
                      text="GAME OVER!\n---\n0-9 - speed\nSpace - restart\nEsc - exit",
                      font="Arial 20 bold",
                      fill="red",
                      justify="center")



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
        self.vector_buffer = ["Right"]

    def move(self):
        """ Moves the snake with the specified vector"""
# add head segment
        self.segments.append(Segment(c.coords(self.segments[-1].instance)[0] + self.vector[0]*SEG_SIZE,
                                     c.coords(self.segments[-1].instance)[1] + self.vector[1]*SEG_SIZE))
# del last segment
        c.delete(self.segments[0].instance)
        del self.segments[0]

    def add_segment(self):
        """ Adds segment to the snake """
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        self.segments.insert(0, Segment(x, y))

    def keypress(self, event):
        global PAUSE_BETWEEN_FRAME
        global SPEED
# Add key to buffer
# Awesome trick for filter back move (eat himself) using abs and ord functions.
# Me know what this bad for big programs.
        if len(self.vector_buffer) < BUFFER_VECTOR_SIZE + 1\
                            and event.keysym in self.mapping\
                            and abs(ord(self.vector_buffer[-1][1])-ord(event.keysym[1]))>5:
            self.vector_buffer.append(event.keysym)
# Speed controll
        elif ord(event.keysym[0]) >= ord('0') and ord(event.keysym[0]) <= ord('9'):
            if ord(event.keysym[0]) == ord('0'):
                SPEED=int(10)
                PAUSE_BETWEEN_FRAME = int(50)
            else:
                SPEED=ord(event.keysym[0])-ord('0')
                PAUSE_BETWEEN_FRAME = int(1000/SPEED-50)
# Exit Game by Esc
        elif event.keysym == "Escape":
            sys.exit()
# Restart
        elif event.keysym == "space":
            os.system('python3 snake.py')
            sys.exit()


    def get_vector_buffer(self):
        if len(self.vector_buffer) > 1:
            self.vector = self.mapping[self.vector_buffer[1]]
            del self.vector_buffer[0]

# Setting up window
root = tkinter.Tk()
root.title("ExtraSnake")
# move windows
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
c.bind("<KeyPress>", s.keypress)

create_block()
main()
root.mainloop()
