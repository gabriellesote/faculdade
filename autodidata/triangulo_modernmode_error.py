import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np


vertex_src = """
# version 460

in vec3 a_position;
in vec3 a_color;
out vec3 v_color;
void main()
{
    gl_Position = vec4(a_position, 1.0);
    v_color = a_color;
}
"""

fragment_src = """
# version 460

in vec3 v_color;
out vec4 out_color;
void main()
{
    out_color = vec4(v_color, 1.0);
}
"""


if not glfw.init():
    raise Exception("glfw can not be initialized")

window = glfw.create_window(1200, 800, "Triângulo", None, None)

if not window:
    glfw.terminate()
    raise Exception("glfw can not be created")

glfw.set_window_pos(window, 400, 200)

glfw.make_context_current(window)

vertices = [-0.5, -0.5, 0.0,     #x,y,z -> lado esquerdo inferior
            0.5, -0.5, 0.0,     #x,y,z -> lado direito inferior
            0.0,  0.5, 0.0]     #x,y,z -> topo do triângulo

colors = [1.0, 0.0, 0.0,        # - red  (valores rgb)
          0.0, 1.0, 0.0,        # - green (valores rgb)
          0.0, 0.0, 1.0]        # - blue (valores rgb)

vertices = np.array(vertices, dtype=np.float32)
colors = np.array(colors, dtype=np.float32)

shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))
print("Shader de vértices compilado com sucesso!")

VBO = glGenBuffers(2)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, len(vertices)*4, vertices, GL_STATIC_DRAW)

position = glGetAttribLocation(shader,"a_position")
glEnableVertexAttribArray(position)
glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))



glUseProgram(shader)
glClearColor(0, 0.1, 0.1, 1)

while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)

    glDrawArrays(GL_TRIANGLES, 0, 3)

    glfw.swap_buffers(window)
glfw.terminate()