#用 strip()、rstrip()和 lstrip()删除空白字符
spam = ' Hello World '
print(spam)
#删除两端空白字符
print(spam.strip()) 
#删除左边空白字符
print(spam.lstrip())
#删除右边空白字符
print(spam.rstrip())
#用 strip()、rstrip()和 lstrip()删除字符
spam1='aShesldhfqlasldfaS'
#删除两端包含a S h的字符。可以多，不分顺序，区分大小写，有其中一个字符就删除，直到边缘没有a S h这三个字符
print(spam1.strip('aSh'))
#删除右端包含a S h的字符。
print(spam1.rstrip('haS'))
#删除左端包含a S h的字符。
print(spam1.lstrip('Sah'))
#用 pyperclip 模块拷贝粘贴字符串
print('用 pyperclip 模块拷贝粘贴字符串')
import pyperclip
pyperclip.copy(spam)
print(pyperclip.paste())

