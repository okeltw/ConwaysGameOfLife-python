#/bin/python3

from graphics import GraphWin, Point
from random import randint

## Done
# Game, Cell Constructors

## To Do
# Update, tick, rules - all cells seem to die?

class Cell:
    def __init__(self, x, y, is_alive, win):
        self.x = x
        self.y = y
        self.point = Point(x,y)
        self.is_alive = is_alive
        self.win = win

    def determine_fate(self, neighbors):
        if self.is_alive and ((neighbors < 2) or (neighbors > 3)):
            self.is_alive = False
        elif self.is_alive == False and neighbors == 3:
            self.is_alive = True
        else:
            pass
    
    def draw(self):
        if self.is_alive == True:
            self.point.draw(self.win)
        else:
            self.point.undraw()

class Game:
    def __init__(self, x_max, y_max, seed, win):
        self.x_max = x_max
        self.y_max = y_max
        self.range = range(0,(x_max+1)*(y_max+1))
        self.board = []
        for i in self.range:
                start_alive = seed[i]
                (x,y) = self.index_to_coord(i)
                self.board.append(Cell(x, y, start_alive, win))
                self.board[-1].draw() 

    def index_to_coord(self, i):
        y = 0
        while (i >= self.y_max):
            y += 1
            i -= self.y_max
        return (i, y)

    def coord_to_index(self, x, y):
        coord = self.x_max * y-1
        coord += x
        return coord

    def pawn_is_alive(self, x, y):
        index = self.coord_to_index(x,y)
        return int(0 <= x <= self.x_max) and (0 <= y <= self.y_max) and self.board[index].is_alive == True:

    def count_neighbors(self, x, y):
        neighbors = 0
        for x_offset in range(-1,1):
            for y_offset in range(-1,1):
                if x_offset == y_offset == 0:
                    continue
                else:
                    neighbors += self.pawn_is_alive(x_offset, y_offset)

        return neighbors

    def tick(self):
        for i in self.range:
                neighbors = self.count_neighbors(x,y)
                print('X={} Y={} Alive={} Neighbors={}'.format(x,y,self.board[i].is_alive, neighbors))
                self.board[i].determine_fate(neighbors)
                self.board[i].draw()

def gen_seed(xlim, ylim):
    probability = 50 # probability that cell starts alive

    length = (xlim+1) * (ylim+1)
    seed = []
    for i in range(0, length):
        seed.append(randint(0,100) <= probability)

    return seed

def main():
    x_lim = 100
    y_lim = 100
    win = GraphWin("Game of Life", x_lim, y_lim)

    seed = gen_seed(x_lim, y_lim)
    game = Game(x_lim, y_lim, seed, win)

    for iteration in range(0,1):
        win.getMouse()
        game.tick()

    print('Done!')
    win.getMouse()
    win.close()

main()
