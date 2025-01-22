import pygame

from data.settings import Settings
from game.game_logic import GameLogic
from graphics.drawing import Drawing
from sound.audio import Audio
from ui.pause_menu import PauseMenu, LoseMenu
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
        self.lose_menu = LoseMenu(screen, self)

    def run(self):
        self.running = True
        self.main_menu.running = False
        clock = pygame.time.Clock()

        ticks = 0
        move_down = False
        while self.running:
            ticks += 1

            if move_down or ticks % (50 // self.game_logic.level ** (1 / 2)) == 0:
                if not self.game_logic.move_down():
                    self.lose()

            self.game_logic.update()

            pygame.display.flip()
            self.screen.fill((0, 0, 0))  # Очистка экрана
            self.drawing.draw_board(self.game_logic.board)
            self.drawing.draw_shape(self.game_logic.current_shape,
                                    self.game_logic.current_shape_offset)
            self.drawing.draw_board_borders(self.game_logic.board)
            self.drawing.draw_ui(self.game_logic.score, self.game_logic.level,
                                 self.game_logic.next_shape)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                        self.pause()
                    elif event.key == (pygame.K_a or pygame.K_LEFT):
                        self.game_logic.move_shape(-1, 0)
                    elif event.key == (pygame.K_d or pygame.K_RIGHT):
                        self.game_logic.move_shape(1, 0)
                    elif event.key == (pygame.K_s or pygame.K_DOWN):
                        move_down = True
                    elif event.key == (pygame.K_w or pygame.K_UP):
                        self.game_logic.rotate_shape()
                elif event.type == pygame.KEYUP:
                    if event.key == (pygame.K_s or pygame.K_DOWN):
                        move_down = False

            clock.tick(100)

    def lose(self):
        self.running = False
        self.pause_menu.running = False
        self.lose_menu.run()

    def pause(self):
        self.pause_menu.run()
    
    def restart(self):
        self.game_logic = GameLogic()
        self.running = True
