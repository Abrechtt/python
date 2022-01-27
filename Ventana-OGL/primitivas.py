#importar libreria

from ensurepip import version
from OpenGL.GL import *
from glew_wish import *
import glfw

#def draw():
    #glBegin(GL_TRIANGLES)
    #glColor3f(1,0,0)
    #glVertex3f(-1,0,0)

    #glColor3f(0,1,0)
    #glVertex3f(0,1,0)

    #glColor3f(0,0,1)
    #glVertex3f(0,0,1)

    #glEnd()


def draw_triangles():
    glBegin(GL_TRIANGLES)

    glColor3f(0.6,0.6,0)
    glVertex3f(-1,0,0)
    glColor3f(0,1,1)
    glVertex3f(0,1,0)
    glColor3f(1,0,1)
    glVertex3f(0.7,0.5,0)
    glEnd()

def draw_point():
    glBegin(GL_POINTS)
    glColor3f(1.0,1.0,1.0)
    glVertex(0,0,0)
    glColor3f(1.0,1.0,1.0)
    glVertex(-0.5,-0.5,0)
    glEnd()

def draw_lines():
    glBegin(GL_LINES)
    glColor3f(1.0,1.0,1.0)
    glVertex3f(0.2,-0.8,0.0)
    glVertex3f(0.8,-0.4,0.0)
    glEnd()

def draw_line_strip():
    glBegin(GL_LINE_STRIP)
    glColor3f(0.5,0.5,0.0)
    glVertex3f(0.7,-0.5,0.0)
    glVertex3f(0.9,-0.5,0.0)
    glVertex3f(0.7,-0.7,0.0)
    glVertex3f(0.9,-0.7,0.0)
    glEnd()

def draw_line_loop():
    glBegin(GL_LINE_LOOP)
    glColor3f(0.7,0.0,0.7)
    glVertex3f(-0.6,0.5,0.0)
    glVertex3f(-0.9,0.3,0.0)
    glVertex3f(-0.7,0.6,0.0)
    glEnd()

def draw_triangle_strip():
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(0.7,0.0,0.7)
    glVertex3f(-0.2,-0.8,0.0)
    glColor3f(0.6,0.6,0.0)
    glVertex3f(-0.6,-0.7,0.0)
    glColor3f(0.5,0.4,0.9)
    glVertex3f(-0.75,-0.3,0.0)
    glColor3f(0.0,0.7,0.7)
    glVertex3f(-0.9,-0.9,0.0)
    glEnd()

def draw_quads():
    glBegin(GL_QUADS)
    glColor3f(0.0,0.4,0.7)
    glVertex3f(-0.2,-0.2,0.0)
    glColor3f(0.5,0.4,0.9)
    glVertex3f(0.2,0.2,0.0)
    glColor3f(1.0,1.0,1.0)
    glVertex3f(0.2,-0.2,0.0)
    glColor3f(0.0,0.4,0.7)
    glVertex3f(-0.2,0.2,0.0)
    glEnd()

def draw_polygon():
    glBegin(GL_POLYGON)
    glColor3f(0.0,0.4,0.7)
    glVertex3f(0.0,0.0,1.0)
    glColor3f(0.8,0.4,0.9)
    glVertex3f(0.0,-0.4,0.0)
    glColor3f(-1.0,1.0,1.0)
    glVertex3f(1,-0.4,0.0)
    glColor3f(0.0,0.4,0.7)
    glVertex3f(1.0,-0.4,0.0)
    glColor3f(0.0,-0.4,0.7)
    glVertex3f(-0.3,0.1,0.0)
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
        draw_lines()
        #draw_line_strip()
        #draw_line_loop()
    

        #polling
        glfw.poll_events()

        #cambio buffers
        glfw.swap_buffers(window)
    
    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()