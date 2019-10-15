import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 680
SCREEN_TITLE = "Space"


class SpaceGame(arcade.Window):


    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        
    def setup(self):
        pass

    def update(self, dtime):
        pass

    def on_draw(dtime):
        arcade.start_render()


        arcade.draw_circle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 100, arcade.color.AMBER)





def main():
    """ Main method """
    game = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()