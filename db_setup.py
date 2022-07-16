import sqlite3


def create_user(username, password):
    conn = sqlite3.connect('mydb.db', check_same_thread=False)
    curr = conn.cursor()

    curr.execute(f'select * from user where username=(?) ', (username,))
    if not curr.fetchall():
        try:
            curr.execute(f'insert into user values (?, ?)', (username, hash(password)))
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
    else:
        return False
    curr.close()
    conn.close()
    return True


def log_user(username, password):
    conn = sqlite3.connect('mydb.db')
    curr = conn.cursor()
    curr.execute('select * from user where username=(?) and password=(?)', (username, password))
    if curr.fetchall():
        curr.close()
        conn.close()
        return True
    else:
        curr.close()
        conn.close()
        return False


def initdb():
    conn = sqlite3.connect('mydb.db')
    curr = conn.cursor()
    username= 'user'
    password = 'password'
    curr.execute('''insert into user values (?, ?)''', (username, password))
    conn.commit()

# initdb()


def check_users():
    conn = sqlite3.connect('mydb.db')
    curr = conn.cursor()
    curr.execute('select * from user')
    print(curr.fetchall())
    # conn.commit()
    curr.close()
    conn.close()


# check_users()/


def delete_users():
    conn = sqlite3.connect('mydb.db')
    curr = conn.cursor()
    curr.execute('delete from user')
    curr.close()
    conn.commit()
    conn.close()


# delete_users()
