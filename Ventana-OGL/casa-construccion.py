#importar libreria

from ensurepip import version
from OpenGL.GL import *
from glew_wish import *
import glfw
import math

def house():
    #muro 1
    glBegin(GL_QUADS)
    glColor3f(1,1,1)
    glVertex3f(0.9,0.3,0.0)
    glVertex3f(0.3,0.3,0.0)
    glVertex3f(0.3,-0.8,0.0)
    glVertex3f(0.9,-0.8,0.0)
    glEnd()

    #muro 2
    glBegin(GL_QUADS)
    glColor3f(1,1,1)
    glVertex3f(-0.1,-0.3,0.0)
    glVertex3f(0.4,-0.3,0.0)
    glVertex3f(0.4,-0.8,0.0)
    glVertex3f(-0.1,-0.8,0.0)
    glEnd()

    #ventana 1
    glBegin(GL_QUADS)
    glColor3f(0.2,1,1)
    glVertex3f(0.8,0.2,0.0)
    glVertex3f(0.4,0.2,0.0)
    glVertex3f(0.4,-0.7,0.0)
    glVertex3f(0.8,-0.7,0.0)
    glEnd()

    #techo
    glBegin(GL_TRIANGLES)
    glColor3f(0.8,0.8,0.8)
    glVertex3f(0.9,0.3,0.0)
    glVertex3f(0.6,0.4,0.0)
    glVertex3f(0.3,0.3,0.0)
    glEnd()

    #puerta
    glBegin(GL_QUADS)
    glColor3f(0.8,0.5,0.0)
    glVertex3f(0.0,-0.4,0.0)
    glVertex3f(0.3,-0.4,0.0)
    glVertex3f(0.3,-0.8,0.0)
    glVertex3f(0.0,-0.8,0.0)
    glEnd()

    #chapa
    glBegin(GL_POLYGON)
    glColor3f(0.6,0.8,0.8)
    for angulo in range(0,359,5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) +0.25, 0.02 * math.sin(angulo * math.pi / 180) + -0.6, 0)
    glEnd()


def sun():
    glBegin(GL_POLYGON)
    glColor3f(0.9,0.9,0.2)
    for angulo in range(0,359,5):
        glVertex3f(0.25 * math.cos(angulo * math.pi / 180) -1, 0.25 * math.sin(angulo * math.pi / 180) + 0.5, 0)
    glEnd()

def tree():
    glBegin(GL_POLYGON)
    glColor3f(0.6,0.7,0.2)
    for angulo in range(0,359,5):
        glVertex3f(0.3 * math.cos(angulo * math.pi / 180) -0.5, 0.3 * math.sin(angulo * math.pi / 180) + -0.2, 0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.1,0.4,0.8)
    glVertex3f(-0.6,-0.8,0.0)
    glVertex3f(-0.4,-0.8,0.0)
    glVertex3f(-0.4,-0.3,0.0)
    glVertex3f(-0.6,-0.3,0.0)

    glEnd()


def background():
    #sky
    glBegin(GL_QUADS)
    glColor3f(0.2,0.8,1.0)
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-0.7,0.0)
    glVertex3f(-1.0,-0.7,0.0)
    glEnd()

    #ground
    glBegin(GL_QUADS)
    glColor3f(0.6,0.3,0.3)
    glVertex3f(-1.0,-1.0,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(1.0,-0.7,0.0)
    glVertex3f(-1.0,-0.7,0.0)
    glEnd()

def main():

    width = 700
    height = 700

    #inicio

    if not glfw.init():
        return

    #declarar
    window = glfw.create_window(800, 600, "ventana", None, None)

    #configurar
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #verificar
    if not window:
        glfw.terminate()
        return

    #context
    glfw.make_context_current(window)
    glewExperimental = True

    #iniciar
    if glewInit() != GLEW_OK:
        print("ahi pa la otra")
        return
    
    version = glGetString(GL_VERSION)
    print(version)

    #draw
    while not glfw.window_should_close(window):
        #viewport
        glViewport(0,0,800,800)
        #color
        glClearColor(1,0,0,1)
        #Borrar
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #dibujo............
        #draw()

        background()
        house()
        sun()
        tree()

        #polling
        glfw.poll_events()

        #cambio buffers
        glfw.swap_buffers(window)
    
    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()