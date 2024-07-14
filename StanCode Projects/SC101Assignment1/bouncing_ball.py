"""
File: bouncing_ball.py
Name: Zining Chen
-------------------------
The window opens with a ball at (START_X, START_Y) and the ball will fall down and bounce back after the user clicking
the mouse until it moves outside the width of the window.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3  # 球的水平速度
DELAY = 10  # 動畫停格多少毫秒(ms)
GRAVITY = 1  # 重力加速度;每一圈 while loop 垂直速度要加上的數值
SIZE = 20  # 球的直徑
REDUCE = 0.9  # 每一次反彈時,在垂直速度所剩之比例
START_X = 30  # 球的起始 x 座標
START_Y = 40  # 球的起始 y 座標
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
count = 1
window = GWindow(800, 500, title='bouncing_ball.py')
move = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces y velocity to REDUCE of itself.
    During this progress, any mouse click should not affect the movement of the ball.
    After clicked 3 times in total, there won't be any actions will be trigger by mouse click.
    """
    window.add(ball)
    onmouseclicked(bounce)


def bounce(mouse):
    global count, move
    if not move and count <= 3 and (mouse.x != START_X or mouse.y != START_Y):
        move = True
        vy = 0
        while True:
            if ball.x+SIZE < 800:
                vy += GRAVITY
                ball.move(VX, vy)
                pause(DELAY)
                if ball.y+SIZE > 500:
                    vy = -(vy*0.9)
                    ball.move(VX, vy)
                    pause(DELAY)
            else:
                window.add(ball, x=START_X, y=START_Y)
                move = False
                # To make sure the mouse click won't affect the ball's movement
                break
        count += 1
    else:
        pass


if __name__ == "__main__":
    main()
