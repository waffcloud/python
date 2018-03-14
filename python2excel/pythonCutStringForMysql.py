# !/usr/bin/env python
# coding=utf-8

import MySQLdb


# 连接 mysql，获取连接的对象
con = MySQLdb.connect(host='192.168.72.131', user='root', passwd='centos', db='db_31project', use_unicode=True, charset="utf8")

# 仍然是，第一步要获取连接的 cursor 对象，用于执行查询
cur = con.cursor()

# 类似于其他语言的 query 函数， execute 是 python 中的执行查询函数
cur.execute("SELECT * FROM test4")

# 使用 fetchall 函数，将结果集（多维元组）存入 rows 里面
rows = cur.fetchall()

# 依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示
#size = row[3]
#status = row[4]
#createAt = row[5]

for row in rows:
   # print (row)
    # 这里，可以使用键值对的方法，由键名字来获取数据
    # print "%s %s" % (row["user_id"], row["user_name"])
   # print("id=%s,stream_name=%s,download_url=%s,size=%s,status=%d,createAt=%s" % (id, stream_name, download_url, size, status, createAt))
    s=(row[4])
    ab=s.split(',')
    print(ab)
    print(ab[0])
    print(ab[-1])
    print(row[0])
    try:
        cur.execute("UPDATE test4 SET longitude='%s',latitude='%s'  WHERE camera_name = '%s' " % (ab[0],ab[-1],row[0]))
        # print("longitude=%s" % (row[4]))
        # 提交到数据库执行
        con.commit()
    except:
   # 发生错误时回滚
        con.rollback()

        # 关闭数据库连接
con.close()


