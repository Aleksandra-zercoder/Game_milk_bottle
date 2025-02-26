import pygame
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Тир: Молочная бутылка")
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)

# --- Константы ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (245, 245, 220)
FPS = 60

BOTTLE_IMAGE_PATH = "milk-bottle.png"
CROSSHAIR_IMAGE_PATH = "crosshair.png"  # Файл с изображением прицела
SCALE_FACTOR = 0.3
GAME_TIME = 30

def play_game(screen, clock, bottle_img, crosshair_img):
    start_ticks = pygame.time.get_ticks()
    score = 0
    bottle_rect = bottle_img.get_rect(topleft=(100, 100))
    font = pygame.font.SysFont(None, 36)

    running = True
    while running:
        clock.tick(FPS)
        elapsed_sec = (pygame.time.get_ticks() - start_ticks) / 1000
        if elapsed_sec >= GAME_TIME:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if bottle_rect.collidepoint(mouse_pos):
                    score += 1
                    new_x = random.randint(0, SCREEN_WIDTH - bottle_rect.width)
                    new_y = random.randint(0, SCREEN_HEIGHT - bottle_rect.height)
                    bottle_rect.topleft = (new_x, new_y)

        screen.fill((30, 30, 30))

        screen.fill(BG_COLOR)
        screen.blit(bottle_img, bottle_rect.topleft)

        # Отрисовка счета и времени
        score_text = font.render("Score: " + str(score), True, (0, 0, 0))
        time_text = font.render("Time: " + str(max(0, int(GAME_TIME - elapsed_sec))), True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 50))

        # Отрисовка кастомного курсора
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Центрируем изображение прицела на позицию мыши
        crosshair_rect = crosshair_img.get_rect(center=(mouse_x, mouse_y))
        screen.blit(crosshair_img, crosshair_rect)


        # Отрисовка кастомного курсора
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Центрируем изображение прицела на позицию мыши
        crosshair_rect = crosshair_img.get_rect(center=(mouse_x, mouse_y))
        screen.blit(crosshair_img, crosshair_rect)

        pygame.display.flip()
    return score

def game_over_screen(screen, clock, score):
    font_large = pygame.font.SysFont(None, 48)
    font_small = pygame.font.SysFont(None, 36)
    while True:
        screen.fill(BG_COLOR)
        game_over_text = font_large.render("Time's up!", True, (200, 0, 0))
        score_text = font_large.render("Your score: " + str(score), True, (0, 0, 0))
        prompt_text = font_small.render("Press R to restart or Q to quit", True, (0, 0, 0))
        screen.blit(game_over_text, ((SCREEN_WIDTH - game_over_text.get_width()) // 2, SCREEN_HEIGHT // 2 - 100))
        screen.blit(score_text, ((SCREEN_WIDTH - score_text.get_width()) // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(prompt_text, ((SCREEN_WIDTH - prompt_text.get_width()) // 2, SCREEN_HEIGHT // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Тир: Молочная бутылка")
    clock = pygame.time.Clock()

    # Загрузка и масштабирование изображения бутылки
    bottle_img = pygame.image.load(BOTTLE_IMAGE_PATH).convert_alpha()
    orig_width, orig_height = bottle_img.get_size()
    bottle_img = pygame.transform.scale(bottle_img, (int(orig_width * SCALE_FACTOR), int(orig_height * SCALE_FACTOR)))

    # Загрузка курсора (прицела)
    crosshair_img = pygame.image.load(CROSSHAIR_IMAGE_PATH).convert_alpha()
    # Уменьшаем размер курсора: коэффициент уменьшения изменён с 0.5 на 0.2
    crosshair_scale = 0.2
    cross_orig_w, cross_orig_h = crosshair_img.get_size()
    crosshair_img = pygame.transform.scale(crosshair_img,(int(cross_orig_w * crosshair_scale), int(cross_orig_h * crosshair_scale)))

    # Скрываем стандартный курсор
    pygame.mouse.set_visible(False)

    while True:
        score = play_game(screen, clock, bottle_img, crosshair_img)
        restart = game_over_screen(screen, clock, score)
        if not restart:
            break

    pygame.quit()

if __name__ == "__main__":
    main()
