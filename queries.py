import sqlite3
from prettytable import PrettyTable

def f1():
    """Выведите список всех студентов.
    Атрибуты вывода: name, surname, age.

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 name, 
                 surname, 
                 age 
                 FROM student''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    pt.align[col_names[0]] = "l"
    pt.align[col_names[1]] = "l"

    for row in rows:
        pt.add_row(row)
    
    print("=== Список всех студентов ===")
    print(pt)
    con.close()

def f2():
    """Выведите отсортированный по фамилиям список студентов из группы ЮРИ-401.
    Имя группы произвольно.
    Атрибуты вывода: "Группа", "Фамилия", "Имя".

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 g.name as "Группа", 
                 s.surname as "Фамилия", 
                 s.name as "Имя"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 WHERE g.name LIKE 'ЮРИ-404'
                 ORDER BY s.surname''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"
    
    for row in rows:
        pt.add_row(row)
    
    print("=== Студенты группы ЮРИ (отсортировано по фамилиям) ===")
    print(pt)
    con.close()

def f3():
    """Выведите всех девушек, обучающихся на факультете 'Реклама'.
    Атрибуты вывода: Название факультета, фамилия.

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 d.name as "Название факультета", 
                 s.surname as "Фамилия"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 JOIN department d ON g.department_id = d.id
                 WHERE d.name = 'Реклама' AND s.gender = 'Женский'
                 ORDER BY s.surname''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"
    
    for row in rows:
        pt.add_row(row)
    
    print("=== Девушки на факультете 'Реклама' ===")
    print(pt)
    con.close()

def f4():
    """Определите количество молодых людей, обучающихся на юридическом факультете.
    Атрибуты вывода: 'Кол-во молодых людей'. Количество строк: 1.

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 COUNT(*) as "Кол-во молодых людей"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 JOIN department d ON g.department_id = d.id
                 WHERE d.name = 'Юриспруденция' AND s.gender = 'Мужской' ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"
    
    for row in rows:
        pt.add_row(row)
    
    print("=== Количество молодых людей на юридическом факультете ===")
    print(pt)
    con.close()

def f5():
    """Определите средний возраст студентов, обучающихся на юридическом факультете.
    Округлите результат до целого числа.
    Атрибуты вывода: 'Юр. фак-т. Средний возраст'. Количество строк: 1.

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 ROUND(AVG(s.age)) as "Юр. фак-т. Средний возраст"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 JOIN department d ON g.department_id = d.id
                 WHERE d.name = 'Юриспруденция' ''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"
    
    for row in rows:
        pt.add_row(row)
    
    print("=== Средний возраст студентов на юридическом факультете ===")
    print(pt)
    con.close()

def f6():
    """Выведите студентов количество, обучающихся на каждом факультете.
    Атрибуты вывода: 'Факультет', 'Количество'. Количество строк должно быть 
    равно количеству факультетов.

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 d.name as "Факультет", 
                 COUNT(s.id) as "Количество"
                 FROM department d
                 LEFT JOIN "group" g ON d.id = g.department_id
                 LEFT JOIN student s ON g.id = s.group_id
                 GROUP BY d.id, d.name
                 ORDER BY "Количество" DESC''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"
    
    for row in rows:
        pt.add_row(row)
    
    print("=== Количество студентов на каждом факультете ===")
    print(pt)
    con.close()

def f7():
    """Выведите средний возраст студентов, обучающихся на каждом факультете.
    Результат округлите до 2-х знаков после точки.
    Атрибуты вывода: 'Факультет', 'Средний возраст'.

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 d.name as "Факультет", 
                 ROUND(AVG(s.age), 2) as "Средний возраст"
                 FROM department d
                 LEFT JOIN "group" g ON d.id = g.department_id
                 LEFT JOIN student s ON g.id = s.group_id
                 GROUP BY d.id, d.name
                 ORDER BY "Средний возраст" DESC''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"
    
    for row in rows:
        pt.add_row(row)
    
    print("=== Средний возраст студентов по факультетам ===")
    print(pt)
    con.close()

def f8():
    """Выведите список студентов, которые не обучаются на юридическом факультете.
    Атрибуты вывода: 'Факультет', 'Группа', 'ФИО'. Атрибут ФИО  должен состоять из фамилии,
    первой буквы имени и точки (напр. Иванов И.).
    
    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 d.name as "Факультет", 
                 g.name as "Группа", 
                 s.surname || ' ' || SUBSTR(s.name, 1, 1) || '.' as "ФИО"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 JOIN department d ON g.department_id = d.id
                 WHERE d.name != 'Юриспруденция'
                 ORDER BY d.name, g.name, s.surname''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"
    
    for row in rows:
        pt.add_row(row)
    
    print("=== Студенты не юридического факультета (ФИО формат) ===")
    print(pt)
    con.close()

def f9():
    """Выведите список студентов юридического факультета, у которых возраст
    меньше среднего по факультету.
    Атрибуты вывода: 'Факультет', 'Фамилия', 'Возраст'.

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 d.name as "Факультет", 
                 s.surname as "Фамилия", 
                 s.age as "Возраст"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 JOIN department d ON g.department_id = d.id
                 WHERE d.name = 'Юриспруденция' 
                 AND s.age < (SELECT AVG(s2.age) 
                              FROM student s2
                              JOIN "group" g2 ON s2.group_id = g2.id
                              JOIN department d2 ON g2.department_id = d2.id
                              WHERE d2.name = 'Юриспруденция')
                 ORDER BY s.age''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"
    
    for row in rows:
        pt.add_row(row)
    
    print("=== Студенты юрфака с возрастом меньше среднего ===")
    print(pt)
    con.close()

def f10():
    """Выведите список студентов, у которых фамилия начинается на букву 'К'.
    Атрибуты вывода: 'Факультет', 'Группа', 'Фамилия'.

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 d.name as "Факультет", 
                 g.name as "Группа", 
                 s.surname as "Фамилия"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 JOIN department d ON g.department_id = d.id
                 WHERE s.surname LIKE 'К%'
                 ORDER BY d.name, g.name, s.surname''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"
    
    for row in rows:
        pt.add_row(row)
    
    print("=== Студенты с фамилией на букву 'К' ===")
    print(pt)
    con.close()

def f11():
    """Выведите список студентов группы ЮРИ-401 (имя группы произвольно),
    у которых имя заканчивается на букву 'й' (напр. Аркадий).
    Атрибуты вывода: 'Группа', 'Имя', 'Фамилия'.

    """
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 g.name as "Группа", 
                 s.name as "Имя", 
                 s.surname as "Фамилия"
                 FROM student s
                 JOIN "group" g ON s.group_id = g.id
                 WHERE g.name LIKE 'ЮРИ-403' AND s.name LIKE '%й'
                 ORDER BY s.surname''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"
    
    for row in rows:
        pt.add_row(row)
    
    print("=== Студенты группы ЮРИ с именами на 'й' ===")
    print(pt)
    con.close()

def f12():
    '''Выведите студента с самой длинной по количеству символов фамилией.
    Атрибуты вывода: "Фамилия", "Кол-во символов"

    '''
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 surname as "Фамилия", 
                 LENGTH(surname) as "Кол-во символов"
                 FROM student
                 ORDER BY LENGTH(surname) DESC
                 LIMIT 1''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"
    
    for row in rows:
        pt.add_row(row)
    
    print("=== Студент с самой длинной фамилией ===")
    print(pt)
    con.close()

def f13():
    '''Выведите уникальный список женских имен и количество их повторений.
    Список должен быть отсортирован по количеству повторений в порядке убывания.
    Атрибуты вывода: "Имя", "Кол-во повторений"

    '''
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    curs.execute('''SELECT 
                 name as "Имя", 
                 COUNT(*) as "Кол-во повторений"
                 FROM student
                 WHERE gender = 'Женский'
                 GROUP BY name
                 ORDER BY COUNT(*) DESC, name''')
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"
    
    for row in rows:
        pt.add_row(row)
    
    print("=== Уникальные женские имена и их количество ===")
    print(pt)
    con.close()

def f14():
    '''Выведите 3 последние записи из таблицы student.
    Сортировку не использовать.
    Атрибуты вывода: id, surname

    '''
    print("\n")
    con = sqlite3.connect("ursei.db")
    curs = con.cursor()

    # Получаем максимальный ID
    curs.execute('''SELECT MAX(id) FROM student''')
    max_id = curs.fetchone()[0]
    
    # Выбираем 3 последние записи по ID (без сортировки в запросе)
    curs.execute('''SELECT 
                 id, 
                 surname
                 FROM student
                 WHERE id >= ?''', (max_id - 2,))
    
    col_names = [cn[0] for cn in curs.description]
    rows = curs.fetchall()

    pt = PrettyTable(col_names)
    for col in col_names:
        pt.align[col] = "l"
    
    for row in rows:
        pt.add_row(row)
    
    print("=== 3 последние записи из таблицы студентов ===")
    print(pt)
    con.close()

func_register = {
    '1': f1,
    '2': f2,
    '3': f3,
    '4': f4,
    '5': f5,
    '6': f6,
    '7': f7,
    '8': f8,
    '9': f9,
    '10': f10,
    '11': f11,
    '12': f12,
    '13': f13,
    '14': f14
}