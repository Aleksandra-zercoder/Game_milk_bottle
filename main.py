import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR
from game_cycle import game_loop

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Тир: Молочная бутылка")
    clock = pygame.time.Clock()

    # Запуск игрового цикла
    game_loop(screen, clock)

    pygame.quit()

if __name__ == "__main__":
    main()
