import psycopg2

__connection = None


def get_connection():
    global __connection
    if __connection is None:
        __connection = psycopg2.connect(
        database="",
        user="",
        password="",
        host="",
        port=""
    )
    return __connection


def init_db(force: bool = False):
    """
        Перевірка чи потрібні таблиці існують, якщо ні, то створтити їх.
        'init_db(force = True)' перестворює таблиці.
    """
    conn = get_connection()

    c = conn.cursor()
    if force:
        c.execute('DROP TABLE IF EXISTS users')

    c.execute('''CREATE TABLE IF NOT EXISTS users (
            user_id     INTEGER NOT NULL,
            group_name       TEXT NOT NULL,
            search_teacher TEXT NOT NULL,
            discipline TEXT,
            UNIQUE(user_id)
        )
    ''')
    conn.commit()


def new_user(user_id: int, group: str = 'not_selected', search_teacher: str = 'off'):
    conn = get_connection()
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (user_id, group_name, search_teacher) VALUES (%s, %s, %s)', (user_id, group, search_teacher))
        print("NEW USER: %s" % user_id)
    except:
        print("%s exists" % user_id)
    conn.commit()


def set_group(group: str, user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET group_name=(%s) WHERE user_id=(%s)', (group, user_id))
    print('Встановлена група: %s' % group, '  User: %s' % user_id)
    conn.commit()


def check_group(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    group = c.execute('SELECT group_name FROM users WHERE user_id=(%s)', (user_id,))
    group = c.fetchone()
    conn.commit()
    #print('%s' % group)
    return group


def check_statisctic():
    conn = get_connection()
    c = conn.cursor()
    value = c.execute('SELECT COUNT(*) FROM users;')
    value = c.fetchone()
    return '%s' % value


def search_teacher_mode(user_id: int, search: str):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET search_teacher=(%s) WHERE user_id=(%s)', (search, user_id))
    conn.commit()


def check_mode(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    search_mode = c.execute('SELECT search_teacher FROM users WHERE user_id=(%s)', (user_id, ))
    search_mode = c.fetchone()
    conn.commit()
    return '%s' % search_mode


def search_teacher(surname: str):
    conn = get_connection()
    c = conn.cursor()
    full_name_teacher = c.execute('SELECT full_name FROM teachers WHERE surname = (%s)', (surname, ))
    full_name_teacher = c.fetchone()
    return '%s' % full_name_teacher


def set_discipline(user_id: int, discipline: str):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET discipline=(%s) WHERE user_id=(%s)', (discipline, user_id))
    conn.commit()


def check_discipline(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    discipline = c.execute('SELECT discipline FROM users WHERE user_id=(%s)', (user_id, ))
    discipline = c.fetchone()
    conn.commit()
    return '%s' % discipline




def qqq(descpl: str, lab: str = 'NaN', pr: str = 'NaN'):
    conn = get_connection()
    c = conn.cursor()
    try:
        c.execute('INSERT INTO techniques (discipline, lab, pr) VALUES (%s, %s, %s)', (descpl, lab, pr))
    except:
        print('memmee')
    conn.commit()

def get_lab(discipline: str):
    conn = get_connection()
    c = conn.cursor()
    lab = c.execute('SELECT lab FROM techniques WHERE discipline=(%s)', (discipline,))
    lab = c.fetchone()
    conn.commit()
    return '%s' % lab


