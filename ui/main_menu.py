import pygame

from game.game_processor import GameProcessor
from ui.pause_menu import PauseMenu
from ui.score_table import ScoreTable


class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.run_game()
                    elif event.key == pygame.K_2:
                        self.show_score_table()
                    elif event.key == pygame.K_3:
                        running = False

            self.draw_menu()
            pygame.display.flip()

    def show_score_table(self):
        # Показ таблицы рекордов
        score_table = ScoreTable(self.screen)
        score_table.run()

    def run_game(self):
        # Запуск игры
        print("Starting new game...")
        processor = GameProcessor(None, None, None, None, None, None, None, None)


    def pause_game(self):
        # Пауза игры
        print("Pausing game...")
        pause_menu = PauseMenu(self.screen)
        pause_menu.run()

    def draw_menu(self):
        self.screen.fill((0, 0, 0))

        # Рисуем текст меню
        menu_items = ["[1] Start New Game", "[2] Score Table", "[3] Exit"]
        for i, item in enumerate(menu_items):
            text = self.font.render(item, True, (255, 255, 255))
            text_rect = text.get_rect(center=(400, 200 + i * 50))
            self.screen.blit(text, text_rect)
