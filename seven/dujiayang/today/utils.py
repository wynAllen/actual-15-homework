#!/usr/bin/env python
#_*_ coding:utf-8 _*_


import MySQLdb as mysql
import config

db = mysql.connect(
                           user   =  config.db_user,
                           passwd =  config.db_passwd,
                           db     =  config.db_name ,
                           host   =  config.db_host,
                           charset=  "utf8" )
db.autocommit(True)
cur = db.cursor()

#import MySQLdb as mysql
#db = mysql.connect('121.43.191.76','reboot','reboot',db='reboot15',charset='utf8')
#db.autocommit(True)
#cur = db.cursor()

# 插入数据
def insert(table,field,data):
	sql = "insert into %s (%s) values (%s)" % (table,','.join(field),','.join(['"%s"' % data[x] for x in field]))
	print "util_insert_sql"
	print sql
	res = cur.execute(sql)
	print "util_insert_res"
	print res
	if res:
		result = {'code':0,'msg':'insert ok'}
	else:
		result = {'code':1,'msg':'insert fail'}
	print "util_insert_result"
	print result
	return result

# 查询数据
def getone(table,field,data):
	if data.has_key('username'):
		# 传过来的data是个字典，data['username']是个字符串，sql的where需要加双引号,即"%s"
		sql = 'select * from %s where username = "%s"' % (table,data['username'])
		print "util_getone_sql"
		print sql
	else:
		sql = 'select * from %s where id = "%s"' % (table,data['id'])
		print "util_getone_idsql"
		print sql
	cur.execute(sql)
	res = cur.fetchone()
	print "util_getone_res"
	print res
	if res:
		user = {k:res[i] for i,k in enumerate(field)}
		result = {'code':0,'msg':user}
	else:
		result = {'code':1,'msg':'data is null'}
	print "util_getone_result"
	print result
	return result

# 查询全部
def listall(table,field):
	sql = "select %s from %s" % (','.join(field),table)
	print "util_listall_sql"
	print sql
	cur.execute(sql)
	res = cur.fetchall()
	print "util_listall_res"
	print res
	if res:
		user = [{k:row[i] for i,k in enumerate(field)} for row in res] # 列表套字典
		result = {'code':0,'msg':user}
	else:
		resutl = {'code':1,'msg':'data is null'}
	print "util_listall_result"
	print result
	return result

# 更新数据
def updateuser(table,field,data):
	conditions = ["%s='%s'" % (k,data[k]) for k in data]
	print "util_update_condition"
	print conditions
	sql = "update %s set %s where id = %s" % (table,','.join(conditions),data['id'])
	print "util_update_sql"
	print sql
	res = cur.execute(sql)
	print "util_update_res"
	print res
	if res:
		result = {'code':0,'msg':'update success'}
	else:
		result = {'code':1,'msg':'update false'}
	print "util_update_rusult"
	print result
	return result

# 删除数据
def delete(table,uid):
	sql = "delete from %s where id = %s" % (table,uid)
	print "util_delete_sql"
	print sql
	res = cur.execute(sql)
	print "util_delete_res"
	print res
	if res:
		result = {'code':0,'msg':'delete ok'}
	else:
		result = {'code':1,'msg':'delete false'}
	print "util_delete_result"
	print result
	return result	
