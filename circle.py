import pyxel
import random
import time
import math


class App:
    MAX_R = 10
    RED = 8
    BLUE = 12
    ORANGE = 9
    WHITE = 7
    BROWN = 4

    def new_circle(self):
        self.start = time.time()
        self.r = 0
        self.x = random.randint(self.MAX_R, pyxel.width - self.MAX_R)
        self.y = random.randint(self.MAX_R, pyxel.height - self.MAX_R)
        n = random.randint(1, 10)
        if n == 1:
            self.colour = self.BLUE
        elif n == 2:
            self.colour = self.RED
        elif n == 3:
            self.colour = self.BROWN
            # self.r = self.MAX_R
            self.x = self.MAX_R
        else:
            self.colour = self.ORANGE

    def is_in_circle(self, xx, yy):
        d = math.hypot(xx - self.x, yy - self.y)
        return d <= self.r

    def begin(self):
        self.speed = 0.5
        self.score = 0
        self.lives = 5
        self.new_circle()

    def __init__(self):
        pyxel.init(160, 120)
        self.begin()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_LEFT_BUTTON):
            if self.lives < 0:
                self.begin()
            elif self.is_in_circle(pyxel.mouse_x, pyxel.mouse_y):
                if self.colour == self.BLUE:
                    self.colour = self.ORANGE
                elif self.colour == self.RED:
                    self.score -= 10
                    self.new_circle()
                elif self.colour == self.BROWN:
                    self.score += (pyxel.width - self.x) // 10
                    self.new_circle()
                    self.speed *= 0.9
                else:
                    self.score += (11 - self.r)
                    self.new_circle()
                    self.speed *= 0.9
        if time.time() - self.start > self.speed:
            if self.colour == self.BROWN:
                if self.r < self.MAX_R:
                    self.r += 0.1
                self.x += 2
                if self.x + self.r >= pyxel.width:
                    self.lives -= 1
                    self.new_circle()
            else:
                self.r += 1
                self.start = time.time()
                if self.r >= self.MAX_R:
                    if self.colour != self.RED:
                        self.lives -= 1
                    self.new_circle()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(0, 0, f"score {self.score:4d} speed {1/self.speed:.2f}", 3)
        for i in range(self.lives):
            pyxel.rect(120 + i * 5, 0, 122 + i * 5, 4, 8)
        if self.lives >= 0:
            if self.r > 0:
                pyxel.circ(self.x, self.y, self.r, self.colour)
        else:
            pyxel.text(50, 50, "GAME OVER", pyxel.frame_count % 16)
            pyxel.text(70, 70, "Click to restart", self.WHITE)


App()
