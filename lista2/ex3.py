
idade = [21, 35, 24, 32, 400, 30, 20, 19, 450, 29]
print(idade)
idade = [int(i/10) if 400 <= i < 500 else i for i in idade]
print(idade)
