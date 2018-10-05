import pyxel
import random
import time
import math


class App:
    MAX_R = 10

    def new_circle(self):
        self.start = time.time()
        self.r = 0
        self.x = random.randint(self.MAX_R, pyxel.width - self.MAX_R)
        self.y = random.randint(self.MAX_R, pyxel.height - self.MAX_R)

    def is_in_circle(self, xx, yy):
        d = math.hypot(xx - self.x, yy - self.y)
        return d <= self.r

    def __init__(self):
        pyxel.init(160, 120, border_width=10, border_color=3)
        self.speed = 1
        self.score = 0
        self.lives = 3
        self.new_circle()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT_BUTTON):
            # print(pyxel.mouse_x, pyxel.mouse_y)
            if self.is_in_circle(pyxel.mouse_x, pyxel.mouse_y):
                self.score += (11 - self.r)
                self.new_circle()
                self.speed *= 0.9
        if time.time() - self.start > self.speed:
            self.r += 1
            self.start = time.time()
            if self.r >= self.MAX_R:
                self.new_circle()
                self.lives -= 1

    def draw(self):
        pyxel.cls(0)
        pyxel.text(0, 0, f"score {self.score:4d} speed {1/self.speed:.2f}", 3)
        for i in range(self.lives):
            pyxel.rect(120 + i * 5, 0, 122 + i * 5, 4, 8)
        if self.lives >= 0:
            if self.r > 0:
                pyxel.circ(self.x, self.y, self.r, 9)
        else:
            pyxel.text(50, 50, "GAME OVER", pyxel.frame_count % 16)


App()
