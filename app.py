import pygame
import numpy as np
import time

# Inicializar pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Establecer dimensiones de la ventana
WIDTH, HEIGHT = 500, 500

# Crear ventana y reloj
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulación de Perinola")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 74)

acciones = ["Pon 1", "Pon 2", "Toma 1", "Toma 2", "Toma todo", "Todos ponen"]

def mostrar_resultado(resultado):
    text = font.render(resultado, True, BLACK)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.fill(WHITE)
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(2)

def main():
    run = True
    while run:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                resultado = np.random.choice(acciones)
                mostrar_resultado(resultado)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

