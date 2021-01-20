#!/usr/bin/python
# -*- coding:UTF-8 -*-

#raw_input("wait input:");
import sys
sys.stdout.write("123\n");

#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,
a = '1';
b = '2';
print a,b

#多个变量赋值
c=d=1;
e,f = 2,'3';
print c,d,e,f;

g = 'g';
del g;

h = '123456'
print h[1::2];
print h * 2;
print h + 'hhh';
print h[-3:];
print h[0:5];

i = ('a',233,'c',2.3,'sda');
#i[0] = 1;	元组不允许更改
print i[1:];

j = [1,2,3,4];
j[0] = 'a';
print j;

k = {};
k['one'] = 'one1';
k['2'] = 'two2';
print k;
print k.keys();
print k.values();