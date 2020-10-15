# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:45:11 2020

@author: Administrator
"""

import xlrd
data=xlrd.open_workbook('iris.xlsx')
table=data.sheets()[0]
tables=[]
def import_xls(xls):
    for row in range(xls.nrows):
        a={'data1':'','data2':'','data3':''}
        a['data1']=table.cell_value(row,0)
        a['data2']=table.cell_value(row,1)
        a['data3']=table.cell_value(row,2)
        tables.append(a)
import_xls(table)
for i in tables:
    print(i['data1'],end=' ')
    print(i['data2'],end=' ')
    print(i['data3'])
        
        
    