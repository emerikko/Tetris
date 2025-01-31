import pygame

from game import game_processor
from data import records
from sound import audio
from ui import main_menu, pause_menu, score_table


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.audio = audio.Audio()
        self.records = records.Records()

        self.game_processor = game_processor.GameProcessor(self)

        self.score_table = score_table.ScoreTable(self)
        self.main_menu = main_menu.MainMenu(self)
        self.pause_menu = pause_menu.PauseMenu(self)
        self.lose_menu = pause_menu.LoseMenu(self)

    def run(self):
        self.main_menu.run()

    def stop(self):
        self.game_processor.stop()
        self.main_menu.stop()
        self.pause_menu.stop()
        self.lose_menu.stop()
