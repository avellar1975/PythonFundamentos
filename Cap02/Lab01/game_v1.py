# Game Ping-Pong
# Objetivo da Atividade: Incluir comentários explicando o código

# Importando as os módulos que serão utilizados
from tkinter import Tk, Canvas
import random
import time

# Pergunta ao jogador o nível de jogo e guarda o valor na variável level
level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))

# Cria uma variável length a partir da variável level
length = 500/level

# Instancia o objeto root a partir da classe Tk()
root = Tk()
root.title("Ping Pong")
root.resizable(0, 0)
root.wm_attributes("-topmost", -1)

# Instancia o objeto canvas a partir da classe Canvas
canvas = Canvas(root, width=800, height=600, bd=0, highlightthickness=0)
canvas.pack()

# Chama o método update do objeto root
root.update()

# Cria as variáveis count do tipo int e lost do tipo bool
count = 0
lost = False


# Cria a classe Bola com seus atributos e métodos
class Bola:
    def __init__(self, canvas, Barra, color):
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

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
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3

        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)

        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count += 1
                score()

        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True


# Cria a classe Barra com seus atributos e métodos
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

        if not False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3


# Cria a função start_game()
def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")
    time.sleep(1)
    Barra.draw()
    Bola.draw()


# Cria a função score()
def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))


# Cria a função game_over()
def game_over():
    canvas.itemconfig(game, text="Game over!")


# Instancia os objetos Barra e Bola
Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")

# Invoca métodos dos objetos canvas e root
score_now = canvas.create_text(430, 20, text="Pontos: " + str(count),
                               fill="green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))


canvas.bind_all("<Button-1>", start_game)

root.mainloop()
