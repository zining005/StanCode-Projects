"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

File: breakout.py
Name: Zining Chen
----------------------
Draw a game that the user can use a ball, which will bounce in the widow and between the objects,
to remove the bricks on the top and catch the ball with the paddle.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    Start the loop to check if the user still have lives to play game. Then, when the ball is moving, start the loop to
    check if the ball touch any objects, or touch the end of the window. If the ball touch above conditions, it needs to
    bounce back in the opposite direction. The user will get the speed and direction for the ball by get it from the
    coder side. If the ball does not catch by the paddle, and fall down outside the window's height, the lives will
    minus 1. The whole game will stops when the user do not have lives or the user removes all the bricks in the
    window.
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    while True:
        # add pause in every while loop to prevent application crash
        pause(FRAME_RATE)
        # Check if user still has lives
        if 0 < lives <= 3:
            vx = graphics.get_dx()
            vy = graphics.get_dy()
            # When ball is moving, start the loop.
            if vx != 0 or vy != 0:
                # The game will stop when all the bricks are remove.
                if graphics.score_count == 0:
                    break
                while True:
                    # add pause in every while loop to prevent application crash
                    pause(FRAME_RATE)
                    # check if the ball touch the edge of the window
                    graphics.ball_touch_window()
                    # check if the ball touch any object and needs to bounce back or remove the bricks
                    graphics.bounce()
                    # get the new speed from the coder's side
                    vx = graphics.get_dx()
                    vy = graphics.get_dy()
                    # ball move according to the new speed
                    graphics.ball.move(vx, vy)
                    # To make sure the ball
                    graphics.touch = False
                    # If the ball fall down outside the window, the lives will minus 1.
                    if graphics.ball.y >= graphics.window.height:
                        lives -= 1
                        # If the user still have lives, the user can restart the game.
                        if lives > 0:
                            graphics.reset_ball()
                            break
                        # The game will end when the user does not have lives anymore.
                        elif lives == 0:
                            break


if __name__ == '__main__':
    main()
