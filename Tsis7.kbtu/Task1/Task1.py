import pygame
import sys
import time
import math

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# Загрузка изображений
clock_face = pygame.image.load("clock.png")  # Картинка циферблата
minute_hand = pygame.image.load("minute_hand.png")  # Минутная стрелка (правая рука)
second_hand = pygame.image.load("second_hand.png")  # Секундная стрелка (левая рука)

# Центр экрана
CENTER = (WIDTH // 2, HEIGHT // 2)

# Функция поворота и рисования стрелки
def draw_hand(image, angle, length):
    rotated_image = pygame.transform.rotate(image, -angle)  # Поворот изображения
    rect = rotated_image.get_rect(center=CENTER)
    screen.blit(rotated_image, rect.topleft)

# Основной цикл
running = True
while running:
    screen.fill((255, 255, 255))  # Фон белый

    # Получение текущего времени
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Углы поворота
    minute_angle = (minutes % 60) * 6  # 360° / 60 минут
    second_angle = (seconds % 60) * 6  # 360° / 60 секунд

    # Отрисовка часов
    screen.blit(clock_face, (0, 0))
    draw_hand(minute_hand, minute_angle, 100)
    draw_hand(second_hand, second_angle, 120)

    # Обновление экрана
    pygame.display.flip()

    # Обработка событий (выход)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Завершение программы
pygame.quit()
sys.exit()

