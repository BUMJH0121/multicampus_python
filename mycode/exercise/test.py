f = open("C:\mypython\python_programming_stu\python_programming_stu\mycode\exercise\yesterday.txt", "r")
yesterday_lyric = f.read()
print(yesterday_lyric.upper().count('YESTERDAY'))
print(yesterday_lyric.count('Yesterday'))
print(yesterday_lyric.count('yesterday'))

f.close()