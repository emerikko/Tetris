import random

import pygame


class GameLogic:
    def __init__(self, audio):
        self.audio = audio
        self.score = 0
        self.level = 1
        self.current_shape_offset = (0, 0)
        self.board = [[False] * 10 for _ in range(20)]
        self.shapes = [
            [[True, True], [True, True]],
            [[True, True, False], [False, True, True]],
            [[True], [True], [True], [True]],
            [[False, True, True], [True, True, False]],
            [[False, True, False], [True, True, True]],
            [[True, True, True], [True, False, False]],
            [[True, True, True], [False, False, True]]
        ]
        self.current_shape = None
        self.next_shape = random.choice(self.shapes)

    def update(self):
        if self.current_shape is None:
            if not self.generate_new_shape():
                return False  # Игра окончена

        return True

    def move_shape(self, dx, dy):
        new_offset = (self.current_shape_offset[0] + dx, self.current_shape_offset[1] + dy)
        old_offset = self.current_shape_offset
        self.current_shape_offset = new_offset
        if self.check_collision():
            self.current_shape_offset = old_offset

    def move_down(self):
        # Передвижение текущей фигуры вниз
        self.current_shape_offset = (self.current_shape_offset[0], self.current_shape_offset[1] + 1)

        # Проверка коллизии
        if self.check_collision():
            self.current_shape_offset = (self.current_shape_offset[0], self.current_shape_offset[1] - 1)
            self.place_shape()
            self.clear_lines()
            if not self.generate_new_shape():
                return False  # Игра окончена

        return True
    def generate_new_shape(self):
        self.current_shape = self.next_shape
        self.next_shape = random.choice(self.shapes)
        self.current_shape_offset = (len(self.board[0]) // 2 - len(self.current_shape[0]) // 2, 0)

        if self.check_collision():
            return False  # Игра окончена
        return True

    def place_shape(self):
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    board_y = self.current_shape_offset[1] + y
                    board_x = self.current_shape_offset[0] + x
                    self.board[board_y][board_x] = True

    def clear_lines(self):
        lines_cleared = 0
        y = len(self.board) - 1
        while y >= 0:
            if all(self.board[y]):
                lines_cleared += 1
                self.board.pop(y)
                self.board.insert(0, [False] * len(self.board[0]))
            else:
                y -= 1

        if lines_cleared > 0:
            self.audio.play_line_clear_sound()
            self.add_score(lines_cleared)
            self.increase_difficulty()

    def increase_difficulty(self):
        self.level += 1

    def check_collision(self):
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    board_y = self.current_shape_offset[1] + y
                    board_x = self.current_shape_offset[0] + x
                    if (board_y >= len(self.board) or
                        board_x < 0 or board_x >= len(self.board[0]) or
                            self.board[board_y][board_x]):
                        return True
        return False

    def handle_input(self, event):
        if event.key == pygame.K_LEFT:
            self.move_shape(-1, 0)
        elif event.key == pygame.K_RIGHT:
            self.move_shape(1, 0)
        elif event.key == pygame.K_DOWN:
            self.move_down()
        elif event.key == pygame.K_UP:
            self.rotate_shape()

    def rotate_shape(self):
        old_shape = self.current_shape
        self.current_shape = list(zip(*self.current_shape[::-1]))
        if self.check_collision():
            self.current_shape = old_shape

    def add_score(self, lines_cleared):
        points_per_line = [40, 100, 300, 1200]
        self.score += points_per_line[lines_cleared - 1] * self.level
