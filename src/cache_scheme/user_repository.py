import sqlite3


def get_user_by_id_db(user_id: int):
    user = {}
    conn = sqlite3.connect('../cache_test.db')
    cursor = conn.cursor()

    # Query and retrieve data from the table
    cursor.execute(f'SELECT * FROM user where id ={user_id}')
    result = cursor.fetchall()

    # Display the retrieved data
    for row in result:
        # print(f'ID: {row[0]}, Name: {row[1]}, Age: {row[2]}')
        user = {'ID': row[0], 'Name': row[1], 'Age': row[2]}

    cursor.close()
    conn.close()

    return user


def update_user_by_id_db(user_id: int, user: dict):
    conn = sqlite3.connect('../cache_test.db')
    cursor = conn.cursor()

    update_query = '''
        UPDATE user
        SET age = ?
        WHERE id = ?
    '''
    cursor.execute(update_query, (user['Age'], user_id))
    # Query and retrieve data from the table
    cursor.execute(f'SELECT * FROM user where id ={user_id}')

    conn.commit()
    cursor.close()
    conn.close()

    return user
