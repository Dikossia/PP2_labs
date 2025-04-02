import pygame, random, sys, time
pygame.init()

# --- Настройки экрана и блоков ---
SCREEN_WIDTH, SCREEN_HEIGHT =600, 420
BLOCK_SIZE = 30
INITIAL_SPEED = 10

# --- Цвета ---
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

# --- Экран и шрифт ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка")
font = pygame.font.Font(None, 30)

# --- Функция отображения текста ---
def draw_text(text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# --- Генерация новой еды ---
def generate_food(snake_body):
    while True:
        x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        if (x, y) not in snake_body:
            value = random.randint(1, 3)  # Вес еды от 1 до 3
            timestamp = time.time()      # Время появления еды
            return {'pos': (x, y), 'value': value, 'created': timestamp}

# --- Отрисовка змейки и еды ---
def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

def draw_food(food):
    color = ORANGE if food['value'] == 1 else RED if food['value'] == 2 else (0, 200, 255)
    pygame.draw.rect(screen, color, (*food['pos'], BLOCK_SIZE, BLOCK_SIZE))

# --- Основная функция игры ---
def game():
    snake = [(90, 90)  , (60, 90), (30, 90)]
    direction = "RIGHT"
    food = generate_food(snake)
    score = 0
    level = 1
    speed = INITIAL_SPEED
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BLACK)

        # --- Управление направлением змейки ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        # --- Перемещение головы змейки ---
        head_x, head_y = snake[0]
        if direction == "UP": head_y -= BLOCK_SIZE
        elif direction == "DOWN": head_y += BLOCK_SIZE
        elif direction == "LEFT": head_x -= BLOCK_SIZE
        elif direction == "RIGHT": head_x += BLOCK_SIZE

        # --- Проверка на столкновения ---
        if (head_x < 0 or head_x >= SCREEN_WIDTH or
            head_y < 0 or head_y >= SCREEN_HEIGHT or
            (head_x, head_y) in snake):
            break  # Конец игры

        snake.insert(0, (head_x, head_y))

        # --- Съедена ли еда? ---
        if (head_x, head_y) == food['pos']:
            score += food['value']
            food = generate_food(snake)

            if score % 5 == 0:  # Каждые 5 очков — новый уровень
                level += 1
                speed += 2
        else:
            snake.pop()  # Удаляем хвост (если не съедено)

        # --- Проверка времени жизни еды ---
        if time.time() - food['created'] > 5:  # 5 секунд
            food = generate_food(snake)  # Удаляем старую и создаём новую

        # --- Отрисовка объектов ---
        draw_snake(snake)
        draw_food(food)
        draw_text(f"Счет: {score}", 10, 10)
        draw_text(f"Уровень: {level}", 500, 10)

        pygame.display.update()
        clock.tick(speed)

    # --- Завершение игры ---
    screen.fill(BLACK)
    draw_text("Вы проиграли!", SCREEN_WIDTH // 2 - 60, SCREEN_HEIGHT // 2 - 10, RED)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    sys.exit()

# --- Запуск игры ---
game()

