import pygame


class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    def draw_board(self, board):
        # Отрисовка игрового поля
        block_size = 30
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if cell:
                    color = (255, 0, 0)  # Красный цвет для заполненных клеток
                else:
                    color = (50, 50, 50)  # Серый цвет для пустых клеток
                pygame.draw.rect(self.screen, color,
                                 (x * block_size, y * block_size, block_size, block_size), 0)
    
    def draw_board_borders(self, board):
        # Отрисовка рамок поля
        block_size = 30

        # Горизонтальные линии
        for y in range(len(board)):
            pygame.draw.line(self.screen, (100, 100, 100),
                             (0, y * block_size),
                             (len(board[0]) * block_size, y * block_size), 2)

        # Вертикальные линии
        for x in range(len(board[0])):
            pygame.draw.line(self.screen, (100, 100, 100), (x * block_size, 0),
                             (x * block_size, len(board) * block_size), 2)

        # Границы поля
        pygame.draw.rect(self.screen, (200, 200, 200), (0, 0, len(board[0]) * block_size,
                                                        len(board) * block_size + 1), 2)

    def draw_shape(self, shape, offset):
        # Отрисовка активной фигуры на поле
        block_size = 30
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, (0, 255, 0),
                                     (x * block_size + offset[0] * block_size,
                                      y * block_size + offset[1] * block_size, block_size, block_size), 0)
    
    def draw_ui(self, score, level, next_shape):
        # Отрисовка интерфейса (очки, уровень, следующая фигура)
        score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        level_text = self.font.render(f"Level: {level}", True, (255, 255, 255))
        next_text = self.font.render("Next:", True, (255, 255, 255))
        screen_width = self.screen.get_width()
        text_width = max(score_text.get_width(), level_text.get_width(), next_text.get_width())
        self.screen.blit(score_text, (screen_width - text_width - 10, 10))
        self.screen.blit(level_text, (screen_width - text_width - 10, 40))
        self.screen.blit(next_text, (screen_width - text_width - 10, 70))

        # Отрисовка следующей фигуры
        block_size = 30
        for y, row in enumerate(next_shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, (0, 255, 0),
                                     (x * block_size + screen_width - text_width - 10,
                                      y * block_size + 100, block_size, block_size), 0)

        # Отрисовка рамок следующей фигуры
        pygame.draw.rect(self.screen, (200, 200, 200),
                         (screen_width - text_width - 10, 100, text_width, block_size * len(next_shape)), 1)
