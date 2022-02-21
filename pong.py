from tkinter import *
import random
import time

level=int(input('Digite em que nível deseja jogar 1/2/3/4/5\n'))
length=420/level

root=Tk()
root.title('PONG')
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

canvas = Canvas(root, width=800, height=600, bd=0, highlightthickness=0,bg='#222222')
canvas.pack()

root.update()

count = 0
lost = False


class Ball:
    def __init__(self, canvas, Bar, color):
        self.canvas = canvas
        self.Bar = Bar
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 200, 200)

        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            if level==1 or level==2:
                self.y=3*level
            elif level==3 or level==4 or level==5:
                self.y =2*level

        if pos[3] >= self.canvas_height:
            if level==1 or level==2:
                self.y=-3*level
            elif level==3 or level==4 or level==5:
                self.y = -2*level

        if pos[0] <= 0:
            if level==1 or level==2:
                self.x=3*level
            elif level==3 or level==4 or level==5:
                self.x = 2*level

        if pos[2] >= self.canvas_width:
            if level==1 or level==2:
                self.x=-3*level
            elif level==3 or level==4 or level==5:
                self.x = -2*level

        self.Bar_pos = self.canvas.coords(self.Bar.id)

        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Bar_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Bar_pos[3]:
                if level == 1 or level == 2:
                    self.y = -3 * level
                elif level == 3 or level == 4 or level == 5:
                    self.y = -2 * level
                global count
                count += 1
                score()

        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True


class Barra:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0

        if self.pos[2] >= self.canvas_width:
            self.x = 0

        global lost

        if lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            if level==1 or level==2:
                self.x=-3*level
            elif level==3 or level==4 or level==5:
                self.x = -2*level

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            if level==1 or level==2:
                self.x=3*level
            elif level==3 or level==4 or level==5:
                self.x=2*level


def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(1)
    Bar.draw()
    Ball.draw()


def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))


def game_over():
    canvas.itemconfig(game, text="Game over!")

Bar = Bar(canvas, "blue")
Ball = Ball(canvas, Barra, "green")

score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill="green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))

canvas.bind_all("<Button-1>", start_game)

root.mainloop()
