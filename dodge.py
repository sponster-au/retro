import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.y = 0
        self.dx = 1
        self.dy = 0
        self.r = 10
        self.R = 10
        self.X = 100
        self.Y = 100
        self.dX = 1
        self.dY = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + self.dx * (10 - self.r)) % pyxel.width
        self.y = (self.y + self.dy * (10 - self.r)) % pyxel.height

        self.X = (self.X + self.dX * (10 - self.R)) % pyxel.width
        self.Y = (self.Y + self.dY * (10 - self.R)) % pyxel.height

        # print(self.x, self.y, self.dx, self.dy)
        if pyxel.btnp(pyxel.KEY_DOWN):
            # print("get down!")
            self.dx, self.dy = 0, 1
        elif pyxel.btnp(pyxel.KEY_UP):
            self.dx, self.dy = 0, -1
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.dx, self.dy = -1, 0
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.dx, self.dy = 1, 0

        if pyxel.btnp(pyxel.KEY_S):
            self.dY = 1
            self.dX = 0
        elif pyxel.btnp(pyxel.KEY_W):
            self.dX = 0
            self.dY = -1
        if pyxel.btnp(pyxel.KEY_A):
            self.dY = 0
            self.dX = -1
        if pyxel.btnp(pyxel.KEY_D):
            self.dX = 1
            self.dY = 0
        if pyxel.btnp(pyxel.KEY_COMMA):
            self.r = max(1, self.r - 1)
        if pyxel.btnp(pyxel.KEY_PERIOD):
            self.r = min(10, self.r + 1)

        if pyxel.btnp(pyxel.KEY_E):
            self.R = max(1, self.R - 1)
        if pyxel.btnp(pyxel.KEY_Q):
            self.R = min(10, self.R + 1)

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.x, self.y, self.r, 3)
        pyxel.circ(self.X, self.Y, self.R, 9)


App()
