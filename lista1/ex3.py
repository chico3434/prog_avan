a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if(a > c):
    a,c = c,a
if (a > b):
    b,a = a,b
if (c < b):
    c,b = b,c

print(a,b,c)

