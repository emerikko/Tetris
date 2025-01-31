import pygame


class Audio:
    def __init__(self):
        pygame.mixer.init()
        self.background_music = pygame.mixer.Sound('sounds/background.mp3')
        self.line_clear_sound = pygame.mixer.Sound('sounds/line_clear.wav')
        self.click_sound = pygame.mixer.Sound('sounds/click.mp3')

    def play_background_music(self):
        self.background_music.play(-1)

    def stop_background_music(self):
        self.background_music.stop()

    def play_line_clear_sound(self):
        self.line_clear_sound.play()

    def play_click_sound(self):
        self.click_sound.play()
