#!/usr/bin/python
#coding:utf-8
import MySQLdb as mysql
con=mysql.connect(host="127.0.0.1",user="root",passwd="123456",db="reboot15",port=3306,charset='utf8')
con.autocommit(True)
cur = con.cursor()

#insert注册
def regist(table,field,data):
    sql = 'insert into %s (%s) values(%s)' %(table,','.join(field),','.join(['"%s"' %data[v] for v in field]))
    res = cur.execute(sql)
    if res:
        result = {'code':0,'msg':'reg success'}
    else:
        result = {'code':1,'msg':'reg faild'}
    return result
    

#select单用户查询
def getone(table,field,data):
    if data.has_key('username'):
        sql = "select * from %s where username='%s'" %(table,data['username'])
    else:
        sql = "select * from %s where id='%s'" %(table,data['id'])
    cur.execute(sql)
    res=cur.fetchone()
    if res:
        user = {k:res[i] for i,k in enumerate(field)}
        res = {'code':0,'msg':user}
        return res
    else:
        res = {'code':1,'msg':'user not is exist'}
    return res

#select多用户查询
def getall(table,field):
    sql = "select * from %s" %(table)
    cur.execute(sql)
    res = cur.fetchall()
    if res:
        user = [{k:row[i] for i,k in enumerate(field)} for row in res]
        res = {'code':0,'msg':user}
    else:
        res = {'code':1,'msg':'select faild'}
    return res

#数据更新
def update(table,field,data):
    sql = "update %s set %s where id=%s" %(table,','.join(["%s='%s'" %(k,data[k]) for k in data]),data['id'])
    res = cur.execute(sql)
    if res:
        res = {'code':0,'msg':'update success'}
    else:
        res = {'code':1,'msg':'update faild'}
    return res

#删除用户
def delete(user,uid):
    sql = "delete from %s where id=%s" %(user,uid)
    res = cur.execute(sql)
    if res:
        res = {'code':0,'msg':'delete success'}
    else:
        res = {'code':1,'msg':'delete faild'}
    return res