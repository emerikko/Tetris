import pygame


class LoseMenu:
    def __init__(self, app):
        self.app = app
        self.font = pygame.font.Font(None, 36)
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.app.game_processor.stop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.app.audio.play_click_sound()
                        self.restart_game()
                    elif event.key == pygame.K_2:
                        self.app.audio.play_click_sound()
                        self.return_to_main_menu()

            self.draw_menu()
            pygame.display.flip()

    def stop(self):
        self.running = False

    def resume_game(self):
        # Возобновление игры
        self.stop()
        self.app.game_processor.run()

    def restart_game(self):
        # Перезапуск игры
        self.running = False
        self.app.game_processor.restart()
        self.app.game_processor.run()

    def return_to_main_menu(self):
        # Возврат в главное меню
        self.running = False
        self.app.game_processor.stop()
        self.app.main_menu.run()

    def draw_menu(self):
        self.app.screen.fill((0, 0, 0))  # Чёрный фон

        # Рисуем текст меню
        menu_items = ["[1] Restart Game", "[2] Return to Main Menu"]
        for i, item in enumerate(menu_items):
            text = self.font.render(item, True, (255, 255, 255))
            text_rect = text.get_rect(center=(400, 200 + i * 50))
            self.app.screen.blit(text, text_rect)


class PauseMenu(LoseMenu):

    def run(self):
        self.running = True
        while self.running:
            self.app.game_processor.stop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.app.stop()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.app.audio.play_click_sound()
                        self.resume_game()
                    elif event.key == pygame.K_2:
                        self.app.audio.play_click_sound()
                        self.restart_game()
                    elif event.key == pygame.K_3:
                        self.app.audio.play_click_sound()
                        self.return_to_main_menu()

            self.draw_menu()
            pygame.display.flip()

    def restart_game(self):
        # Перезапуск игры
        self.running = False
        self.app.game_processor.restart()

    def return_to_main_menu(self):
        # Возврат в главное меню
        self.stop()
        self.app.game_processor.stop()
        self.app.main_menu.run()

    def draw_menu(self):
        self.app.screen.fill((0, 0, 0))  # Чёрный фон

        # Рисуем текст меню
        menu_items = ["[1] Resume Game", "[2] Restart Game", "[3] Return to Main Menu"]
        for i, item in enumerate(menu_items):
            text = self.font.render(item, True, (255, 255, 255))
            text_rect = text.get_rect(center=(400, 200 + i * 50))
            self.app.screen.blit(text, text_rect)
