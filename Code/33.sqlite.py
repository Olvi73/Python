# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 21:19:35 2020

@author: Oliver
"""

import pandas
import sqlite3


def create():
    with sqlite3.connect('Studb') as con:
        cursor=con.cursor()
        sql = 'create table Student(id varchar(20) primary key, name varchar(20), sex varchar(20), datetime varchar(20), member varchar(20), birth int, native varchar(20), score int, scholarship int, resume varchar(20))'
        cursor.execute(sql)
        con.commit()
        
        
def tbInsert():
    with sqlite3.connect('Studb') as con:
        cursor=con.cursor()
        sql = "INSERT INTO `Student` (`id`,`name`, `sex`, `datetime`) VALUES (?, ?, ?, ?)"
        # cursor.execute(sql,('1','Bob','man','2000-1-1'))
        # cursor.execute(sql,('2','Jackob','man','1999-1-1'))
        # cursor.execute(sql,('3','victoria','woman','1999-2-1'))
        cursor.execute(sql,('4','test','man','2000-3-2'))
        con.commit()
        
        
def tbDelete():
    with sqlite3.connect('Studb') as con:
        cursor=con.cursor()
        sql = "delete from Student where name=\'Bob\'"
        cursor.execute(sql)
        con.commit()
        
        
def tbUpdate():
    with sqlite3.connect('Studb') as con:
        cursor=con.cursor()
        sql = "update Student set member='no' where id='1'"
        cursor.execute(sql)
        con.commit()
            
        
def tbInfo():
    with sqlite3.connect('Studb') as con:
        cursor=con.cursor()
        cursor.execute("PRAGMA table_info(Student)")
        for rs in cursor.fetchall():
            print(rs)
        

def getall():
    with sqlite3.connect('Studb') as con:
        cursor=con.cursor()
        cursor.execute('select * from Student')
        for rs in cursor.fetchall():
            print(rs)
            

def query():
    with sqlite3.connect('Studb') as con:
        cursor=con.cursor()
        cursor.execute('select * from Student where sex=\'man\'')
        for rs in cursor.fetchall():
            print(rs)

        
def tbcsv():
    with sqlite3.connect('Studb') as con:
        df = pandas.read_csv('data.csv')
        df.to_sql('Student', con, if_exists='append', index=False)


