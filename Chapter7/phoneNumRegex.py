#!/usr/bin/python3
#正则表达式匹配
import re
phoneNumRegex=re.compile(r'\d{3}-\d{3}-\d{4}')
mo=phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
#利用括号分组
isphoneNumRegex=re.compile(r'(\d{3})-(\d{3}-\d{4})')
tam=isphoneNumRegex.search('My number is 415-555-4242.')
print(tam.group(0))
print(tam.group(1))
print(tam.group(2))
#利用管道匹配多个分组
heroregx=re.compile(r'tom|amy')
mo1=heroregx.search('tom and amy to feel!')
print(mo1.group())
heroregx=re.compile(r'tom|amy')
mo2=heroregx.search('amy and tom to feel!')
print(mo2.group())
#用问号实现可选匹配 不管存在不存在都可以
woman=re.compile(r'Bat(wo)?man')
mo3=woman.search('The Adventures of Batman')
print(mo3.group())

mo4=woman.search('The Adventures of Batwoman')
print(mo4.group())

#星号（*）匹配多次
batregx=re.compile(r'Bat(wo)*man')
mo5=batregx.search('The Adventures of Batwoman')
print(mo5.group())
mo6=batregx.search('The Adventures of Batwowowoman')
print(mo6.group())
mo7=batregx.search('The Adventures of Batman')
print(mo7.group())

#用加号匹配一次或多次
batregx=re.compile(r'Bat(wo)+man')
mo9=batregx.search('The Adventures of Batwoman')
print(mo9.group())
mo10=batregx.search('The Adventures of Batwowowoman')
print(mo10.group())
#不区分大小写的匹配
print('不区分大小写的匹配')
robocop=re.compile(r'robocop',re.I)
print(robocop.search('RoboCOP is part man, part machine, all cop.').group())
#用 sub()方法替换字符串
print('用 sub()方法替换字符串')
namesRegex=re.compile(r'Agent \w+')
print(namesRegex.sub('Tom','Agent  Alice gave the secret  documents to Agent Bob'))
agentnameRegex=re.compile(r'Agent (\w)\w*')
print(agentnameRegex.sub(r'\1xxx','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))