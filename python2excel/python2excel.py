# coding:utf8
import sys
import xlwt
#import MySQLdb
import pymysql as MySQLdb
import datetime

host = '192.168.72.131'
user = 'root'
pwd = 'centos'
db = 'db_31project'
sql = 'select * from Testvideo'
sheet_name = 'building'
out_path = 'F:\one.xls'

# 把数据库的数据导入到excel 中
conn = MySQLdb.connect(host,user,pwd,db,charset='utf8')
cursor = conn.cursor()
count = cursor.execute(sql)
print(count)

cursor.scroll(0,mode='absolute')
results = cursor.fetchall()
fields = cursor.description
workbook = xlwt.Workbook()
sheet = workbook.add_sheet(sheet_name,cell_overwrite_ok=True)

for field in range(0,len(fields)):
    sheet.write(0,field,fields[field][0])

row = 1
col = 0
for row in range(1,len(results)+1):
    for col in range(0,len(fields)):
        sheet.write(row,col,u'%s'%results[row-1][col])

workbook.save(out_path)