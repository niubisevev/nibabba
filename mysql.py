import pymysql

db=pymysql.connect(host='localhost',port=3306,user='debian-sys-maint',password='MUN1H8MWUYNePwHp',database='stu',charset='utf8')
cur =db.cursor()
# cur.execute("update student set age=12 where name ='ss'")
cur.execute("delete from student where name ='ss'")
db.commit()
cur.close()
db.close()