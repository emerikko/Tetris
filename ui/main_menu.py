import pygame


class MainMenu:
    def __init__(self, app):
        self.app = app
        self.font = pygame.font.Font(None, 36)
        self.running = False

    def run(self):
        self.running = True
        print('Main Menu is ready...')
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.app.audio.play_click_sound()
                    self.stop()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.app.audio.play_click_sound()
                        self.app.game_processor.run()
                    elif event.key == pygame.K_2:
                        self.app.audio.play_click_sound()
                        self.app.score_table.run()
                    elif event.key == pygame.K_3:
                        self.app.audio.play_click_sound()
                        self.stop()

            self.draw_menu()
            pygame.display.flip()

    def stop(self):
        self.running = False

    def draw_menu(self):
        self.app.screen.fill((0, 0, 0))

        # Рисуем текст меню
        menu_items = ["[1] Start New Game", "[2] Score Table", "[3] Exit"]
        for i, item in enumerate(menu_items):
            text = self.font.render(item, True, (255, 255, 255))
            text_rect = text.get_rect(center=(400, 200 + i * 50))
            self.app.screen.blit(text, text_rect)
