#!/usr/bin/python
# -*- coding:UTF-8 -*-

#逻辑运算符 or 	and		not
print 'or 	and		not';
a = True;
b = False;
if a or b:
	print 'a or b true';
else:
	print 'a or b false';

c = True;
d = True;
if c and d:
	print 'c and d true';
else:
	print 'c and d false';

if not(a and b):
	print 'not a and b true';
else:
	print 'not a and b false';


#成员运算符	in		not in
print '----------------';
print 'in		not in';
e = 20;
f = [1,2,20,'1'];
print (e in f);
print (e not in f);
print ('1' in f);

#身份运算符	is		is not
print '----------------';
print 'is		is not';
g = 20;
h = 20;
print (g is h);
print (g is not h);
g = '20';
h = '20';
print (g is h);
print (g is not h);

#is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等。
i = [1,2,3];
j = i;
print (i is j);
print (i == j);
j = i[:];
print i,j;
print (i is j);
print (i == j);