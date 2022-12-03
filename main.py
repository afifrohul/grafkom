import os.path
import random

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import snake_character
import snake_head2

snake_pos = [0,0]
speed = 15
# speed = 1
gerakAtas=True
gerakBawah=True
gerakKiri=True
gerakKanan=True

food_X = random.randint(-120, 120)
food_Y = random.randint(-120, 120)

state = 'start'
food = None
score = 0 
if (os.path.isfile("high_score.txt")):
        scoreFile = open("high_score.txt")
        high_score = int(scoreFile.read())
        scoreFile.close()
else:
        high_score = 0

#fungsi menggunakan objek kotak
def bentuk():

    glBegin(GL_QUADS)
    glColor3ub(255,0,0)
    glVertex2f(-400,400) #a
    glVertex2f(-400,-400) #b
    glVertex2f(-350,-400) #c
    glVertex2f(-350,400) #f
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(255,0,0)
    glVertex2f(-400, 400)
    glVertex2f(400, 400)
    glVertex2f(400, 350)
    glVertex2f(-400, 350)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(255,0,0)
    glVertex2f(350, 400)
    glVertex2f(400, 400)
    glVertex2f(400, -400)
    glVertex2f(350, -400)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(255,0,0)
    glVertex2f(400, -350)
    glVertex2f(400, -400)
    glVertex2f(-400, -400)
    glVertex2f(-400, -350)
    glEnd()

#fungsi untuk mengkonfigurasi tulisan yg berada pada akhir stage
def game_over(atas,bawah,kiri,kanan):
    global state
    global score
    global high_score
    if ((snake_pos[0]<= kanan and snake_pos[0]>= kiri)and (snake_pos[1]<=atas and snake_pos[1]>=bawah)):
        state='gameover'


#random makanan ular(tantangan)
def makanan(x,y):
    glBegin(GL_QUADS)
    glColor3ub(237,240,245)
    glVertex2f(x,y) #a
    glVertex2f(x,y-10) #b
    glVertex2f(x-10,y-10) #c
    glVertex2f(x-10,y) #d
    glEnd()

def new_food(food):
    global snake_pos
    global score
    global food_X
    global food_Y 
    if food != None:
        food = None

    food = makanan(food_X, food_Y)
    if ((snake_pos[0]>=food_X-20 and snake_pos[0]<=food_X+10) and (snake_pos[1]<=food_Y+10 and snake_pos[1]>=food_Y-20)):
    # if snake_pos[0]==food_X and snake_pos[1]==food_Y:
        score += 1
        food_X = random.randint(-120, 120)
        food_Y = random.randint(-120, 120)
        new_food(food)


#fungsi iterasi
def iterate():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-800/2, 800/2, -900/2,800/2)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

#Fungsi mengkonfigurasi Tulisan
def drawText(text,x,y,R,G,B):
    glPushMatrix()
    glColor3ub(R, G, B)
    glRasterPos2i(x,y)
    for i in str(text):
        c= ord(i)
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, c)
    glPopMatrix()

#fungsi memunculkan suatu object di sebuah layar
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #untuk membersihkan layar
    glLoadIdentity() #untuk mereset semua posisi grafik/bentuk
    iterate() #fungsi looping
    if state=='start':
        # snake_character.gabung(snake_pos[0],snake_pos[1])
        snake_head2.snake(snake_pos[0], snake_pos[1])
        bentuk()
        drawText('score '+ str(score), -200, -425, 255, 255, 255,)
        drawText('high score '+ str(high_score), 100, -425, 255, 255, 255,)
        new_food(food)
        game_over(400, -400, -400, -310)
        game_over(400, 310, -400, 400)
        game_over(400, -400, 310, 400)
        game_over(-310, -400, -400, 400)
        # if snake_pos[0] >= 55 or snake_pos[1] >= 55:
        #     state='gameover'

    elif state=='gameover':
        drawText('GAME OVER !!', -100, 0, 255, 0, 0)
        if score > high_score:
            drawText('Congratulation! YOU GET THE HIGHEST SCORE!. Your Final Score :' + str(score), -380, -300, 21, 255, 0)
        else:
            drawText('Your Final Score :' + str(score), -80, -300, 21, 255, 0)
        # drawText('Thank You', -80, -300, 21, 255, 0)

    glutSwapBuffers() #untuk membersihkan layar

#mengatur mengontrol gerakan
def controller(key,x,y):
    global gerakKanan
    global gerakKiri
    global gerakBawah
    global gerakAtas
    if key==GLUT_KEY_UP and gerakAtas:
        if gerakBawah==False:
            gerakBawah=True
        snake_pos[1]+=speed
        print(snake_pos)
        print(food_X)
        print(food_Y)
    if key==GLUT_KEY_DOWN and gerakBawah:
        if gerakAtas==False:
            gerakAtas=True
        snake_pos[1]-=speed
        print(snake_pos)
        print(food_X)
        print(food_Y)
    if key==GLUT_KEY_LEFT and gerakKiri:
        if gerakKanan==False:
            gerakKanan=True
        snake_pos[0]-=speed
        print(snake_pos)
        print(food_X)
        print(food_Y)
    if key==GLUT_KEY_RIGHT and gerakKanan:
        if gerakKiri==False:
            gerakKiri=True
        snake_pos[0]+=speed
        print(snake_pos)
        print(food_X)
        print(food_Y)
    
# inisialisasi
glutInit() #inisialisasi glut
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800,800)
glutInitWindowPosition(0,0)
wind = glutCreateWindow("Snake Game")
glutDisplayFunc(showScreen)
glutSpecialFunc(controller)
glutIdleFunc(showScreen)
glutMainLoop()