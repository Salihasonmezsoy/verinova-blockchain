import pymysql

db_url = pymysql.connect(host='localhost',
                         user='root',
                         password='12345',
                         db='new_schema',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)