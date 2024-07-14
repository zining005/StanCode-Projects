"""
File: my_drawing.py
Name: Zining Chen
----------------------
Draw a Minion with it's favourite - banana in a sunny day to rememeber the concept "Object" in Python.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLine, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    Draw the Minion by separating the head, body, hands, legs...,etc by using GOval, GRect, GArc, GLine, and GPolygon.
    Then, use GOval and GPolygon to draw clouds and grass. Last but not least, use GArc to draw the banana.
    """
    window = GWindow(width=900, height=500, title='Minion')
    background1 = GRect(900, 500, x=0, y=350)
    background1.filled = True
    background1.fill_color = 'darkseagreen'
    background1.color = 'darkseagreen'
    window.add(background1)
    background2 = GRect(900, 350, x=0, y=0)
    background2.filled = True
    background2.fill_color = 'powderblue'
    background2.color = 'powderblue'
    window.add(background2)
    # clouds
    cloud1_1 = GOval(30, 20, x=100, y=50)
    cloud1_1.filled = True
    cloud1_1.fill_color = 'ghostwhite'
    cloud1_1.color = 'ghostwhite'
    window.add(cloud1_1)
    cloud1_2 = GOval(30, 20, x=110, y=55)
    cloud1_2.filled = True
    cloud1_2.fill_color = 'ghostwhite'
    cloud1_2.color = 'ghostwhite'
    window.add(cloud1_2)
    cloud1_3 = GOval(30, 20, x=120, y=45)
    cloud1_3.filled = True
    cloud1_3.fill_color = 'ghostwhite'
    cloud1_3.color = 'ghostwhite'
    window.add(cloud1_3)
    cloud1_4 = GOval(30, 20, x=130, y=60)
    cloud1_4.filled = True
    cloud1_4.fill_color = 'ghostwhite'
    cloud1_4.color = 'ghostwhite'
    window.add(cloud1_4)
    cloud1_5 = GOval(30, 20, x=90, y=65)
    cloud1_5.filled = True
    cloud1_5.fill_color = 'ghostwhite'
    cloud1_5.color = 'ghostwhite'
    window.add(cloud1_5)
    cloud1_6 = GOval(30, 20, x=115, y=70)
    cloud1_6.filled = True
    cloud1_6.fill_color = 'ghostwhite'
    cloud1_6.color = 'ghostwhite'
    window.add(cloud1_6)
    cloud2_1 = GOval(30, 20, x=600, y=100)
    cloud2_1.filled = True
    cloud2_1.fill_color = 'ghostwhite'
    cloud2_1.color = 'ghostwhite'
    window.add(cloud2_1)
    cloud2_2 = GOval(30, 20, x=610, y=105)
    cloud2_2.filled = True
    cloud2_2.fill_color = 'ghostwhite'
    cloud2_2.color = 'ghostwhite'
    window.add(cloud2_2)
    cloud2_3 = GOval(30, 20, x=620, y=95)
    cloud2_3.filled = True
    cloud2_3.fill_color = 'ghostwhite'
    cloud2_3.color = 'ghostwhite'
    window.add(cloud2_3)
    cloud2_4 = GOval(30, 20, x=630, y=110)
    cloud2_4.filled = True
    cloud2_4.fill_color = 'ghostwhite'
    cloud2_4.color = 'ghostwhite'
    window.add(cloud2_4)
    cloud2_5 = GOval(30, 20, x=590, y=115)
    cloud2_5.filled = True
    cloud2_5.fill_color = 'ghostwhite'
    cloud2_5.color = 'ghostwhite'
    window.add(cloud2_5)
    cloud2_6 = GOval(30, 20, x=615, y=120)
    cloud2_6.filled = True
    cloud2_6.fill_color = 'ghostwhite'
    cloud2_6.color = 'ghostwhite'
    window.add(cloud2_6)
    cloud3_1 = GOval(30, 20, x=750, y=30)
    cloud3_1.filled = True
    cloud3_1.fill_color = 'ghostwhite'
    cloud3_1.color = 'ghostwhite'
    window.add(cloud3_1)
    cloud3_2 = GOval(30, 20, x=760, y=35)
    cloud3_2.filled = True
    cloud3_2.fill_color = 'ghostwhite'
    cloud3_2.color = 'ghostwhite'
    window.add(cloud3_2)
    cloud3_3 = GOval(30, 20, x=770, y=25)
    cloud3_3.filled = True
    cloud3_3.fill_color = 'ghostwhite'
    cloud3_3.color = 'ghostwhite'
    window.add(cloud3_3)
    cloud3_4 = GOval(30, 20, x=780, y=40)
    cloud3_4.filled = True
    cloud3_4.fill_color = 'ghostwhite'
    cloud3_4.color = 'ghostwhite'
    window.add(cloud3_4)
    cloud3_5 = GOval(30, 20, x=740, y=45)
    cloud3_5.filled = True
    cloud3_5.fill_color = 'ghostwhite'
    cloud3_5.color = 'ghostwhite'
    window.add(cloud3_5)
    cloud3_6 = GOval(30, 20, x=765, y=50)
    cloud3_6.filled = True
    cloud3_6.fill_color = 'ghostwhite'
    cloud3_6.color = 'ghostwhite'
    window.add(cloud3_6)
    # grass
    grass1 = GPolygon()
    grass1.add_vertex((100, 350))
    grass1.add_vertex((120, 350))
    grass1.add_vertex((110, 310))
    grass1.filled = True
    grass1.fill_color = 'darkseagreen'
    grass1.color = 'darkseagreen'
    window.add(grass1)
    grass2 = GPolygon()
    grass2.add_vertex((110, 350))
    grass2.add_vertex((140, 350))
    grass2.add_vertex((125, 290))
    grass2.filled = True
    grass2.fill_color = 'darkseagreen'
    grass2.color = 'darkseagreen'
    window.add(grass2)
    grass3 = GPolygon()
    grass3.add_vertex((130, 350))
    grass3.add_vertex((150, 350))
    grass3.add_vertex((140, 310))
    grass3.filled = True
    grass3.fill_color = 'darkseagreen'
    grass3.color = 'darkseagreen'
    window.add(grass3)
    grass4 = GPolygon()
    grass4.add_vertex((150, 350))
    grass4.add_vertex((170, 350))
    grass4.add_vertex((160, 310))
    grass4.filled = True
    grass4.fill_color = 'darkseagreen'
    grass4.color = 'darkseagreen'
    window.add(grass4)
    grass5 = GPolygon()
    grass5.add_vertex((160, 350))
    grass5.add_vertex((190, 350))
    grass5.add_vertex((175, 290))
    grass5.filled = True
    grass5.fill_color = 'darkseagreen'
    grass5.color = 'darkseagreen'
    window.add(grass5)
    grass6 = GPolygon()
    grass6.add_vertex((180, 350))
    grass6.add_vertex((200, 350))
    grass6.add_vertex((190, 310))
    grass6.filled = True
    grass6.fill_color = 'darkseagreen'
    grass6.color = 'darkseagreen'
    window.add(grass6)
    grass7 = GPolygon()
    grass7.add_vertex((700, 350))
    grass7.add_vertex((720, 350))
    grass7.add_vertex((710, 310))
    grass7.filled = True
    grass7.fill_color = 'darkseagreen'
    grass7.color = 'darkseagreen'
    window.add(grass7)
    grass8 = GPolygon()
    grass8.add_vertex((710, 350))
    grass8.add_vertex((740, 350))
    grass8.add_vertex((725, 290))
    grass8.filled = True
    grass8.fill_color = 'darkseagreen'
    grass8.color = 'darkseagreen'
    window.add(grass8)
    grass9 = GPolygon()
    grass9.add_vertex((730, 350))
    grass9.add_vertex((750, 350))
    grass9.add_vertex((740, 310))
    grass9.filled = True
    grass9.fill_color = 'darkseagreen'
    grass9.color = 'darkseagreen'
    window.add(grass9)
    # Minion's head
    head = GArc(200, 400, 0, 180, x=350, y=110)
    head.filled = True
    head.fill_color = 'gold'
    head.color = 'gold'
    window.add(head)
    # Minion's left arm
    left_arm_1 = GArc(150, 80, 90, 180, x=330, y=260)
    left_arm_1.filled = True
    left_arm_1.fill_color = 'gold'
    left_arm_1.color = 'gold'
    window.add(left_arm_1)
    left_arm_2 = GArc(150, 40, 90, 180, x=342, y=280)
    left_arm_2.filled = True
    left_arm_2.fill_color = 'powderblue'
    left_arm_2.color = 'powderblue'
    window.add(left_arm_2)
    # Minion's right arm
    right_arm_1 = GArc(150, 80, 270, 180, x=495, y=260)
    right_arm_1.filled = True
    right_arm_1.fill_color = 'gold'
    right_arm_1.color = 'gold'
    window.add(right_arm_1)
    right_arm_2 = GArc(150, 40, 270, 180, x=483, y=280)
    right_arm_2.filled = True
    right_arm_2.fill_color = 'powderblue'
    right_arm_2.color = 'powderblue'
    window.add(right_arm_2)
    # Minion's face
    face = GRect(200, 100, x=350, y=200)
    face.filled = True
    face.fill_color = 'gold'
    face.color = 'gold'
    window.add(face)
    # Minion's lower body
    lower_body = GArc(200, 400, 180, 180, x=350, y=200)
    lower_body.filled = True
    lower_body.fill_color = 'steelblue'
    lower_body.color = 'steelblue'
    window.add(lower_body)
    # Minion's hair
    hair_1 = GLine(x0=420, y0=90, x1=440, y1=120)
    hair_2 = GLine(x0=455, y0=90, x1=455, y1=120)
    hair_3 = GLine(x0=480, y0=90, x1=460, y1=120)
    window.add(hair_1)
    window.add(hair_2)
    window.add(hair_3)
    # Minion's left bend
    l_eye_bend = GRect(32, 15, x=350, y=200)
    l_eye_bend.filled = True
    l_eye_bend.fill_color = 'black'
    l_eye_bend.color = 'black'
    window.add(l_eye_bend)
    # Minion's left eyeglass
    l_eye_glass = GOval(70, 70, x=380, y=175)
    l_eye_glass.filled = True
    l_eye_glass.fill_color = 'dimgrey'
    l_eye_glass.color = 'dimgrey'
    window.add(l_eye_glass)
    # Minion's left eye
    l_eye = GOval(50, 50, x=390, y=185)
    l_eye.filled = True
    l_eye.fill_color = 'white'
    l_eye.color = 'white'
    window.add(l_eye)
    l_inner_eye = GOval(20, 20, x=405, y=203)
    l_inner_eye.filled = True
    l_inner_eye.fill_color = 'sienna'
    l_inner_eye.color = 'sienna'
    window.add(l_inner_eye)
    l_eye_ball = GOval(15, 15, x=405, y=208)
    l_eye_ball.filled = True
    l_eye_ball.fill_color = 'black'
    l_eye_ball.color = 'black'
    window.add(l_eye_ball)
    l_white_eye_ball = GOval(5, 5, x=407, y=208)
    l_white_eye_ball.filled = True
    l_white_eye_ball.fill_color = 'white'
    l_white_eye_ball.color = 'white'
    window.add(l_white_eye_ball)
    # Minion's right bend
    r_eye_bend = GRect(32, 15, x=518, y=200)
    r_eye_bend.filled = True
    r_eye_bend.fill_color = 'black'
    r_eye_bend.color = 'black'
    window.add(r_eye_bend)
    # Minion's right eyeglass
    r_eye_glass = GOval(70, 70, x=450, y=175)
    r_eye_glass.filled = True
    r_eye_glass.fill_color = 'dimgrey'
    r_eye_glass.color = 'dimgrey'
    window.add(r_eye_glass)
    # Minion's right eye
    r_eye = GOval(50, 50, x=460, y=185)
    r_eye.filled = True
    r_eye.fill_color = 'white'
    r_eye.color = 'white'
    window.add(r_eye)
    r_inner_eye = GOval(20, 20, x=475, y=203)
    r_inner_eye.filled = True
    r_inner_eye.fill_color = 'sienna'
    r_inner_eye.color = 'sienna'
    window.add(r_inner_eye)
    r_eye_ball = GOval(15, 15, x=475, y=208)
    r_eye_ball.filled = True
    r_eye_ball.fill_color = 'black'
    r_eye_ball.color = 'black'
    window.add(r_eye_ball)
    r_white_eye_ball = GOval(5, 5, x=477, y=208)
    r_white_eye_ball.filled = True
    r_white_eye_ball.fill_color = 'white'
    r_white_eye_ball.color = 'white'
    window.add(r_white_eye_ball)
    # Minion's mouth
    mouth = GArc(25, 15, 180, 190, x=438, y=250)
    mouth.filled = True
    # mouth.fill_color = 'white'
    # mouth.color = 'white'
    window.add(mouth)
    # Minion's overalls left strap
    left_strap = GPolygon()
    left_strap.add_vertex((350, 245))
    left_strap.add_vertex((350, 260))
    left_strap.add_vertex((410, 295))
    left_strap.add_vertex((410, 280))
    left_strap.filled = True
    left_strap.fill_color = 'steelblue'
    left_strap.color = 'steelblue'
    window.add(left_strap)
    # Minion's overalls right strap
    right_strap = GPolygon()
    right_strap.add_vertex((550, 245))
    right_strap.add_vertex((550, 260))
    right_strap.add_vertex((490, 295))
    right_strap.add_vertex((490, 280))
    right_strap.filled = True
    right_strap.fill_color = 'steelblue'
    right_strap.color = 'steelblue'
    window.add(right_strap)
    # Minion's overalls
    overalls = GRect(110, 50, x=395, y=275)
    overalls.filled = True
    overalls.fill_color = 'steelblue'
    overalls.color = 'steelblue'
    window.add(overalls)
    # Minion's pocket
    pocket = GArc(70, 150, 180, 180, x=416, y=260)
    pocket.filled = True
    pocket.fill_color = 'white'
    pocket.color = 'white'
    window.add(pocket)
    # Minion's overalls' left button
    left_button = GOval(8, 8, x=390, y=274)
    left_button.filled = True
    window.add(left_button)
    # Minion's overalls' right button
    right_button = GOval(8, 8, x=500, y=275)
    right_button.filled = True
    window.add(right_button)
    # Minion's left leg
    left_leg = GRect(25, 20, x=425, y=385)
    left_leg.filled = True
    left_leg.fill_color = 'steelblue'
    left_leg.color = 'steelblue'
    window.add(left_leg)
    # Minion's right leg
    right_leg = GRect(25, 20, x=455, y=385)
    right_leg.filled = True
    right_leg.fill_color = 'steelblue'
    right_leg.color = 'steelblue'
    window.add(right_leg)
    # Minion's left shoe
    left_shoe_1 = GRect(25, 18, x=425, y=405)
    left_shoe_1.filled = True
    window.add(left_shoe_1)
    left_shoe_2 = GRect(25, 10, x=420, y=410)
    left_shoe_2.filled = True
    window.add(left_shoe_2)
    # Minion's right shoe
    right_shoe_1 = GRect(25, 18, x=455, y=405)
    right_shoe_1.filled = True
    window.add(right_shoe_1)
    right_shoe_2 = GRect(25, 10, x=460, y=410)
    right_shoe_2.filled = True
    window.add(right_shoe_2)
    # Minion's left sole
    left_sole = GArc(50, 18, 90, 180, x=412, y=405)
    left_sole.filled = True
    window.add(left_sole)
    # Minion's right sole
    right_sole = GArc(50, 18, 270, 180, x=468, y=405)
    right_sole.filled = True
    window.add(right_sole)
    # banana
    banana1 = GArc(100, 30, 220, 180, x=600, y=400)
    banana1.filled = True
    banana1.fill_color = 'gold'
    banana1.color = 'gold'
    window.add(banana1)
    banana2 = GArc(150, 20, 220, 180, x=550, y=402)
    banana2.filled = True
    banana2.fill_color = 'darkseagreen'
    banana2.color = 'darkseagreen'
    window.add(banana2)
    banana3 = GRect(10, 6, x=668, y=403)
    banana3.filled = True
    banana3.fill_color = 'sienna'
    banana3.color = 'sienna'
    window.add(banana3)


if __name__ == '__main__':
    main()
