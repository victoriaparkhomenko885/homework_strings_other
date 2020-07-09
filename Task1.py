text = 'Я учусь программированию в BRAIN'
result = ' '.join(word[0].upper() + word[1:] for word in text.split())
print(result)