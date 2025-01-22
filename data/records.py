import csv

class Records:
    def __init__(self, filename='records.csv'):
        self.filename = filename
        self.records = self.load_records()

    def load_records(self):
        try:
            with open(self.filename, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                return list(reader)
        except FileNotFoundError:
            return []

    def save_record(self, name, score):
        self.records.append([name, score])
        self.records.sort(key=lambda x: int(x[1]), reverse=True)
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.records[:10])  # Сохраняем только топ-10 рекордов
            