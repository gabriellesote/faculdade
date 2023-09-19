import glfw

#inicialização da biblioteca glfw:
if not glfw.init():
    raise Exception("glfw can not be initialized")

#criação da janela
window = glfw.create_window(1200, 800, "Olá janela", None, None)

#confere se o a janela está aberta 
if not window:
    glfw.terminate()
    raise Exception("glfw can not be created")

#posiciona a janela na tela
glfw.set_window_pos(window, 400, 100)

#torna a janela atual como contexto de renderização especificada.( Isso significa que todas as operações de renderização subsequentes serão aplicadas a essa janela específica.)
glfw.make_context_current(window)

# o loop que continuará executando até que a função ´glfw.window_should_close(window)´ retorne True. Este Loop mantém a janela aberta.
while not glfw.window_should_close(window):
    glfw.poll_events()  #processa todos os eventos de entrada (movimentos do mouse, pressionamento de tecla, cliques)
    glfw.swap_buffers(window)  #  glfw.swap_buffers(window) Esta linha troca os buffers de frente e trás. Em muitas aplicações gráficas, é comum usar um "double-buffering", onde os desenhos são feitos em um buffer enquanto o outro é exibido na tela. Esta função troca os buffers, mostrando o que foi desenhado no buffer de trás na janela, e então você começa a desenhar no buffer de trás para a próxima iteração.

glfw.terminate()  # após sair do loop principal, essa função é chamada para liberar e limpar todos os recursos alocados pela GLFW. Isso é uma boa prática para garantir que tudo seja encerrado corretamente antes do término do programa.








"""
No geral, este código representa o ciclo principal de um aplicativo gráfico usando GLFW, onde ele processa os eventos de entrada, atualiza a interface gráfica e mantém o programa em execução até que o usuário decida fechar a janela. Quando a janela é fechada, ele termina a execução corretamente liberando os recursos da GLFW.
"""

