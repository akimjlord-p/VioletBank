import sqlite3

con = sqlite3.connect('violet_db.db')
cur = con.cursor()


def is_db_empty() -> bool:
    cur.execute('''SELECT count(*) FROM sqlite_master WHERE type = "table"''')
    res = cur.fetchone()
    if res[0] != 0:
        return False
    else:
        return True


def initiate_db():
    cur.execute('''CREATE TABLE projects (
                    project_id INTEGER PRIMARY KEY,
                    data_type TEXT NOT NULL)
    ''')
    con.commit()
    cur.execute('''CREATE TABLE contributions (
                    contribution_id INTEGER PRIMARY KEY,
                    project_id INTEGER,
                    name TEXT,
                    start_sum REAL,
                    percent REAL,
                    type_of_term TEXT,
                    term INTEGER,
                    type_of_capitalization TEXT,
                    FOREIGN KEY (project_id) REFERENCES projects (project_id) )
    ''')
    con.commit()
    cur.execute('''CREATE TABLE loans (
                    loan_id INTEGER PRIMARY KEY,
                    project_id INTEGER,
                    start_sum REAL,
                    name TEXT,
                    percent REAL,
                    term INTEGER,
                    FOREIGN KEY (project_id) REFERENCES projects (project_id))
    ''')
    con.commit()


def add_contribution(contribution) -> bool:
    cur.execute('SELECT * FROM contributions WHERE name=?', (contribution.name,))
    res = cur.fetchall()
    if not res:
        cur.execute('SELECT project_id FROM projects WHERE project_id=(SELECT MAX(project_id) FROM projects)')
        last_id = cur.fetchone()
        if last_id:
            project_id = int(last_id[0]) + 1
        else:
            project_id = 0
        cur.execute('INSERT INTO projects(project_id,data_type) VALUES(?, "contribution")', (project_id,))
        cur.execute('INSERT INTO contributions'
                    '(contribution_id,'
                    'project_id,'
                    'name,'
                    'start_sum,'
                    'percent,'
                    'type_of_term,'
                    'term,'
                    'type_of_capitalization) VALUES('
                    '?, ?, ?, ?, ?, ?, ?, ?)',
                    (project_id,
                     project_id,
                     contribution.name,
                     contribution.start_sum,
                     contribution.percent,
                     contribution.type_of_term,
                     contribution.term,
                     contribution.type_of_capitalization))
        con.commit()
        return False
    else:
        cur.execute('UPDATE contributions '
                    'SET '
                    'start_sum=?, '
                    'percent=?,'
                    'type_of_term=?, '
                    'term=?, '
                    'type_of_capitalization=?'
                    'WHERE name=?', (contribution.start_sum,
                                     contribution.percent,
                                     contribution.type_of_term,
                                     contribution.term,
                                     contribution.type_of_capitalization,
                                     contribution.name))
        con.commit()
        return True


def get_projects():
    names_list = []
    cur.execute('SELECT * FROM projects')
    res = cur.fetchall()
    for project in res:
        if project[1] == 'contribution':
            cur.execute('SELECT name FROM contributions WHERE project_id=?', (project[0],))
            contribution = cur.fetchone()
            names_list.append('contribution ' + str(contribution[0]))
        else:
            cur.execute('SELECT name FROM loans WHERE project_id=?', (project[0],))
            loan = cur.fetchone()
            names_list.append('loan ' + str(loan[0]))
    return names_list


def get_contribution_by_name(name):
    cur.execute('SELECT * FROM contributions WHERE name=?', (name,))
    res = cur.fetchone()
    data = {'contribution_id': res[0],
            'project_id': res[1],
            'name': res[2],
            'start_sum': res[3],
            'percent': res[4],
            'type_of_term': res[5],
            'term': res[6],
            'type_of_capitalization': res[7]}
    return data


def get_loan_by_name(name):
    cur.execute('SELECT * FROM loans WHERE name=?', (name,))
    res = cur.fetchone()
    data = {'loan_id': res[0],
            'project_id': res[1],
            'start_sum': res[2],
            'name': res[3],
            'percent': res[4],
            'term': res[5]}
    return data


def add_loan(loan) -> bool:
    cur.execute(f'SELECT * FROM loans WHERE name="{loan.name}"')
    res = cur.fetchall()
    if not res:
        cur.execute('SELECT project_id FROM projects WHERE project_id=(SELECT MAX(project_id) FROM projects)')
        last_id = cur.fetchone()
        if last_id:
            project_id = int(last_id[0]) + 1
        else:
            project_id = 0
        cur.execute('INSERT INTO projects(project_id,data_type) VALUES(?, "loan")', (project_id,))
        cur.execute('INSERT INTO loans'
                    '(loan_id,'
                    'project_id,'
                    'name,'
                    'start_sum,'
                    'percent,'
                    'term)'
                    ' VALUES ('
                    '?, ?, ?, ?, ?, ?)', (project_id, loan.name, loan.start_sum, loan.percent, loan.term))
        con.commit()
        return False
    else:
        sql = (f'UPDATE loans '
               f'SET '
               f'start_sum=?, '
               f'percent=?,'
               f'term=?'
               f'WHERE name=?', (loan.start_sum, loan.percent, loan.term, loan.name))
        cur.execute(sql)
        con.commit()
        return True
