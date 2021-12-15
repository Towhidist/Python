# some string function
s="hAve a nice dAy"
print (s)

print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())
print(s.center(60))
print(s.center(60,'*'))
print(s.replace('nice','good'))
print(s.find('nice'))
print(s.index('nice'))
print(s.count('a'))
print(s.count('A'))
print(s.lower().count('a'))
print(s.split())
s2='We,love,python,programming,language'
print(s2.split(','))
s3='We love-python programming language'
print(s3.split('-'))

result=s2.split(',')
print(type(result))
print(type(s2))
print(dir(s))