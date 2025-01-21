import pygame

from data.settings import Settings
from game.game_logic import GameLogic
from graphics.drawing import Drawing
from sound.audio import Audio
from ui.pause_menu import PauseMenu
from ui.score_table import ScoreTable


class GameProcessor:
    def __init__(self, main_menu, screen):
        self.main_menu = main_menu
        self.screen = screen
        self.game_logic = GameLogic()
        self.audio = Audio()
        self.settings = Settings()
        self.drawing = Drawing(screen)
        self.score_table = ScoreTable(screen)
        self.pause_menu = PauseMenu(screen, self)
        self.running = True

    def run(self):
        self.main_menu.running = False
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                        self.pause()

            self.drawing.draw_board(self.game_logic.board)
            # self.drawing.draw_shape(self.game_logic.current_shape, self.game_logic.current_shape_offset)
            self.drawing.draw_ui(self.game_logic.score, self.game_logic.level, self.game_logic.next_shape)

            self.screen.fill((0, 0, 0))  # Очистка экрана
            pygame.display.flip()
            clock.tick(60)

    def pause(self):
        self.pause_menu.run()
