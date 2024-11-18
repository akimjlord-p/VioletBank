from core.db_func import add_contribution
from core.csv_func import add_csv_contribution


class Contribution:
    def __init__(self, name: str, start_sum: float, percent: float, type_of_term: str, term: int, type_of_capitalization: str):
        self.name = name
        self.sum_ = start_sum
        self.start_sum = start_sum
        self.percent = percent
        self.type_of_term = type_of_term
        self.term = term
        self.type_of_capitalization = type_of_capitalization
        self.data = []

    def calculate(self):
        self.data.append(self.sum_)
        for i in range(0, self.term):
            if self.type_of_capitalization == 'dif':
                self.sum_ += self.sum_ * self.percent / 100
            else:
                self.sum_ += self.start_sum * self.percent
            self.data.append(self.sum_)

    def get_data(self):
        return self.data

    def save_to_db(self):
        return add_contribution(self)

    def save_as_csv(self):
        add_csv_contribution(self)


class ContributionException(Exception):
    pass
