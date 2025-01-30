import pygame


class ScoreTable:
    def __init__(self, app):
        self.app = app
        self.font = pygame.font.Font(None, 36)
        self.running = False

    def run(self):
        self.running = True
        print('Score Table is running...')
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.app.audio.play_click_sound()
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.app.audio.play_click_sound()
                        self.running = False

            self.draw_table()
            pygame.display.flip()

    def stop(self):
        self.running = False

    def draw_table(self):
        self.app.screen.fill((0, 0, 0))  # Чёрный фон

        # Рисуем заголовок
        title = self.font.render("Score Table", True, (255, 255, 255))
        title_rect = title.get_rect(center=(400, 50))
        self.app.screen.blit(title, title_rect)

        # Рисуем записи рекордов
        records = self.app.records.load_records()
        for i, record in enumerate(records):
            level, score = record
            text = self.font.render(f"{i+1}. Level: {level}; Score: {score}", True, (255, 255, 255))
            text_rect = text.get_rect(center=(400, 150 + i * 30))
            self.app.screen.blit(text, text_rect)