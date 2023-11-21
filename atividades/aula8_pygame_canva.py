import pygame
import pygame_gui
from pygame.locals import *
from PIL import Image

# Inicialize o Pygame
pygame.init()

# Configurações da tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Paint App')

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
brush_color = BLACK
eraser_color = WHITE  # Adicione a cor da borracha
using_eraser = False  # Variável para rastrear se a borracha está ativa

# Lista de cores disponíveis
color_list = [RED, GREEN, BLUE, YELLOW]

# Configuração do pincel
brush_size = 5
eraser_size = 5
drawing = False
last_pos = None

# Superfície para desenho
canvas = pygame.Surface((width, height))
canvas.fill(WHITE)

# Configuração da fonte
font = pygame.font.Font(None, 36)

# Configuração dos botões de cores
button_width = 50
button_height = 30
button_margin = 10
button_y = height - button_height - button_margin

buttons = []
for i, color in enumerate(color_list):
    button_x = i * (button_width + button_margin) + button_margin
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    buttons.append({'rect': button_rect, 'color': color})

# Configuração do gerenciador de interface gráfica
gui_manager = pygame_gui.UIManager((width, height))

# Configuração dos botões de tamanho do pincel
button_size_increase_rect = pygame.Rect(width - 100, height - 40, 50, 30)
button_size_decrease_rect = pygame.Rect(width - 160, height - 40, 50, 30)

# Configuração do indicador da largura do pincel
brush_width_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(width - 250, height - 40, 80, 30),
                                                 text=f"Size: {brush_size}",
                                                 manager=gui_manager,
                                                 container=None)

running = True
while running:
    time_delta = pygame.time.Clock().tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
            last_pos = event.pos
            # Verificar se um botão de cor foi pressionado
            for button in buttons:
                if button['rect'].collidepoint(event.pos):
                    brush_color = button['color']
                    using_eraser = False  # Desativa a borracha ao selecionar uma cor
            # Verificar se um botão de tamanho do pincel foi pressionado
            if button_size_increase_rect.collidepoint(event.pos):
                if using_eraser:
                    eraser_size = min(10, eraser_size + 1)
                else:
                    brush_size = min(10, brush_size + 1)
            elif button_size_decrease_rect.collidepoint(event.pos):
                if using_eraser:
                    eraser_size = max(1, eraser_size - 1)
                else:
                    brush_size = max(1, brush_size - 1)

        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                last_pos = None
        elif event.type == MOUSEMOTION:
            if drawing:
                mouse_x, mouse_y = event.pos
                if last_pos:
                    if using_eraser:
                        pygame.draw.line(canvas, eraser_color, last_pos, (mouse_x, mouse_y), eraser_size)
                    else:
                        pygame.draw.line(canvas, brush_color, last_pos, (mouse_x, mouse_y), brush_size)
                last_pos = (mouse_x, mouse_y)
        elif event.type == KEYDOWN:
            if event.key == K_b:
                # Alternar entre a borracha e o pincel ao pressionar o botão B
                using_eraser = not using_eraser

        # Processar eventos da interface gráfica
        gui_manager.process_events(event)

    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))

    # Adicione instruções na tela
    instructions_text = "Aperte B para apagar o desenho"
    text_surface = font.render(instructions_text, True, BLACK)
    screen.blit(text_surface, (10, 10))

    # Desenha os botões de cores na tela
    for button in buttons:
        pygame.draw.rect(screen, button['color'], button['rect'])

    # Desenha os botões de tamanho do pincel na tela
    pygame.draw.rect(screen, (200, 200, 200), button_size_increase_rect)
    pygame.draw.rect(screen, (200, 200, 200), button_size_decrease_rect)
    plus_text = font.render("+", True, BLACK)
    minus_text = font.render("-", True, BLACK)
    screen.blit(plus_text, (width - 75, height - 35))
    screen.blit(minus_text, (width - 135, height - 35))

    # Atualiza a interface gráfica
    gui_manager.update(time_delta)
    gui_manager.draw_ui(screen)

    # Atualiza o indicador da largura do pincel
    brush_width_label.set_text(f"Size: {brush_size}")

    pygame.display.flip()

# Salvar a imagem desenhada com o Pillow
image = pygame.surfarray.array3d(canvas)
image = Image.fromarray(image)
image.save('drawing.png')

pygame.quit()
