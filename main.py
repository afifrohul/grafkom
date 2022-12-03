import os.path
import random

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import snake

# from math import trunc
# from os import stat



posisi_ular = [0,0]
speed = 15
gerakAtas=True
gerakBawah=True
gerakKiri=True
gerakKanan=True

dotX = random.randint(-120, 120)
dotY = random.randint(-120, 120)

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
    if ((posisi_ular[0]<= kanan and posisi_ular[0]>= kiri)and (posisi_ular[1]<=atas and posisi_ular[1]>=bawah)):
        state='gameover'
    if score > high_score:
        scoreFile = open("high_score.txt", "w")
        scoreFile.write(str(score))
        scoreFile.close()
        # drawText('selamat! kamu mendapatkan score tertinggi', -200,-50,255,0.0)

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
    global posisi_ular
    global score
    global dotX
    global dotY 
    if food != None:
        food = None

    food = makanan(dotX, dotY)
    if ((posisi_ular[0]>=dotX-20 and posisi_ular[0]<=dotX+10) and (posisi_ular[1]<=dotY+10 and posisi_ular[1]>=dotY-20)):
        score += 1
        dotX = random.randint(-120, 120)
        dotY = random.randint(-120, 120)
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
        snake.gabung(posisi_ular[0],posisi_ular[1])
        bentuk()
        drawText('score'+ str(score), -200, -300, 255, 0, 255)
        drawText('high score'+ str(high_score), 100, -300, 255, 0, 255)
        new_food(food)
        game_over(400, -400, -400, -310)
        game_over(400, 310, -400, 400)
        game_over(400, -400, 310, 400)
        game_over(-310, -400, -400, 400)
    elif state=='gameover':
        drawText('GAME OVER !!', -100, 0, 255, 0, 0)
        drawText('Thank You', -80, -300, 21, 255, 0)

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
        posisi_ular[1]+=speed
    if key==GLUT_KEY_DOWN and gerakBawah:
        if gerakAtas==False:
            gerakAtas=True
        posisi_ular[1]-=speed
    if key==GLUT_KEY_LEFT and gerakKiri:
        if gerakKanan==False:
            gerakKanan=True
        posisi_ular[0]-=speed
    if key==GLUT_KEY_RIGHT and gerakKanan:
        if gerakKiri==False:
            gerakKiri=True
        posisi_ular[0]+=speed
    
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