#!/usr/bin/python
#-*- coding:utf-8 -*-

#pass
print 'pass'
for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块'
   print '当前字母 :', letter
print ''

print '-----------------'
#字符串，list，元组，字典



print '-----------------'
print 'time'
import time
print time.time();
print time.localtime();
print time.localtime(time.time());
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime());

import calendar;
cal = calendar.month(2021,1);
print cal;