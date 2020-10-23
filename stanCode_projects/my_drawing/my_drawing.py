"""
File: my_drawing
Author name: Alan Chen
----------------------
This program will draw a recently famous picture of Gian(技安), one of the main characters in doraemon(哆啦A夢).
This is a picture that originally Gian was scared by something. Here, I reassign the things that scared him is the
Illuminati symbol with a string of PYTHON.
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GPolygon, GArc
from campy.graphics.gwindow import GWindow

w = GWindow(1000, 650)


def main():
    """
    Draw a scared Gian.
    """
    '''
    #This is for adjusting the position 
    for i in range(0, 1000, 100):
        li = GLine(i, 0, i, 650)
        locatei = GLabel(str(i))
        w.add(li)
        w.add(locatei, i, 20)

    for j in range(0, 700, 100):
        lj = GLine(0, j, 1000, j)
        locatej = GLabel(str(j))
        w.add(lj)
        w.add(locatej, 0, j)
    '''
    #background
    bg = GPolygon()
    bg.add_vertex((666, 325))
    bg.add_vertex((0, 0))
    bg.add_vertex((0, 325))
    bg.filled = True
    bg.fill_color = 'red'
    bg.color = 'red'
    w.add(bg)

    bg = GPolygon()
    bg.add_vertex((666, 325))
    bg.add_vertex((0, 325))
    bg.add_vertex((0, 650))
    bg.filled = True
    bg.fill_color = 'orange'
    bg.color = 'orange'
    w.add(bg)

    bg = GPolygon()
    bg.add_vertex((666, 325))
    bg.add_vertex((333, 650))
    bg.add_vertex((0, 650))
    bg.filled = True
    bg.fill_color = 'lightgreen'
    bg.color = 'lightgreen'
    w.add(bg)

    bg = GPolygon()
    bg.add_vertex((666, 325))
    bg.add_vertex((333, 650))
    bg.add_vertex((666, 650))
    bg.filled = True
    bg.fill_color = 'slategrey'
    bg.color = 'slategrey'
    w.add(bg)

    bg = GPolygon()
    bg.add_vertex((666, 325))
    bg.add_vertex((1000, 650))
    bg.add_vertex((666, 650))
    bg.filled = True
    bg.fill_color = 'darkcyan'
    bg.color = 'darkcyan'
    w.add(bg)

    bg = GPolygon()
    bg.add_vertex((666, 325))
    bg.add_vertex((1000, 650))
    bg.add_vertex((1000, 400))
    bg.filled = True
    bg.fill_color = 'greenyellow'
    bg.color = 'greenyellow'
    w.add(bg)

    bg = GPolygon()
    bg.add_vertex((666, 325))
    bg.add_vertex((1000, 400))
    bg.add_vertex((1000, 200))
    bg.filled = True
    bg.fill_color = 'khaki'
    bg.color = 'khaki'
    w.add(bg)

    bg = GPolygon()
    bg.add_vertex((666, 325))
    bg.add_vertex((1000, 0))
    bg.add_vertex((1000, 200))
    bg.filled = True
    bg.fill_color = 'mistyrose'
    bg.color = 'mistyrose'
    w.add(bg)

    bg = GPolygon()
    bg.add_vertex((666, 325))
    bg.add_vertex((1000, 0))
    bg.add_vertex((666, 0))
    bg.filled = True
    bg.fill_color = 'plum'
    bg.color = 'plum'
    w.add(bg)

    bg = GPolygon()
    bg.add_vertex((666, 325))
    bg.add_vertex((350, 0))
    bg.add_vertex((666, 0))
    bg.filled = True
    bg.fill_color = 'magenta'
    bg.color = 'magenta'
    w.add(bg)

    bg = GPolygon()
    bg.add_vertex((666, 325))
    bg.add_vertex((350, 0))
    bg.add_vertex((0, 0))
    bg.filled = True
    bg.fill_color = 'tomato'
    bg.color = 'tomato'
    w.add(bg)



    #body
    body = GOval(900, 200)
    body.filled = True
    body.fill_color = 'Steelblue'
    body.color = 'blue'
    w.add(body, 220, 570)

    #face
    lower_face = GOval(530, 380)
    lower_face.filled = True
    lower_face.fill_color = 'Steelblue'
    lower_face.color = 'navy'
    w.add(lower_face, 405, 260)

    upper_face = GOval(485, 575)
    upper_face.filled = True
    upper_face.fill_color = 'Steelblue'
    upper_face.color = 'Steelblue'
    w.add(upper_face, 423, 40)

    shadow_on_face = GOval(420, 330)
    shadow_on_face.filled = True
    shadow_on_face.fill_color = 'Cadetblue'
    shadow_on_face.color = 'Cadetblue'
    w.add(shadow_on_face, 455, 230)

    shadow_on_face2 = GOval(390, 370)
    shadow_on_face2.filled = True
    shadow_on_face2.fill_color = 'Cadetblue'
    shadow_on_face2.color = 'Cadetblue'
    w.add(shadow_on_face2, 480, 170)

    # right_eye
    right_eye1 = GOval(90, 90)
    right_eye1.filled = True
    right_eye1.fill_color = 'powderblue'
    right_eye1.color = 'black'
    w.add(right_eye1, 525, 225)

    right_eye2 = GOval(45, 80)
    right_eye2.color = 'black'
    w.add(right_eye2, 546, 231)

    right_eye3 = GOval(30, 45)
    right_eye3.color = 'black'
    w.add(right_eye3, 552, 253)

    right_eye4 = GOval(5, 10)
    right_eye4.filled = True
    right_eye4.fill_color = 'black'
    right_eye4.color = 'black'
    w.add(right_eye4, 565, 271)

    # left_eye
    left_eye1 = GOval(90, 90)
    left_eye1.filled = True
    left_eye1.fill_color = 'powderblue'
    left_eye1.color = 'black'
    w.add(left_eye1, 710, 230)

    left_eye2 = GOval(60, 80)
    left_eye2.color = 'black'
    w.add(left_eye2, 725, 235)

    left_eye3 = GOval(25, 50)
    left_eye3.color = 'black'
    w.add(left_eye3, 740, 250)

    left_eye4 = GOval(5, 10)
    left_eye4.filled = True
    left_eye4.fill_color = 'black'
    left_eye4.color = 'black'
    w.add(left_eye4, 750, 270)

    # nose
    nose = GOval(80, 52)  # 610 351
    nose.filled = True
    nose.fill_color = 'DarkSeaGreen'
    nose.color = 'black'
    w.add(nose, 610, 347)

    # mouse
    for i in range(10):
        mouse = GOval(50, 80)
        mouse.filled = True
        mouse.fill_color = 'navy'
        mouse.color = 'navy'
        w.add(mouse, 560 + 4 * i, 430 - i)

    for i in range(100):
        mouse = GOval(50, 80)
        mouse.filled = True
        mouse.fill_color = 'navy'
        mouse.color = 'navy'
        w.add(mouse, 600 + i, 420)

    # tongue
    for i in range(15):
        tongue = GOval(50, 40)
        tongue.filled = True
        tongue.fill_color = 'mediumblue'
        tongue.color = 'mediumblue'
        w.add(tongue, 570 + 2 * i, 470 - i)

    for i in range(10):
        tongue = GOval(50, 45)
        tongue.filled = True
        tongue.fill_color = 'mediumblue'
        tongue.color = 'mediumblue'
        w.add(tongue, 600 + i, 455)

    for i in range(25):
        tongue = GOval(50, 30)
        tongue.filled = True
        tongue.fill_color = 'mediumblue'
        tongue.color = 'mediumblue'
        w.add(tongue, 600 + i, 475)

    for i in range(50):
        tongue = GOval(50, 45)
        tongue.filled = True
        tongue.fill_color = 'mediumblue'
        tongue.color = 'mediumblue'
        w.add(tongue, 650 + i, 455)

    # hair
    top_hair = GOval(330, 95)
    top_hair.filled = True
    top_hair.fill_color = 'navy'
    top_hair.color = 'navy'
    w.add(top_hair, 505, 25)

    bangs = GPolygon()
    bangs.add_vertex((510, 82))
    bangs.add_vertex((620, 82))
    bangs.add_vertex((560, 147))
    bangs.filled = True
    bangs.fill_color = 'navy'
    bangs.color = 'navy'
    w.add(bangs)

    bangs = GPolygon()
    bangs.add_vertex((580, 98))
    bangs.add_vertex((690, 98))
    bangs.add_vertex((635, 155))
    bangs.filled = True
    bangs.fill_color = 'navy'
    bangs.color = 'navy'
    w.add(bangs)

    bangs = GPolygon()
    bangs.add_vertex((650, 96))
    bangs.add_vertex((770, 96))
    bangs.add_vertex((710, 150))
    bangs.filled = True
    bangs.fill_color = 'navy'
    bangs.color = 'navy'
    w.add(bangs)

    bangs = GPolygon()
    bangs.add_vertex((740, 85))
    bangs.add_vertex((825, 85))
    bangs.add_vertex((780, 148))
    bangs.filled = True
    bangs.fill_color = 'navy'
    bangs.color = 'navy'
    w.add(bangs)

    for i in range(80):  # rightside
        side = GOval(40, 90)
        side.filled = True
        side.fill_color = 'navy'
        side.color = 'navy'
        w.add(side, 800 + i, 55 + i ** 1.2)

    for i in range(100):  # leftside
        side = GOval(40, 40)
        side.filled = True
        side.fill_color = 'navy'
        side.color = 'navy'
        w.add(side, 500 - i, 60 + i ** 1.2)

    # right_ear
    right_ear = GOval(70, 130)
    right_ear.filled = True
    right_ear.fill_color = 'Steelblue'
    right_ear.color = 'blue'
    w.add(right_ear, 395, 250)

    right_inear = GOval(50, 80)
    right_inear.filled = True
    right_inear.fill_color = 'royalblue'
    right_inear.color = 'blue'
    w.add(right_inear, 410, 290)

    # left_ear
    left_ear = GOval(70, 130)
    left_ear.filled = True
    left_ear.fill_color = 'Steelblue'
    left_ear.color = 'blue'
    w.add(left_ear, 880, 260)

    left_inear = GOval(50, 80)
    left_inear.filled = True
    left_inear.fill_color = 'royalblue'
    left_inear.color = 'blue'
    w.add(left_inear, 890, 290)

    # tears
    t1 = GOval(50, 25)
    t1.filled = True
    t1.fill_color = 'aqua'
    w.add(t1, 525, 300)

    t1 = GOval(50, 25)
    t1.filled = True
    t1.fill_color = 'aqua'
    w.add(t1, 750, 300)

    #left tears
    for i in range(0, 10, 2):
        tear = GOval(15, 50)
        tear.filled = True
        tear.fill_color = 'aqua'
        tear.color = 'aqua'
        w.add(tear, 525 - 2* i, 300 + 10 * i)

    for i in range(0, 10, 2):
        tear = GOval(21, 40)
        tear.filled = True
        tear.fill_color = 'aqua'
        tear.color = 'aqua'
        w.add(tear, 515 + i, 400 + 10 * i)

    for i in range(0, 10, 2):
        tear = GOval(18, 40)
        tear.filled = True
        tear.fill_color = 'aqua'
        tear.color = 'aqua'
        w.add(tear, 525, 500 + 10 * i)


    #right tears
    for i in range(0, 10, 2):
        tear = GOval(5, 50)
        tear.filled = True
        tear.fill_color = 'aqua'
        tear.color = 'aqua'
        w.add(tear, 790 + 2 * i, 300 + 10 * i)

    for i in range(0, 10, 2):
        tear = GOval(11, 40)
        tear.filled = True
        tear.fill_color = 'aqua'
        tear.color = 'aqua'
        w.add(tear, 808 - i, 410 + 10 * i)


    #lines
    line1 = GLine(525, 175, 575, 185)
    w.add(line1)

    line2 = GLine(575,185, 625, 270)
    w.add(line2)

    line3 = GLine(710, 255, 760, 170)
    w.add(line3)

    line4 = GLine(651, 400, 651, 420)
    w.add(line4)

    line5 = GLine(630, 520, 660, 520)
    w.add(line5)


    # Illuminati
    tri = GPolygon()
    tri.add_vertex((150, 20))
    tri.add_vertex((-20, 280))
    tri.add_vertex((320, 280))
    tri.filled = True
    tri.fill_color = 'green'
    w.add(tri)

    up_eye = GArc(200, 120, 0, 180)
    up_eye.filled = True
    up_eye.fill_color = 'darkgreen'
    w.add(up_eye, 50, 150)

    low_eye = GArc(200, 120, -12, -167)
    low_eye.filled = True
    low_eye.fill_color = 'darkgreen'
    low_eye.color = 'darkgreen'
    w.add(low_eye, 50, 145)

    eye_ball = GOval(55, 55)
    eye_ball.filled = True
    eye_ball.fill_color = 'black'
    w.add(eye_ball, 125, 150)

    py = GLabel('PYTHON')
    py.font = '-50'
    w.add(py, 20, 280)

if __name__ == '__main__':
    main()
