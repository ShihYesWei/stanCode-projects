"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This program provides a class: 'BreakoutGraphics' that draws the components of Breakout based on GObjects.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constants
BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks. ---
BRICK_COLS = 10  # Number of columns of bricks. |
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        """
        Create the basic objects for the game breakout including the ball, the paddle and the bricks.
        :param ball_radius: This controls the size of the ball.
        :param paddle_width: This controls the width of the paddle.
        :param paddle_height: This controls the height of the paddle.
        :param paddle_offset: This controls the distance of the paddle to the bottom of the window.
        :param brick_rows: This controls how many rows of bricks in the window.
        :param brick_cols: This controls how many columns of bricks in the window.
        :param brick_width: This controls the size of the brick in width.
        :param brick_height: This controls the size of the brick in height.
        :param brick_offset: This controls the distance of the top brick to the bottom of the window.
        :param brick_spacing: This controls the size of the space between bricks.
        :param title: the name of the game 'Breakout'
        """
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        self.ball_radius = ball_radius
        self.__dx = 0  # The movement of the ball in x axis
        self.__dy = 0  # The movement of the ball in y axis
        self.start = 0  # if start ==0: game pause; if start ==1: game start
        self.bricks_left = brick_cols * self.brick_rows  # The number of bricks while start

        # Create a graphical window, with some extra space.
        self.window_width = self.brick_cols * (self.brick_width + self.brick_spacing) - self.brick_spacing
        self.window_height = brick_offset + 3 * (
                self.brick_rows * (self.brick_height + self.brick_spacing) - self.brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(self.paddle_width, self.paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, (self.window_width - self.paddle_width) // 2,
                        self.window_height - self.paddle_height - self.paddle_offset)

        # Draw the bricks
        for i in range(self.brick_cols):
            for j in range(self.brick_rows):
                brick = GRect(self.brick_width, self.brick_height)
                brick.filled = True
                if j < self.brick_rows / 5:
                    brick.fill_color = 'red'
                elif self.brick_rows / 5 <= j < 2 * self.brick_rows / 5:
                    brick.fill_color = 'orange'
                elif 2 * self.brick_rows / 5 <= j < 3 * self.brick_rows / 5:
                    brick.fill_color = 'yellow'
                elif 3 * self.brick_rows / 5 <= j < 4 * self.brick_rows / 5:
                    brick.fill_color = 'green'
                elif 4 * self.brick_rows / 5 <= j < 5 * self.brick_rows / 5:
                    brick.fill_color = 'blue'
                self.window.add(brick, (self.brick_width + self.brick_spacing) * i,
                                (self.brick_height + self.brick_spacing) * j + self.brick_offset)

        # Center a filled ball in the graphical window, set the initial velocity of the ball,
        # and wait for a mouse click to start game.
        self.create_ball()
        self.set_ball_init_velo()
        onmouseclicked(self.start_click)

    def create_ball(self):
        """
        This function creates a ball in the middle of the window
        This is a filled, black ball.
        """
        self.ball = GOval(self.ball_radius * 2, self.ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, self.window_width // 2 - self.ball_radius,
                        self.window_height // 2 - self.ball_radius)

    def set_ball_init_velo(self):
        """
        This set the initial velocity for the ball.
        The y-velocity is a fixed as the constant: INITIAL_Y_SPEED
        The x-velocity is a random velocity from 1 to the constant: MAX_X_SPEED
        50% of chances that the x-velocity will become minus.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    def start_click(self, mouse):
        """
        Mouse click is the signal of the game start.
        The :param self.start will be set as 1 (game start)
        and will be waiting for mouse move.
        :param mouse: mouse click
        """
        self.start = 1
        self.remove_chances()
        onmousemoved(self.move_paddle)

    def move_paddle(self, mouse):
        """
        If the :param self.start is 1, as game started,
        The middle of the paddle will be the x position of the mouse.
        But the y position will be fixed.
        :param mouse: mouse click
        """
        if self.start == 1:
            if mouse.x < self.paddle_width // 2:
                self.paddle.x = 0
            elif mouse.x > self.window_width - self.paddle_width // 2:
                self.paddle.x = self.window_width - self.paddle_width
            else:
                self.paddle.x = mouse.x - self.paddle_width // 2

    def get_dx(self):
        """
        getter of the :param self.__dx
        :return: the value of self.__dx
        """
        return self.__dx

    def get_dy(self):
        """
        getter of the :param self.__dy
        :return: the value of self.__dy
        """
        return self.__dy

    def check_collisions(self):
        """
        This function will check whether the ball bump into anything and remove the brick or bounce by paddle.
        :param: which corner bumped into paddle, as the int(1, 2, 3, 4) will be
        (upper-left, upper-right, lower-right, lower-left).
        If the upper part of the ball bumped into the paddle, the y of the ball will be slightly shifted to the lower of
         the paddle (and this chance will end soon);
        If the lower part of the ball bumped into the paddled, the y of the ball will be slightly shifted to the upper
         of the paddle.
        :return: True if the ball bump into something.
        """
        which_corner = 1
        maybe_object = self.window.get_object_at(self.ball.x, self.ball.y)  # upper-left, 1
        if maybe_object is None:
            maybe_object = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y)  # upper-right, 2
            which_corner += 1
        if maybe_object is None:
            maybe_object = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y +
                                                     2 * self.ball_radius)  # lower-right 3
            which_corner += 2
        if maybe_object is None:
            maybe_object = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball_radius)  # lower-left 4
            which_corner += 3
        if maybe_object is not None and maybe_object is not self.paddle:
            self.window.remove(maybe_object)
            self.bricks_left -= 1
            return True
        elif maybe_object is not None and maybe_object is self.paddle:
            # 上半碰到就下去 下半碰到就上去
            if which_corner == 1 or which_corner == 2:
                self.ball.y = self.window_height - self.paddle_offset
            elif which_corner == 3 or which_corner == 4:
                self.ball.y = self.window_height - self.paddle_offset - self.paddle_height - 2 * self.ball_radius
            return True

    def remove_ball(self):
        """
        Remove the ball, when the ball is out of window or the game is end.
        """
        self.window.remove(self.ball)

    def remove_paddle(self):
        """
        Remove the paddle, when the game is end.
        """
        self.window.remove(self.paddle)

    def you_lose(self):
        """
        Show the message that you lose the game and how many bricks left.
        """
        lose = GLabel('You lose')
        bleft = GLabel(f'Bricks left: {self.bricks_left}')
        lose.font = str(int(-0.8 * self.brick_rows * self.brick_cols))
        bleft.font = str(int(-0.3 * self.brick_rows * self.brick_cols))
        self.window.add(lose, self.window_width // 2 - lose.width // 2,
                        self.window_height // 2 + lose.height // 2)
        self.window.add(bleft, self.window_width // 2 - bleft.width // 2,
                        self.window_height // 2 + lose.height)

    def you_win(self):
        """
        Show the message that you win the game.
        """
        win = GLabel('You win!')
        win2 = GLabel('You\'ve break all the bricks!')
        win.font = str(int(-0.8 * self.brick_rows * self.brick_cols))
        win2.font = str(int(-0.3 * self.brick_rows * self.brick_cols))
        self.window.add(win, self.window_width // 2 - win.width // 2,
                        self.window_height // 2 - win.height // 2)
        self.window.add(win2, self.window_width // 2 - win2.width // 2,
                        self.window_height // 2 + win.height)

    def chances(self, lives):
        """
        To show how many lives left and instruct click to start.
        :param lives: how many tries left
        """
        if lives > 1:
            self.cleft = GLabel(f' You have {lives} chances.')
        if lives == 1:
            self.cleft = GLabel(f' You\'ve got the last chance!')
        self.cleft.font = str(int(-0.3 * self.brick_rows * self.brick_cols))
        self.click_to_start = GLabel('Click to start')
        self.click_to_start.font = str(int(-0.5 * self.brick_rows * self.brick_cols))
        self.window.add(self.cleft, self.window_width // 2 - self.cleft.width // 2,
                        self.window_height // 2 - self.cleft.height // 2)
        self.window.add(self.click_to_start, self.window_width // 2 - self.click_to_start.width // 2,
                        self.window_height // 2 + self.click_to_start.height * 1.5)


    def remove_chances(self):
        """
        Remove the message of the chance left and instruction of click to start
        """
        self.window.remove(self.cleft)
        self.window.remove(self.click_to_start)
