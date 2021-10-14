
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

if (x < (y+z)) and (y < (x+z)) and (z < (x+y)):
    if x == y and x == z:
        print('triângulo equilátero')
    elif x == y or x == z or y == z:
        print('triângulo isósceles')
    else:
        print('triângulo escaleno')
else:
    print('não pode ser um triângulo')
