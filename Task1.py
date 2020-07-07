string = 'Я учусь программированию в BRAIN'
res = ' '.join(word[0].upper() + word[1:] for word in string.split())
print(res)