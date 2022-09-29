import pymysql
connection = pymysql.connect(host='localhost', user='root', password='123456', charset='utf8')  # 连接数据库
cursor = connection.cursor()
# sql = "CREATE DATABASE `test` CHARACTER SET 'utf8';"
# cursor.execute(sql)
sql1 = "show databases;"
cursor.execute(sql1)
#data = cursor.fetchone() 只显示单行搜寻到的结果
data = cursor.fetchall() # 多行显示查询到的结果
print(data)
connection.close()




