import os.path
import random
import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

snake_pos = [0,0]
speed = 15
# speed = 1
gerakAtas=True
gerakBawah=True
gerakKiri=True
gerakKanan=True

# gerakAtas=False
# gerakBawah=False
# gerakKiri=False
# gerakKanan=False

food_X = random.randint(-300, 300)
food_Y = random.randint(-300, 300)

food_2min_X = random.randint(-300, 300)
food_2min_Y = random.randint(-300, 300)

food_3min_X = random.randint(-300, 300)
food_3min_Y = random.randint(-300, 300)

sfood_X = random.randint(-300, 300)
sfood_Y = random.randint(-300, 300)

pois_X = random.randint(-300, 300)
pois_Y = random.randint(-300, 300)

state = 'start'
food = None
food_2min = None
food_3min = None
sfood = None
pois = None 
score = 0 
if (os.path.isfile("high_score.txt")):
        scoreFile = open("high_score.txt")
        high_score = int(scoreFile.read())
        scoreFile.close()
else:
        high_score = 0

#fungsi menggunakan objek kotak
def boundaries():
    glBegin(GL_QUADS)
    glColor3ub(255,0,0)
    glVertex2f(-400,400) #a
    glVertex2f(-400,-400) #b
    glVertex2f(-320,-400) #c
    glVertex2f(-320,400) #f
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(255,0,0)
    glVertex2f(-400, 400)
    glVertex2f(400, 400)
    glVertex2f(400, 330)
    glVertex2f(-400, 330)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(255,0,0)
    glVertex2f(320, 400)
    glVertex2f(400, 400)
    glVertex2f(400, -400)
    glVertex2f(320, -400)
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(255,0,0)
    glVertex2f(400, -330)
    glVertex2f(400, -400)
    glVertex2f(-400, -400)
    glVertex2f(-400, -330)
    glEnd()

def snake():
    glPushMatrix()
    glTranslated(snake_pos[0], snake_pos[1], 0)
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(-20, 20)
    glVertex2f(20, 20)
    glVertex2f(20, -20)
    glVertex2f(-20, -20)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(0, 255, 0)
    glVertex2f(-14, 14)
    glVertex2f(-14, -12)
    glVertex2f(14, -12)
    glVertex2f(14, 14)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3ub(0, 255, 0)
    glVertex2f(-10, 16)
    glVertex2f(-10, 14)
    glVertex2f(10, 14)
    glVertex2f(10, 16)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3ub(0, 255, 0)
    glVertex2f(-10, -12)
    glVertex2f(-10, -14)
    glVertex2f(10, -14)
    glVertex2f(10, -12)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2f(-10, 0)
    glVertex2f(-10, -8)
    glVertex2f(-2, -8)
    glVertex2f(-2, -0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(-6, -4)
    glVertex2f(-6, -8)
    glVertex2f(-2, -8)
    glVertex2f(-2, -4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2f(2, 0)
    glVertex2f(2, -8)
    glVertex2f(10, -8)
    glVertex2f(10, 0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(2, -4)
    glVertex2f(2, -8)
    glVertex2f(6, -8)
    glVertex2f(6, -4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0, -14)
    glVertex2f(0, -16)
    glVertex2f(2, -16)
    glVertex2f(2, -14)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(-2, -16)
    glVertex2f(-2, -18)
    glVertex2f(0, -18)
    glVertex2f(0, -16)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(-4, -18)
    glVertex2f(-4, -20)
    glVertex2f(-2, -20)
    glVertex2f(-2, -18)
    glEnd()

    glPopMatrix()

#random makanan ular(tantangan)
def makanan(x,y):
    glPushMatrix()
    glTranslated(x, y, 0)
    glBegin(GL_QUADS)
    glColor3ub(237,240,245)
    glVertex2f(-5, 5)
    glVertex2f(5, 5)
    glVertex2f(5, -5)
    glVertex2f(-5, -5)
    glEnd()
    glPopMatrix()

def new_food(food):
    global snake_pos, score, food_X, food_Y, sfood_X, sfood_Y, pois_X, pois_Y, food_2min_X, food_2min_Y, food_3min_X, food_3min_Y
    if food != None:
        food = None

    food = makanan(food_X, food_Y)
    if snake_pos[0] in range(int(food_X)-20, int(food_X)+20) and snake_pos[1] in range(int(food_Y)-20, int(food_Y)+20):
        score += 1
    
        food_X = random.randint(-300, 300)
        food_Y = random.randint(-300, 300)
        new_food(food)
        food_2min_X = random.randint(-300, 300)
        food_2min_Y = random.randint(-300, 300)
        new_2min_food(food_2min)
        food_3min_X = random.randint(-300, 300)
        food_3min_Y = random.randint(-300, 300)
        new_3min_food(food_3min)
        sfood_X = random.randint(-300, 300)
        sfood_Y = random.randint(-300, 300)
        new_special_food(sfood)
        pois_X = random.randint(-300, 300)
        pois_Y = random.randint(-300, 300)
        new_poison(pois)

def makanan_2min(x,y):
    glPushMatrix()
    glTranslated(x, y, 0)
    glBegin(GL_QUADS)
    glColor3ub(0,0,255)
    glVertex2f(-5, 5)
    glVertex2f(5, 5)
    glVertex2f(5, -5)
    glVertex2f(-5, -5)
    glEnd()
    glPopMatrix()

def new_2min_food(food_2min):
    global snake_pos, score, food_X, food_Y, sfood_X, sfood_Y, pois_X, pois_Y, food_2min_X, food_2min_Y, food_3min_X, food_3min_Y
    if food_2min != None:
        food_2min = None

    food_2min = makanan_2min(food_2min_X, food_2min_Y)
    if snake_pos[0] in range(int(food_2min_X)-20, int(food_2min_X)+20) and snake_pos[1] in range(int(food_2min_Y)-20, int(food_2min_Y)+20):
        score -= 2
    
        food_X = random.randint(-300, 300)
        food_Y = random.randint(-300, 300)
        new_food(food)
        food_2min_X = random.randint(-300, 300)
        food_2min_Y = random.randint(-300, 300)
        new_2min_food(food_2min)
        sfood_X = random.randint(-300, 300)
        sfood_Y = random.randint(-300, 300)
        new_special_food(sfood)
        pois_X = random.randint(-300, 300)
        pois_Y = random.randint(-300, 300)
        new_poison(pois)

def makanan_3min(x,y):
    glPushMatrix()
    glTranslated(x, y, 0)
    glBegin(GL_QUADS)
    glColor3ub(0,255,255)
    glVertex2f(-5, 5)
    glVertex2f(5, 5)
    glVertex2f(5, -5)
    glVertex2f(-5, -5)
    glEnd()
    glPopMatrix()

def new_3min_food(food_3min):
    global snake_pos, score, food_X, food_Y, sfood_X, sfood_Y, pois_X, pois_Y, food_2min_X, food_2min_Y, food_3min_X, food_3min_Y
    if food_3min != None:
        food_3min = None

    food_3min = makanan_3min(food_3min_X, food_3min_Y)
    if snake_pos[0] in range(int(food_3min_X)-20, int(food_3min_X)+20) and snake_pos[1] in range(int(food_3min_Y)-20, int(food_3min_Y)+20):
        score -= 3

        food_X = random.randint(-300, 300)
        food_Y = random.randint(-300, 300)
        new_food(food)
        food_2min_X = random.randint(-300, 300)
        food_2min_Y = random.randint(-300, 300)
        new_2min_food(food_2min)
        food_3min_X = random.randint(-300, 300)
        food_3min_Y = random.randint(-300, 300)
        new_3min_food(food_3min)
        sfood_X = random.randint(-300, 300)
        sfood_Y = random.randint(-300, 300)
        new_special_food(sfood)
        pois_X = random.randint(-300, 300)
        pois_Y = random.randint(-300, 300)
        new_poison(pois)

def makanan_special(x,y):
    glPushMatrix()
    glTranslated(x, y, 0)
    glBegin(GL_QUADS)
    glColor3ub(255,255,0)
    glVertex2f(-10, 10)
    glVertex2f(10, 10)
    glVertex2f(10, -10)
    glVertex2f(-10, -10)
    glEnd()
    glPopMatrix()

def new_special_food(sfood):
    global snake_pos, score, food_X, food_Y, sfood_X, sfood_Y, pois_X, pois_Y,food_2min_X, food_2min_Y, food_3min_X, food_3min_Y

    if sfood != None:
        sfood = None

    if score > 0 :
        sfood = makanan_special(sfood_X, sfood_Y)
        
        if snake_pos[0] in range(int(sfood_X)-20, int(sfood_X)+20) and snake_pos[1] in range(int(sfood_Y)-20, int(sfood_Y)+20):
            score += 3
        
            food_X = random.randint(-300, 300)
            food_Y = random.randint(-300, 300)
            new_food(food)
            food_2min_X = random.randint(-300, 300)
            food_2min_Y = random.randint(-300, 300)
            new_2min_food(food_2min)
            food_3min_X = random.randint(-300, 300)
            food_3min_Y = random.randint(-300, 300)
            new_3min_food(food_3min)
            sfood_X = random.randint(-300, 300)
            sfood_Y = random.randint(-300, 300)
            new_special_food(sfood)
            pois_X = random.randint(-300, 300)
            pois_Y = random.randint(-300, 200)
            new_poison(pois)
        
        # if snake_pos[0] not in range(int(sfood_X)-20, int(sfood_X)+20) and snake_pos[1] not in range(int(sfood_Y)-20, int(sfood_Y)+20):
        #     time.sleep(3)
        #     sfood_X = random.randint(-300,900)
        #     sfood_Y = random.randint(-300,900)

def racun(x,y):
    global snake_pos, score, food_X, food_Y, sfood_X, sfood_Y, pois_X, pois_Y,food_2min_X, food_2min_Y, food_3min_X, food_3min_Y
    glPushMatrix()
    glTranslated(x, y, 0)
    glBegin(GL_QUADS)
    glColor3ub(255, 0, 255)
    glVertex2f(-5, 5)
    glVertex2f(5, 5)
    glVertex2f(5, -5)
    glVertex2f(-5, -5)
    glEnd()
    glPopMatrix()
        
def new_poison(pois):
    global state, snake_pos, pois_X, pois_Y 
    if pois != None:
        pois = None
    
    pois = racun(pois_X, pois_Y)
    if snake_pos[0] in range(int(pois_X)-20, int(pois_X)+20) and snake_pos[1] in range(int(pois_Y)-20, int(pois_Y)+20):
        state = 'gameover'

def game_over(atas,bawah,kiri,kanan):
    global state, score, high_score
    if ((snake_pos[0]<= kanan and snake_pos[0]>= kiri)and (snake_pos[1]<=atas and snake_pos[1]>=bawah)):
        state='gameover'
    if score > high_score:
        scoreFile = open("high_score.txt", "w")
        scoreFile.write(str(score))
        scoreFile.close()


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
    glLoadIdentity() #untuk mereset semua posisi grafik/boundaries
    iterate() #fungsi looping
    if state=='start':
        boundaries()
        snake()
        new_food(food)
        new_poison(pois)
        if score > 4 :
            new_2min_food(food_2min)
        if score > 10 :
            new_3min_food(food_3min)
        if score % 7 == 0:
            new_special_food(sfood)
        drawText('score '+ str(score), -200, -425, 255, 255, 255,)
        drawText('high score '+ str(high_score), 100, -425, 255, 255, 255,)
        game_over(400, -400, -400, -310)
        game_over(400, 310, -400, 400)
        game_over(400, -400, 310, 400)
        game_over(-310, -400, -400, 400)
    elif state=='gameover':
        drawText('GAME OVER !!', -100, 0, 255, 0, 0)
        if score > high_score:
            drawText('Congratulation! YOU GET THE HIGHEST SCORE!. Your Final Score :' + str(score), -380, -300, 21, 255, 0)
        else:
            drawText('Your Final Score :' + str(score), -80, -300, 21, 255, 0)

    glutSwapBuffers() #untuk membersihkan layar

#mengatur mengontrol gerakan
def controller(key,x,y):
    global gerakKanan, gerakKiri, gerakBawah, gerakAtas
    if key==GLUT_KEY_UP and gerakAtas:
        if gerakBawah==False:
            gerakBawah=True
        snake_pos[1]+=speed
    if key==GLUT_KEY_DOWN and gerakBawah:
        if gerakAtas==False:
            gerakAtas=True
        snake_pos[1]-=speed
    if key==GLUT_KEY_LEFT and gerakKiri:
        if gerakKanan==False:
            gerakKanan=True
        snake_pos[0]-=speed
    if key==GLUT_KEY_RIGHT and gerakKanan:
        if gerakKiri==False:
            gerakKiri=True
        snake_pos[0]+=speed

    
        
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