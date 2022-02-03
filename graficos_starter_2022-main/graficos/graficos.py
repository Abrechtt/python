#Comandos para librerías
#pip install pyopengl
#pip install glfw

#Importar librerias

from turtle import color, position
from OpenGL.GL import *
from glew_wish import *
import glfw
import math

color = [1.0, 0.0, 0.0]
position = [0.0, 0.0]
velocidad = 0.01


def key_callback(window, key, scancode, action, mods):
    #Escape cierra ventana
    global color
    global position
    global velocidad

    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, 1)
    if key == glfw.KEY_R and action == glfw.PRESS:
        color = [1.0, 0.0, 0.0]
    if key == glfw.KEY_G and action == glfw.PRESS:
        color = [0.0, 1.0, 0.0]
    if key == glfw.KEY_B and action == glfw.PRESS:
        color = [0.0, 0.0, 1.0]

    if key == glfw.KEY_W and (action == glfw.PRESS or glfw.REPEAT):
        position[1] = position[1] + velocidad
    if key == glfw.KEY_S and (action == glfw.PRESS or glfw.REPEAT):
        position[1] = position[1] - velocidad
    if key == glfw.KEY_A and (action == glfw.PRESS or glfw.REPEAT):
        position[0] = position[0] - velocidad
    if key == glfw.KEY_D and (action == glfw.PRESS or glfw.REPEAT):
        position[0] = position[0] + velocidad


def draw():
    global color
    global position

    glPushMatrix()
    glTranslatef(position[0], position[1], 0.0)
    glBegin(GL_TRIANGLES)

    #Establecer color
    glColor3f(color[0], color[1], color[2])

    #Manda vertices a dibujar
    glVertex3f(-0.08,-0.08,0)
    glVertex3f(0,0.08,0)
    glVertex3f(0.08,-0.08,0)

    glEnd()
    glPopMatrix()


def main():
    width = 700
    height = 700
    #Inicializar GLFW
    if not glfw.init():
        return

    #declarar ventana
    window = glfw.create_window(width, height, "Mi ventana", None, None)

    #Configuraciones de OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Verificamos la creacion de la ventana
    if not window:
        glfw.terminate()
        return

    #Establecer el contexto
    glfw.make_context_current(window)

    #Le dice a GLEW que si usaremos el GPU
    glewExperimental = True

    #Inicializar glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #imprimir version
    version = glGetString(GL_VERSION)
    print(version)

    glfw.set_key_callback(window, key_callback)

    #Draw loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        #glViewport(0,0,width,height)
        #Establecer color de borrado
        glClearColor(0.7,0.7,0.7,1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        draw()


        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()



    
    