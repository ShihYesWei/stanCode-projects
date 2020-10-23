"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

This function controls the animation of the game, based on the class from breakoutgraphics
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3  # How many lives to try


def main():
    """
    This function controls the animation of the game.
    :param graphics, is the object from the class BreakoutGraphics
    :param lives, how many more times can try
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    graphics.chances(lives)
    for i in range(NUM_LIVES):
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        while True:
            pause(FRAME_RATE)
            if graphics.start == 1:  # game start
                if 0 >= graphics.ball.x + dx or graphics.ball.x + dx >= graphics.window_width - 2 * graphics.ball_radius:
                    # bump into the left or right boundary of the window
                    dx = -dx
                if 0 >= graphics.ball.y + dy:  # bump into the upper window
                    dy = -dy
                graphics.ball.move(dx, dy)  # move the ball
                if graphics.check_collisions():  # Check whether the ball bump into any thing
                    dy = -dy
                if graphics.ball.y + dy >= graphics.window_height:  # The ball is out of window
                    graphics.remove_ball()
                    graphics.create_ball()
                    graphics.set_ball_init_velo()
                    graphics.start = 0
                    lives -= 1
                    graphics.chances(lives)
                    break
                if graphics.bricks_left == 0:
                    break
        if lives == 0:  # lose
            graphics.start = 0
            graphics.remove_ball()
            graphics.remove_paddle()
            graphics.remove_chances()
            graphics.you_lose()
            break
        if graphics.bricks_left == 0:  # win
            graphics.remove_ball()
            graphics.remove_paddle()
            graphics.start = 0
            graphics.you_win()
            break



if __name__ == '__main__':
    main()
