import pygame


class GameProcessor:
    def __init__(self, game_logic, audio, settings, drawing, score_table, pause_menu, main_menu):
        self.game_logic = game_logic
        self.audio = audio
        self.settings = settings
        self.drawing = drawing
        self.score_table = score_table
        self.pause_menu = pause_menu
        self.main_menu = main_menu
        self.running = True

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                        self.pause_game()

            drawing.draw_board(self.game.board)
            drawing.draw_shape(self.game.current_shape, self.game.current_shape_offset)
            drawing.draw_ui(self.game.score, self.game.level, self.game.next_shape)


            self.screen.fill((0, 0, 0))  # Очистка экрана
            pygame.display.flip()
            clock.tick(60)
