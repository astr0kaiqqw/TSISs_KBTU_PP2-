import pygame
import os

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Папка с музыкой (помести сюда свои файлы .mp3)
MUSIC_FOLDER = "music"
tracks = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]

# Проверка наличия треков
if not tracks:
    print("Нет mp3-файлов в папке 'music'. Добавьте треки и попробуйте снова.")
    pygame.quit()
    exit()

# Текущий трек
current_track = 0
pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, tracks[current_track]))

# Настройки экрана
WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

# Шрифты
font = pygame.font.Font(None, 36)

# Функция отображения текста
def draw_text(text, x, y):
    render = font.render(text, True, (0, 0, 0))
    screen.blit(render, (x, y))

# Основной цикл
running = True
while running:
    screen.fill((200, 200, 255))  # Голубой фон

    # Текущий трек
    draw_text(f"Playing: {tracks[current_track]}", 20, 50)
    draw_text("Controls:", 20, 100)
    draw_text("P - Play/Pause", 20, 130)
    draw_text("S - Stop", 20, 160)
    draw_text("N - Next Track", 20, 190)
    draw_text("B - Previous Track", 20, 220)
    pygame.display.flip()

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play / Pause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                    pygame.mixer.music.play()

            elif event.key == pygame.K_s:  # Stop
                pygame.mixer.music.stop()

            elif event.key == pygame.K_n:  # Next Track
                current_track = (current_track + 1) % len(tracks)
                pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, tracks[current_track]))
                pygame.mixer.music.play()

            elif event.key == pygame.K_b:  # Previous Track
                current_track = (current_track - 1) % len(tracks)
                pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, tracks[current_track]))
                pygame.mixer.music.play()

# Завершение программы
pygame.quit()

