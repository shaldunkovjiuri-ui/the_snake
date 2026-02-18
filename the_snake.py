from random import choice, randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DEFAULT_POSITION = (0, 0)
SNAKE_START_POS = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

CHOICE_DIRECTION = {
    (LEFT, pygame.K_UP): UP,
    (RIGHT, pygame.K_UP): UP,
    (UP, pygame.K_LEFT): LEFT,
    (DOWN, pygame.K_LEFT): LEFT,
    (LEFT, pygame.K_DOWN): DOWN,
    (RIGHT, pygame.K_DOWN): DOWN,
    (UP, pygame.K_RIGHT): RIGHT,
    (DOWN, pygame.K_RIGHT): RIGHT,
}

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    """Родительский класс, описывающий игровые объекты."""

    def __init__(self) -> None:
        """Иницилизирует базовые атрибуты объекта."""
        self.position = None
        self.body_color = None

    def draw(self):
        """Метод для отрисовки объекта (переопределяется в подклассах)."""


class Apple(GameObject):
    """Класс, описывающий яблоко и поведение на игровом поле."""

    def __init__(self, snake_position=None):
        """Инициализирует яблоко, устанавливая цвет и случайную позицию."""
        super().__init__()
        self.position = DEFAULT_POSITION
        self.body_color = APPLE_COLOR

        if snake_position is None:
            snake_position = [SNAKE_START_POS]

        self.randomize_position(snake_position)

    def randomize_position(self, snake_position):
        """
        Устанавливает случайное положение яблока,
        убеждаясь, что оно не совпадает с телом змейки.
        """
        while True:
            position_x = randint(0, GRID_WIDTH - 1) * GRID_SIZE
            position_y = randint(0, GRID_HEIGHT - 1) * GRID_SIZE
            new_position = (position_x, position_y)
            if new_position not in snake_position:
                self.position = new_position
                break

    def draw(self):
        """Отрисовывает яблоко на игровой поверхности."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Класс, описывающий змейку и её поведение на игровом поле."""

    def __init__(self):
        """Инициализирует начальное состояние змейки."""
        super().__init__()
        self.length = 1
        self.direction = RIGHT
        self.next_direction = None
        self.body_color = SNAKE_COLOR
        self.positions = [(SNAKE_START_POS)]

    def get_head_position(self):
        """Возвращает позицию головы змейки."""
        return self.positions[0]

    def draw(self):
        """Отрисовывает змейку на экране, выделяя голову."""
        for position in self.positions[1:]:
            rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)
        head_rect = pygame.Rect(self.get_head_position(), (GRID_SIZE,
                                                           GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

    def move(self):
        """Обновляет позицию змейки."""
        head_snake_x, head_snake_y = self.get_head_position()
        direction_x, direction_y = self.direction

        new_x = (head_snake_x + direction_x * GRID_SIZE) % SCREEN_WIDTH
        new_y = (head_snake_y + direction_y * GRID_SIZE) % SCREEN_HEIGHT
        new_position = (new_x, new_y)

        self.positions.insert(0, new_position)
        if len(self.positions) > self.length:
            self.positions.pop()

    def reset(self):
        """Сбрасывает змейку в начальное состояние при столкновении."""
        self.length = 1
        self.positions = [SNAKE_START_POS]
        self.direction = choice([UP, DOWN, LEFT, RIGHT])
        screen.fill(BOARD_BACKGROUND_COLOR)

    def update_direction(self):
        """Обновляет направление движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None


def handle_keys(game_object):
    """Обрабатывает нажатия клавиш для управления змейкой."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            new_direction = CHOICE_DIRECTION.get((game_object.direction,
                                                  event.key))
            if new_direction:
                game_object.next_direction = new_direction


def main():
    """Основной цикл игры."""
    pygame.init()
    snake = Snake()
    apple = Apple(snake.positions)
    apple.randomize_position(snake.positions)
    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.update_direction()
        snake.move()
        head_snake = snake.get_head_position()
        if head_snake == apple.position:
            snake.length += 1
            apple.randomize_position(snake.positions)
        elif head_snake in snake.positions[1:]:
            snake.reset()
            apple.randomize_position(snake.positions)
        screen.fill(BOARD_BACKGROUND_COLOR)
        snake.draw()
        apple.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
