import csv


def add_csv_contribution(contribution):
    data_to_write = [
        {'type_of_data': 'type_of_project', 'data': 'contribution'},
        {'type_of_data': 'name', 'data': contribution.name},
        {'type_of_data': 'type_of_capitalization', 'data': contribution.type_of_capitalization},
        {'type_of_data': 'percent', 'data': contribution.percent},
        {'type_of_data': 'type_of_term', 'data': contribution.type_of_term},
        {'type_of_data': 'term', 'data': contribution.term},
        {'type_of_data': 'start_sum', 'data': contribution.start_sum}
    ]
    with open(f'{contribution.name}.csv', 'w', newline='', encoding="utf8") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=list(data_to_write[0].keys()),
            delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for i in data_to_write:
            writer.writerow(i)
        csvfile.close()


def get_type_of_project(fname):
    with open(fname, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        return list(reader)[1][1]


def get_contribution_from_csv(fname):
    with open(fname, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        reader = list(reader)
        res = {'name': reader[2][1],
               'type_of_capitalization': reader[3][1],
               'percent': reader[4][1],
               'type_of_term': reader[5][1],
               'term': reader[6][1],
               'start_sum': reader[7][1]}
        return res


def add_csv_loan(loan):
    data_to_write = [
        {'type_of_data': 'type_of_project', 'data': 'loan'},
        {'type_of_data': 'name', 'data': loan.name},
        {'type_of_data': 'percent', 'data': loan.percent},
        {'type_of_data': 'term', 'data': loan.term},
        {'type_of_data': 'start_sum', 'data': loan.start_sum}
    ]
    with open(f'{loan.name}.csv', 'w', newline='', encoding="utf8") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=list(data_to_write[0].keys()),
            delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for i in data_to_write:
            writer.writerow(i)
        csvfile.close()


def get_loan_from_csv(fname):
    with open(fname, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        reader = list(reader)
        res = {'name': reader[2][1],
               'percent': float(reader[3][1]),
               'term': int(reader[4][1]),
               'start_sum': float(reader[5][1])}
        return res
