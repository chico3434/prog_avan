def f_troca(str):
    first = str[0].lower()
    newStr = []
    for i in range(len(str)):
        if str[i].lower() == first and i != 0:
            newStr.append('#')
        else:
            newStr.append(str[i])
    return "".join(newStr)


print(f_troca('ENCE'))
print(f_troca('Dados'))
print(f_troca('Armação'))
print(f_troca('calça clochard'))

