import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, - 1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)


class OGl():
    def three_func(a, b, func):
        return func(a[0], b[0]), func(a[1], b[1]), func(a[2], b[2])


class GLCamera():
    def __init__(self):
        self.pos = [0.0, 0.0, 10.0]
        self.rot = [0.0, 0.0, 0.0]
        self.rotating = False
        self.mouse_pos = [0, 0]

    def add_to_scene(self):
        glRotatef(self.rot[2], 0, 0, 1)
        glRotatef(self.rot[1], 0, 1, 0)
        glRotatef(self.rot[0], 1, 0, 0)
        glTranslatef(-self.pos[0], -self.pos[1], -self.pos[2])

    def change_of_basis(self):
        rx, ry, rz = [self.rot[i] * np.pi / 180 for i in range(3)]
        s, c = np.sin(rx), np.cos(rx)
        mx = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
        s, c = np.sin(ry), np.cos(ry)
        my = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
        s, c = np.sin(rz), np.cos(rz)
        mz = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
        m = my @ mx @ mz
        inv_m = np.linalg.inv(m)
        return inv_m

    def handle_camera_events(self, event):
        if event.type == pygame.KEYDOWN:
            cb = self.change_of_basis()
            if event.key == pygame.K_f:
                m = cb.dot(np.array([0, 0, -0.5]))
                self.pos = OGl.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_g:
                m = cb.dot(np.array([0, 0, 0.5]))
                self.pos = OGl.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_LEFT:
                m = cb.dot(np.array([-0.5, 0, 0]))
                self.pos = OGl.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_RIGHT:
                m = cb.dot(np.array([0.5, 0, 0]))
                self.pos = OGl.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_DOWN:
                m = cb.dot(np.array([0, -0.5, 0]))
                self.pos = OGl.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_UP:
                m = cb.dot(np.array([0, 0.5, 0]))
                self.pos = OGl.three_func(self.pos, m, lambda x, y: x + y)

        if event.type == pygame.MOUSEMOTION and self.rotating:
            tmp_pos = pygame.mouse.get_pos()
            x, y = self.mouse_pos[0] - tmp_pos[0], self.mouse_pos[1] - tmp_pos[1]
            if x != 0 or y != 0:
                self.rot[1] = (self.rot[1] + x)
                self.rot[0] = (self.rot[0] + y)
                self.mouse_pos = tmp_pos

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not self.rotating:
                self.rotating = True
                self.mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.rotating = False


def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_caption('Moving Cube')
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    camera = GLCamera()

    while True:
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        camera.add_to_scene()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            camera.handle_camera_events(event)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
