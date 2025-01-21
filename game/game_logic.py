class GameLogic:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.current_shape = None
        self.next_shape = None
        self.board = [[0] * 10 for _ in range(20)]
        print(self.board)

    def update(self):
        # Логика падения фигур, проверка заполненных линий и т.д.
        pass

    def handle_input(self, event):
        # Обработка ввода пользователя (перемещение, поворот фигур)
        pass

    def add_score(self, lines_cleared):
        # Подсчет очков за уничтоженные линии
        pass