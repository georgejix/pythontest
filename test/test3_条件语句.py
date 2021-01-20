#!/usr/bin/python
#-*- coding:UTF-8 -*-

#if else
print 'if else';
num = 4;
if num == 3:
	print 'num == 3';
elif num == 5:
	print 'num == 5';
else:
	print 'num=%d'%(num);

#循环
print '-----------';
print 'while';
a = 1.5;
while a < 5:
	print a;
	a += 1;
else:
	print 'a>=%f'%(a);

print '-----------';
print 'for';
for letter in 'Python':
	print letter,
print '';
#通过序列索引迭代
b = ['a','b','c','d','e'];
print range(len(b));
for index in range(len(b)):
	print b[index],
print '';
#循环使用 else 语句
for num in range(10,20):
	for i in range(2,num):
		if num%i == 0:
			j = num/i;
			print '%d=%d*%d'%(num,i,j);
			break;
	else:
		print '%d是质数'%(num);

#break
print '-----------';
print 'break';
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      break
   print '当前字母 :', letter

var = 10                    # 第二个实例
while var > 0:              
   print '当前变量值 :', var
   var = var -1
   if var == 5:   # 当变量 var 等于 5 时退出循环
      break

#continue
print '-----------';
print 'continue';
for letter in 'Python':
	if letter == 'h':
		continue;
	print letter,
print '';

var = 10                    # 第二个实例
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print '当前变量值 :', var
print "Good bye!"
