import pymysql

connection = pymysql.connect(host='localhost', user='root', password='123456', charset='utf8')  # 连接数据库
cursor = connection.cursor()
sql = "CREATE DATABASE `test` CHARACTER SET 'utf8';"  # 创建数据库test
cursor.execute(sql)
connection.close()
