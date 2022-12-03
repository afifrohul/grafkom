from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

w,h= 800,800

def rasiocanvas():
  glClearColor(0.0,0.0,0.9,1.0)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluOrtho2D(-4,13,-4,12)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()

def kepala(x,y):
  glBegin(GL_POLYGON)
  glColor3ub(0, 255, 0)
  glVertex2f((x + 4 + 7 )* 7, (y + 6.5 + 7 )* 7)
  glVertex2f((x + 4 + 7 )* 7, (y + 6 + 7 )* 7)
  glVertex2f((x + 7 + 7 )* 7, (y + 6 + 7 )* 7)
  glVertex2f((x + 7 + 7 )* 7, (y + 6.5 + 7 )* 7)
  glEnd()
  
  glBegin(GL_POLYGON)
  glColor3ub(0, 255, 0)
  glVertex2f((x + 4 + 7 )* 7, (y + 1 + 7 )* 7)
  glVertex2f((x + 4 + 7 )* 7, (y + 0.5 + 7 )* 7)
  glVertex2f((x + 7 + 7 )* 7, (y + 0.5 + 7 )* 7)
  glVertex2f((x + 7 + 7 )* 7, (y + 1 + 7 )* 7)
  glEnd()

  glBegin(GL_POLYGON)
  glColor3ub(0, 255, 0)
  glVertex2f((x + 3 + 7 )* 7, (y + 6 + 7 )* 7)
  glVertex2f((x + 3 + 7 )* 7, (y + 1 + 7 )* 7)
  glVertex2f((x + 8 + 7 )* 7, (y + 1 + 7 )* 7)
  glVertex2f((x + 8 + 7 )* 7, (y + 6 + 7 )* 7)
  glEnd()

def matakanan(x,y):
  glBegin(GL_POLYGON)
  glColor3ub(255, 255, 255)
  glVertex2f((x + 4 + 7 )* 7, (y + 6 -3 + 7 )* 7)
  glVertex2f((x + 4 + 7 )* 7, (y + 5 -3+ 7 )* 7)
  glVertex2f((x + 5 + 7 )* 7, (y + 5 -3+ 7 )* 7)
  glVertex2f((x + 5 + 7 )* 7, (y + 6 -3+ 7 )* 7)
  glEnd()

def pupilkanan(x,y):
  glBegin(GL_POLYGON)
  glColor3ub(0, 0, 0)
  glVertex2f((x + 4.6 + 7 )* 7, (y + 5.4 -3 + 7 )* 7)
  glVertex2f((x + 4.6 + 7 )* 7, (y + 5 -3 + 7 )* 7)
  glVertex2f((x + 5 + 7 )* 7, (y + 5  -3+ 7 )* 7)
  glVertex2f((x + 5 + 7 )* 7, (y + 5.4 -3+ 7 )* 7)
  glEnd()

def matakiri(x,y):
  glBegin(GL_POLYGON)
  glColor3ub(255, 255, 255)
  glVertex2f((x + 6 + 7 )* 7, (y + 6 -3+ 7 )* 7)
  glVertex2f((x + 6 + 7 )* 7, (y + 5 -3+ 7 )* 7)
  glVertex2f((x + 7 + 7 )* 7, (y + 5 -3+ 7 )* 7)
  glVertex2f((x + 7 + 7 )* 7, (y + 6 -3+ 7 )* 7)
  glEnd()

def pupilkiri(x,y):
  glBegin(GL_POLYGON)
  glColor3ub(0, 0, 0)
  glVertex2f((x + 6 + 7 )* 7, (y + 5.4 -3+ 7 )* 7)
  glVertex2f((x + 6 + 7 )* 7, (y + 5 -3+ 7 )* 7)
  glVertex2f((x + 6.4 + 7 )* 7, (y + 5 -3+ 7 )* 7)
  glVertex2f((x + 6.4 + 7 )* 7, (y + 5.4 -3+ 7 )* 7)
  glEnd()

def mulut(x,y):
  glBegin(GL_POLYGON)
  glColor3ub(255, 0, 0)
  glVertex2f((x + 5.5 + 7 )* 7, (y + 0.5 + 7 )* 7)
  glVertex2f((x + 5.5 + 7 )* 7, (y + 0 + 7 )* 7)
  glVertex2f((x + 6 + 7 )* 7, (y + 0 + 7 )* 7)
  glVertex2f((x + 6 + 7 )* 7, (y + 0.5 + 7 )* 7)
  glEnd()
  
  glBegin(GL_POLYGON)
  glColor3ub(255, 0, 0)
  glVertex2f((x + 5 + 7 )* 7, (y + 0 + 7 )* 7)
  glVertex2f((x + 5 + 7 )* 7, (y + -0.5 + 7 )* 7)
  glVertex2f((x + 5.5 + 7 )* 7, (y + -0.5 + 7 )* 7)
  glVertex2f((x + 5.5 + 7 )* 7, (y + 0 + 7 )* 7)
  glEnd()
  
  glBegin(GL_POLYGON)
  glColor3ub(255, 0, 0)
  glVertex2f((x + 4.5 + 7 )* 7, (y + -0.5 + 7 )* 7)
  glVertex2f((x + 4.5 + 7 )* 7, (y + -1 + 7 )* 7)
  glVertex2f((x + 5 + 7 )* 7, (y + -1 + 7 )* 7)
  glVertex2f((x + 5 + 7 )* 7, (y + -0.5 + 7 )* 7)
  glEnd()

# def iterate():
#   glViewport(0, 0, 500, 500)
#   glMatrixMode(GL_PROJECTION)
#   glLoadIdentity()
#   glOrtho(0.0, 1500, 0.0, 1500, 0.0, 1.0)
#   glMatrixMode (GL_MODELVIEW)
#   glLoadIdentity()

# def showScreen():
#   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#   glClearColor(0,0,0,1)
#   glLoadIdentity()
#   iterate()
#   glColor3d(255, 0, 0)
#   kepala()
#   matakanan()
#   pupilkanan()
#   matakiri()
#   pupilkiri()
#   mulut()
#   glutSwapBuffers()

def snake(x,y):
  glColor3d(255, 0, 0)
  kepala(x,y)
  matakanan(x,y)
  pupilkanan(x,y)
  matakiri(x,y)
  pupilkiri(x,y)
  mulut(x,y)
  
# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(750, 700)
# glutInitWindowPosition(0, 0)
# wind = glutCreateWindow("LOGO HMIF")
# glutDisplayFunc(showScreen)
# glutIdleFunc(showScreen)
# glutMainLoop()