#!/usr/bin/python
#coding:utf-8
from flask import Flask,render_template,request,redirect,session
from db import insert,getone,update,select,delete
import json
import time
from . import app
filed=['id','apply_date','apply_type','apply_desc','deal_persion','status','deal_desc','deal_time','apply_persion']

# 工单列表
@app.route('/joblist/',methods=['POST','GET'])
def joblist():
    if not session:
        #return redirect('/login/')
        return redirect('/login/')
    where = {'status':['0','1']}
    res = select('ops_jobs',filed)
    return render_template('joblist.html',users=session,result=res['msg'])

# 工单详情
@app.route('/jobdetail/',methods=['POST','GET'])
def jobdetail():
    if not session:
        return redirect('/login/')
    data={k:v[0] for k,v in dict(request.args).items()}
    #print data
    result = getone('ops_jobs',filed,data)
    #print result
    #result = {'code':0,'msg':res['msg']['apply_desc']}    
    result['msg']['apply_date']=str(result['msg']['apply_date'])
    result['msg']['deal_time']=str(result['msg']['deal_time'])
    print result
    return json.dumps(result)



#创建工单
@app.route('/jobadd/',methods=['POST','GET'])
def jobadd():
     if not session:
        return redirect('/login/')
     if request.method=='POST':
         data={k:v[0] for k,v in dict(request.form).items()}
         if not data['apply_desc']:
            return json.dumps({'code':1,'errmsg':'apply_desc is not null'})
         data['apply_date']=time.strftime('%Y-%m-%d %H:%M')
         data['status'],data['apply_persion']=0,session['username']
         result = insert('ops_jobs',filed,data)
         return json.dumps(result)
     return render_template('jobadd.html',users=session)

#  处理
@app.route('/jobupdate/',methods=['POST','GET'])
def jobupdate():
     filed=['status']
     if not session:
        return redirect('/login/')
     if request.method=='POST':
         data={k:v[0] for k,v in dict(request.form).items()}
         data['status']=2
         print data
         result=update('ops_jobs',filed,data)
         return json.dumps(result)

     data={k:v[0] for k,v in dict(request.args).items()}
     data['deal_time']=time.strftime('%Y-%m-%d %H:%M')
     data['status']='1'
     data['deal_persion']=session['username']
     print data
     result=update('ops_jobs',filed,data)
     print result
     return json.dumps(result)

# 历史工单
@app.route('/jobhistory/',methods=['POST','GET'])
def jobhistoy():
    if not session:
        return redirect('/login/')
    data={k:v[0] for k,v in dict(request.args).items()}
    result = select('ops_jobs',filed)
    return render_template('jobhistory.html',users=session,result=result['msg'])


