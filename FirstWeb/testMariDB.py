import pymysql
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='wxxd123123',
                             db='opctest',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        #sql = "INSERT INTO table1 (tag_time, tag_name, tag_value) VALUES ('2019-08-19 13:08:11', 'tag3', '99.99')"
        sql = "INSERT INTO table1 (tag_time, tag_name, tag_value) VALUES (%s, %s, %s)"
        cursor.execute(sql, ('2019-08-19 15:08:11', 'tag3', '88.99'))
        #cursor.execute(sql,)23

    # connection is not autocommit by default. So you must commit to save your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT tag_time, tag_value FROM table1 WHERE tag_name = %s"
        cursor.execute(sql, ('tag3', ))
        result = cursor.fetchall()
        #result = cursor.fetchone()
        print(result)
finally:
    connection.close()