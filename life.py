import pyxel
import time


class App:
    def __init__(self):
        pyxel.init(16, 12, caption="Conway's Life", scale=50)
        self.running = False
        # grid[x][y]
        self.grid = [[0 for i in range(pyxel.height)] for j in range(pyxel.width)]
        self.tick_period = 1.0
        self.last_tick = time.time()
        pyxel.run(self.update, self.draw)

    def interact(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.running = not self.running
        if pyxel.btnp(pyxel.KEY_LEFT_BUTTON):
            self.grid[pyxel.mouse_x][pyxel.mouse_y] ^= 1
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.tick_period *= 1.5
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.tick_period /= 1.5

    def neighbour_count(self, x, y):
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                xx = x + dx
                yy = y + dy
                if dx == 0 and dy == 0:
                    continue
                if xx < 0 or xx >= pyxel.width:
                    continue
                if yy < 0 or yy >= pyxel.height:
                    continue
                count += self.grid[xx][yy]
        return count

    def update(self):
        self.interact()
        if self.running and time.time() - self.last_tick > self.tick_period:
            self.last_tick = time.time()
            new_grid = [[0 for i in range(pyxel.height)] for j in range(pyxel.width)]
            for x in range(pyxel.width):
                for y in range(pyxel.height):
                    n = self.neighbour_count(x, y)
                    if self.grid[x][y] == 1 and n in (0, 1):
                        new_grid[x][y] = 0
                    if self.grid[x][y] == 1 and n in (2, 3):
                        new_grid[x][y] = 1
                    if self.grid[x][y] == 1 and n > 3:
                        new_grid[x][y] = 0
                    if self.grid[x][y] == 0 and n == 3:
                        new_grid[x][y] = 1
            self.grid = new_grid

    def draw(self):
        if self.running:
            # running - red on black
            bg = 0
            fg = 8
        else:
            # stopped - black on white
            bg = 7
            fg = 0
            pyxel.cls(0)
        pyxel.cls(bg)
        for x in range(pyxel.width):
            for y in range(pyxel.height):
                if self.grid[x][y] == 1:
                    pyxel.pix(x, y, fg)


App()
