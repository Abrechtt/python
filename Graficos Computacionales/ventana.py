#importar libreria

from ensurepip import version
from OpenGL.GL import *
from glew_wish import *
import glfw


def draw():
    glBegin(GL_TRIANGLES)
    glColor3f(1,0,0)
    glVertex3f(-1,0,0)

    glColor3f(0,1,0)
    glVertex3f(0,1,0)

    glColor3f(0,0,1)
    glVertex3f(0,0,1)



    glEnd()




def main():
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
        draw()

        #polling
        glfw.poll_events()

        #cambio buffers
        glfw.swap_buffers(window)
    
    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()