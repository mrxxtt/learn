#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql


   # return pymysql.connect(host='39.107.73.171',
   #                  port=3306,
   #                  user='root',
   #                  password='123456',
   #                  database='clear',
   #                  charset='utf8')
import mysql.connector
def conn():
    config = {
        'host': '39.107.73.171',
        'user': 'root',
        'password': '123456',
        'port': 3306,
        'database': 'clear',
        'charset': 'utf8'
    }
    return mysql.connector.connect(**config)  #指定utf8编码的连接
# cursor = conn.cursor()  # 创建一个光标，然后通过光标执行sql语句
# cursor.execute('create table user2 (id varchar(20) primary key, name varchar(20))')
# # 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user2 (id, name) values (%s, %s)', ['1', 'Michael'])
# cursor.execute("select * from user2")
# values = cursor.fetchall()  # 取出cursor得到的数据
# cursor.close(); conn.close()
# print(values)
