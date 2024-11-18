from core.db_func import add_loan
from core.csv_func import add_csv_loan
class Loan:
    def __init__(self, name: str, start_sum: float, percent: float, term: int):
        self.name = name
        self.sum_ = start_sum
        self.start_sum = start_sum
        self.percent = percent
        self.term = term
        self.data = []
        self.overpayment = 0
        self.monthly_payment = None
        self.monthly_percent = percent / 1200

    def calculate(self):
        self.sum_ = self.start_sum
        self.monthly_payment = self.start_sum * (self.monthly_percent + self.monthly_percent /
                                                 ((1 + self.monthly_percent) ** int(self.term) - 1))
        for i in range(self.term):
            percent_payment = self.sum_ * self.monthly_percent
            payment_without_percent = self.monthly_payment - percent_payment
            self.overpayment += percent_payment
            self.sum_ -= payment_without_percent
            self.data.append({'monthly_payment': self.monthly_payment,
                              'percent_payment': percent_payment,
                              'payment_without_percent': payment_without_percent,
                              'sum_': self.sum_})

    def get_data(self):
        return self.data

    def save_to_db(self):
        return add_loan(self)

    def save_as_csv(self):
        add_csv_loan(self)
class LoanException(Exception):
    pass
