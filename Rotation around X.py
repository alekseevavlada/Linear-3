from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

x0 = -1.0
y0 = -1.0
z0 = 1.0
rangle = 0.0


def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def any_cube(x0, y0, z0, hite):
    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(8.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(x0, y0, z0)  # 1
    glVertex3f(x0, y0 + hite, z0)  # 2
    glVertex3f(x0 + hite, y0 + hite, z0)  # 3
    glVertex3f(x0 + hite, y0, z0)  # 4
    glVertex3f(x0, y0, z0)  # 1
    glEnd()

    glBegin(GL_POINTS)
    glVertex3f(x0, y0, z0)  # 1
    glEnd()

    glBegin(GL_POINTS)
    glVertex3f(x0, y0 + hite, z0)  # 2
    glVertex3f(x0 + hite, y0 + hite, z0)  # 3
    glVertex3f(x0 + hite, y0, z0)  # 4
    glEnd()

    glBegin(GL_LINE_STRIP)
    glVertex3f(x0, y0, z0 - hite)  # 5
    glVertex3f(x0, y0 + hite, z0 - hite)  # 6
    glVertex3f(x0 + hite, y0 + hite, z0 - hite)  # 7
    glVertex3f(x0 + hite, y0, z0 - hite)  # 8
    glVertex3f(x0, y0, z0 - hite)  # 5
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(x0, y0 + hite, z0)  # 2
    glVertex3f(x0, y0 + hite, z0 - hite)  # 6
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(x0 + hite, y0 + hite, z0)  # 3
    glVertex3f(x0 + hite, y0 + hite, z0 - hite)  # 7
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(x0 + hite, y0, z0)  # 4
    glVertex3f(x0 + hite, y0, z0 - hite)  # 8
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(x0, y0, z0)  # 1
    glVertex3f(x0, y0, z0 - hite)  # 5
    glEnd()


def DrawGLScene():
    global rangle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    size = [1.0, 1.0, 1.0]
    location = [0.0, 0.0, -5.0]
    glLoadIdentity()
    glTranslatef(location[0], location[1], location[2])
    glScale(size[0], size[1], size[2])
    glRotatef(rangle * 0.4, 1.0, 0.0, 0.0)  # Rotate cube around X
    any_cube(-1.0, -1.0, 1.0, 2.0)

    rangle += 1.0
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Rotating around X")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    InitGL(1000, 1000)
    glutMainLoop()


main()