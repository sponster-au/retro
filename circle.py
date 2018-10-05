import pyxel
import random
import time
import math


class App:
    MAX_R = 10
    SPEED = 0.5

    def new_circle(self):
        self.start = time.time()
        self.r = 0
        self.x = random.randint(0, pyxel.width)
        self.y = random.randint(0, pyxel.height)

    def is_in_circle(self, xx, yy):
        d = math.hypot(xx - self.x, yy - self.y)
        return d <= self.r

    def __init__(self):
        pyxel.init(160, 120)
        self.new_circle()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT_BUTTON):
            # print(pyxel.mouse_x, pyxel.mouse_y)
            if self.is_in_circle(pyxel.mouse_x, pyxel.mouse_y):
                self.new_circle()
                self.SPEED *= 0.9
        if time.time() - self.start > self.SPEED:
            self.r += 1
            self.start = time.time()
            if self.r >= self.MAX_R:
                self.new_circle()

    def draw(self):
        pyxel.cls(0)
        if self.r > 0:
            pyxel.circ(self.x, self.y, self.r, 9)


App()
