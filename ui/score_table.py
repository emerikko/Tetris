import pygame
from data.records import Records


class ScoreTable:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.records = Records()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.draw_table()
            pygame.display.flip()

    def draw_table(self):
        self.screen.fill((0, 0, 0))  # Чёрный фон

        # Рисуем заголовок
        title = self.font.render("Score Table", True, (255, 255, 255))
        title_rect = title.get_rect(center=(400, 50))
        self.screen.blit(title, title_rect)

        # Рисуем записи рекордов
        records = self.records.load_records()
        for i, record in enumerate(records):
            name, score = record
            text = self.font.render(f"{i+1}. {name}: {score}", True, (255, 255, 255))
            text_rect = text.get_rect(center=(400, 150 + i * 30))
            self.screen.blit(text, text_rect)