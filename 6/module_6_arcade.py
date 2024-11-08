import arcade

SCREEN_WIGHT = 400
SCREEN_HEIGHT = 300
SCREEN_TITLE = "Пин-понг"


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__("ball.png", 1.0)


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__("bar.png", 1.0)


class Game(arcade.Window):

    def __init__(self, wight, height, title):
        super().__init__(wight, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIGHT / 2
        self.bar.center_y = SCREEN_HEIGHT / 2
        self.ball.center_x = SCREEN_WIGHT / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()


if __name__ == "__main__":
    window = Game(SCREEN_WIGHT, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
