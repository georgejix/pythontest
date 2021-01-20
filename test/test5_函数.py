#!/usr/bin/python
#-*- coding:utf-8 -*-

#函数传参
def printStr(str):
	'printstr';
	print str;
	return;

printStr('123');
a=1;
#a = raw_input('input:');
printStr(str=a);
printStr(a);


#关键字参数，默认参数
def printStr2(name,age=17):
	print 'name=',name,',age=',age;
	return;
printStr2(age=18,name='zs');
printStr2('lisi');

#不定长参数
def printStr3(name,*p):
	print 'name=',name,p;
	for i in p:
		print i,;
	print '';
	return;
printStr3('zs',1,2,3);

#匿名函数
sum = lambda arg1,arg2:arg1+arg2;
print '1+2=',sum(1,2);

#return 语句
def sum2(arg1,arg2):
	return arg1+arg2;
print '2+3=',sum2(2,3);

#全局变量和局部变量
total = 0 # 这是一个全局变量
# 可写函数说明
def sum3( arg1, arg2 ):
   #返回2个参数的和."
   total = arg1 + arg2 # total在这里是局部变量.
   print "函数内是局部变量 : ", total
   return total
 
#调用sum函数
sum3( 10, 20 )
print "函数外是全局变量 : ", total