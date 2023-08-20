import sqlite3


conn = sqlite3.connect('../cache_test.db')
cursor = conn.cursor()

# Query and retrieve data from the table
cursor.execute('SELECT * FROM user')
result = cursor.fetchall()

# Display the retrieved data
for row in result:
    print(f'ID: {row[0]}, Name: {row[1]}, Age: {row[2]}')

# Close the cursor and the database connection

cursor.close()
conn.close()

