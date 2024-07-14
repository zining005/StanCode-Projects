"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

File: breakoutgraphics.py
Name: Zining Chen
----------------------
Write the back around and basic move for the game. So when the user start to set the game's rules, the user can already
see that there will be bricks, a ball and a paddle in the window. And the objects will do the actions by the coder's
demand. So when the user write the code, the user only needs to set like the conditions to end the game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random


BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball
FRAME_RATE = 10

"""
In this game, the paddle will move along with the mouse. The bricks will show in the beginning of the game.The ball will
start moving when the users click mouse. The ball will move inside the window and will bounce back when it touch the 
edge of the window. However, if the ball is outside the window's width, it won't bounce back. The ball will also bounce
back when it touches any object, and will remove the objects if the objects are bricks.
"""


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.ball_radius = BALL_RADIUS
        self.brick_rows = BRICK_ROWS
        self.brick_cols = BRICK_COLS
        self.paddle_offset = PADDLE_OFFSET
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width) / 2,
                            y=window_height - paddle_offset)
        self.paddle.filled = 'True'
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=window_width / 2 - ball_radius,
                          y=window_height / 2 - ball_radius)
        self.window_width = window_width
        self.window_height = window_height
        self.ball.filled = 'True'
        self.window.add(self.ball)
        # create move to check if the ball is already moving or not
        self.move = False
        # create touch to make the ball won't keep bounce back and forward
        self.touch = False
        # create the initial speed
        self.__dx = 0
        self.__dy = 0
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        # Let the game start when the user click the mouse
        onmouseclicked(self.switch)
        # Let the paddle can move with the mouse
        onmousemoved(self.move_paddle)
        self.score_count = brick_rows * brick_cols
        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                # create red bricks
                if i < 2:
                    self.bricks.fill_color = 'red'
                    self.bricks.color = 'red'
                # create orange bricks
                if 2 <= i < 4:
                    self.bricks.fill_color = 'orange'
                    self.bricks.color = 'orange'
                # create yellow bricks
                if 4 <= i < 6:
                    self.bricks.fill_color = 'yellow'
                    self.bricks.color = 'yellow'
                # create green bricks
                if 6 <= i < 8:
                    self.bricks.fill_color = 'green'
                    self.bricks.color = 'green'
                # create blue bricks
                if 8 <= i < 10:
                    self.bricks.fill_color = 'blue'
                    self.bricks.color = 'blue'
                self.window.add(self.bricks, x=(brick_spacing + brick_width) * j, y=brick_offset + (brick_spacing +
                                                                                                    brick_height) * i)

    # create getter function for the user to count how many bricks in total
    def get_brick_rows(self):
        return self.brick_rows

    # create getter function for the user to count how many bricks in total
    def get_brick_cols(self):
        return self.brick_cols

    # Let the paddle can move with the mouse
    def move_paddle(self, mouse):
        if 0 < mouse.x < self.window.width:
            self.paddle.x = mouse.x - self.paddle.width / 2
        # minus half of the paddle's width to make sure the whole paddle will be inside the window even mouse.x<0
        elif mouse.x-self.paddle.width/2 < 0:
            self.paddle.x = 0
        elif mouse.x > self.window.width:
            # minus half of the paddle's width to make sure the whole paddle will be inside the window even mouse.x>0
            self.paddle.x = self.window.width-self.paddle.width

    # The ball will back to the initial position with initial speed
    def reset_ball(self):
        self.ball = GOval(self.ball_radius * 2, self.ball_radius * 2)
        self.ball.filled = 'True'
        self.__dx = 0
        self.__dy = 0
        self.window.add(self.ball, x=self.window_width / 2 - self.ball_radius,
                        y=self.window_height / 2 - self.ball_radius)
        # To make sure the ball won't start moving without user click the mouse.
        self.move = False

    # The game will start will the user click mouse. Need to get the mouse information from it as onmouseclick needs it.
    def switch(self, mouse):
        # When the ball is moving, mouse click action won't affect the speed of the ball.
        if not self.move:
            self.move = True
            self.set_ball_velocity()

    # Set the speed for the ball
    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED

    # Let the user can get the ball's speed for x from coder's side.
    def get_dx(self):
        return self.__dx

    # Let the user can get the ball's speed for y from coder's side.
    def get_dy(self):
        return self.__dy

    # To check if the ball touch the edge of the window
    def ball_touch_window(self):
        # Check window's left and right side
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = - self.__dx
        # Check window's upper side
        if self.ball.y <= 0:
            self.__dy = - self.__dy

    # Make the ball will bounce back when it touches the objects and remove the objects if the objects are bricks.
    def bounce(self):
        # To make sure the game won't keep enter this loop when it already touch one of the objects in the window.
        if not self.touch:
            # The upper left corner
            obj_1 = self.window.get_object_at(self.ball.x, self.ball.y)
            # The upper right corner
            obj_2 = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball_radius)
            # The lower left corner
            obj_3 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y)
            # The lower right corner
            obj_4 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y + 2 * self.ball_radius)
            # Use if and elif to make sure only one condition will execute
            if obj_1 is not None:
                if obj_1 is self.paddle:
                    self.touch = True
                    self.__dy = -self.__dy
                    # Prevent the ball will bounce back and forward in the paddle
                    self.ball.y = self.window_height - self.paddle_offset - self.paddle.height
                else:
                    # Cannot write self.bricks in this case cause self.bricks means the last brick that we created.
                    self.window.remove(obj_1)
                    self.score_count -= 1
                    self.touch = True
                    self.__dy = -self.__dy
            elif obj_2 is not None:
                if obj_2 is self.paddle:
                    self.touch = True
                    self.__dy = -self.__dy
                    self.ball.y = self.window_height - self.paddle_offset - self.paddle.height
                else:
                    self.window.remove(obj_2)
                    self.score_count -= 1
                    self.touch = True
                    self.__dy = -self.__dy
            elif obj_3 is not None:
                if obj_3 is self.paddle:
                    self.touch = True
                    self.__dy = -self.__dy
                    self.ball.y = self.window_height - self.paddle_offset - self.paddle.height
                else:
                    self.window.remove(obj_3)
                    self.score_count -= 1
                    self.touch = True
                    self.__dy = -self.__dy
            elif obj_4 is not None:
                if obj_4 is self.paddle:
                    self.touch = True
                    self.__dy = -self.__dy
                    self.ball.y = self.window_height - self.paddle_offset - self.paddle.height
                else:
                    self.window.remove(obj_4)
                    self.score_count -= 1
                    self.touch = True
                    self.__dy = -self.__dy
