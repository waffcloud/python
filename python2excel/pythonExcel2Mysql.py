# !/usr/bin/env python
# coding=utf-8
import xlrd
import MySQLdb

# 读取EXCEL中内容到数据库中
wb = xlrd.open_workbook('G:\pel.xls')
sh = wb.sheet_by_index(0)
nrows = sh.nrows  # 行数
ncols = sh.ncols  # 列数
dfun = []
fo = []

fo.append(sh.row_values(0))
for i in range(1, nrows):
    dfun.append(sh.row_values(i))

conn = MySQLdb.connect(host='192.168.72.131', user='root', passwd='centos', db='db_31project', use_unicode=True, charset="utf8")
cursor = conn.cursor()
# 创建table
cursor.execute("create table test4(" + fo[0][0] + " varchar(100));")
# 创建table属性
for i in range(1, ncols):
    cursor.execute("alter table test4 add " + fo[0][i] + " varchar(100);")
val = ''
for i in range(0, ncols):
    val = val + '%s,'
print
dfun

cursor.executemany("insert into test4 values(" + val[:-1] + ");", dfun)
conn.commit()
