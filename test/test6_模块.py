#!/usr/bin/python
#-*- coding:utf-8 -*-

print 'import';
import test6_lib;
print '1+2=',test6_lib.sum(1,2);

from test6_lib import sum;
print '2+3=',sum(2,3);

from test6_lib import *;
print '3+4=',sum2(3,4);

#PYTHONPATH 变量
#set PYTHONPATH=/usr/local/lib/python

#作用域
print '----------';
print '作用域';
var1 = 10;
def fun1(arg1):
	var1 = arg1;
	#声明var1是全局变量
	global var1
	return;
fun1(2);
print var1;

#dir()
print '----------';
print 'dir';
import math
print dir(math);


#globals(),locals()
print '----------';
print 'globals,locals';
def fun2():
	a=1;
	print 'locals:',locals();
	print 'globals:',globals();
	return;
fun2();

#reload
print '----------';
print 'reload';
import test6_lib2;
reload(test6_lib2);

#package
print '----------';
print 'package';
from package_runoob.runoob1 import *;
from package_runoob.runoob2 import *;
run1('run1');
run2('run2');