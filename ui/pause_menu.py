import pygame


class PauseMenu:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.font = pygame.font.Font(None, 36)
        self.running = False

    def run(self):
        self.game.running = False
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.resume_game()
                    elif event.key == pygame.K_2:
                        self.restart_game()
                    elif event.key == pygame.K_3:
                        self.return_to_main_menu()

            self.draw_menu()
            pygame.display.flip()

    def resume_game(self):
        # Возобновление игры
        print("Resuming game...")
        self.running = False
        self.game.running = True

    def restart_game(self):
        # Перезапуск игры
        print("Restarting game...")

    def return_to_main_menu(self):
        # Возврат в главное меню
        print("Returning to main menu...")
        self.running = False
        self.game.running = False

    def pause_game(self):
        # Пауза игры
        print("Pausing game...")
        self.run()

    def draw_menu(self):
        self.screen.fill((0, 0, 0))  # Чёрный фон

        # Рисуем текст меню
        menu_items = ["[1] Resume Game", "[2] Restart Game", "[3] Return to Main Menu"]
        for i, item in enumerate(menu_items):
            text = self.font.render(item, True, (255, 255, 255))
            text_rect = text.get_rect(center=(400, 200 + i * 50))
            self.screen.blit(text, text_rect)
