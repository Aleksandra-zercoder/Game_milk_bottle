import pygame

# --- Константы ---

# Параметры окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Цвет фона (бежевый, например (245, 245, 220))
BG_COLOR = (245, 245, 220)

# Частота кадров
FPS = 60

# Параметры бутылки
BOTTLE_IMAGE_PATH = "milk-bottle.png"  # Убедитесь, что файл лежит рядом с main.py
BOTTLE_START_POS = (100, 100)  # Координаты вывода на экран
BOTTLE_SIZE = (75, 150)  # Ширина и высота


def main():
    pygame.init()

    # Создаём окно
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Тир: Молочная бутылка")
    clock = pygame.time.Clock()

    # Загружаем и масштабируем изображение бутылки
    bottle_img = pygame.image.load(BOTTLE_IMAGE_PATH).convert_alpha()
    bottle_img = pygame.transform.scale(bottle_img, BOTTLE_SIZE)

    running = True
    while running:
        clock.tick(FPS)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Отрисовка фона
        screen.fill(BG_COLOR)

        # Отрисовка бутылки
        screen.blit(bottle_img, BOTTLE_START_POS)

        # Обновление экрана
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
