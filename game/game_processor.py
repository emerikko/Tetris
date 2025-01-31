import pygame

from game.game_logic import GameLogic
from game import drawing


class GameProcessor:
    def __init__(self, app):
        self.app = app
        self.drawing = drawing.Drawing(self.app.screen)
        self.game_logic = GameLogic(self.app.audio)
        self.running = False

    def run(self):
        self.running = True
        self.app.audio.play_background_music()
        clock = pygame.time.Clock()

        ticks = 0
        move_down = False
        while self.running:
            ticks += 1

            if move_down or ticks % (50 // self.game_logic.level ** (1 / 4)) == 0:
                if not self.game_logic.move_down():
                    self.lose()

            self.game_logic.update()

            pygame.display.flip()
            self.app.screen.fill((0, 0, 0))  # Очистка экрана
            self.drawing.draw_board(self.game_logic.board)
            self.drawing.draw_shape(self.game_logic.current_shape,
                                    self.game_logic.current_shape_offset)
            self.drawing.draw_board_borders(self.game_logic.board)
            self.drawing.draw_ui(self.game_logic.score, self.game_logic.level,
                                 self.game_logic.next_shape)

            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    self.app.stop()
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_p, pygame.K_ESCAPE):
                        self.pause()
                    elif event.key in (pygame.K_a, pygame.K_LEFT):
                        self.game_logic.move_shape(-1, 0)
                    elif event.key in (pygame.K_d, pygame.K_RIGHT):
                        self.game_logic.move_shape(1, 0)
                    elif event.key in (pygame.K_s, pygame.K_DOWN):
                        move_down = True
                    elif event.key in (pygame.K_w, pygame.K_UP):
                        self.game_logic.rotate_shape()
                elif event.type == pygame.KEYUP:
                    if event.key in (pygame.K_s, pygame.K_DOWN):
                        move_down = False

            clock.tick(100)

    def stop(self):
        self.app.audio.stop_background_music()
        self.running = False

    def pause(self):
        self.stop()
        self.app.pause_menu.run()

    def lose(self):
        self.stop()
        self.app.records.save_record(self.game_logic.level, self.game_logic.score)
        self.app.lose_menu.run()

    def restart(self):
        self.stop()
        self.game_logic = GameLogic(self.app.audio)
        self.run()
