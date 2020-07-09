import shlex
from collections import Counter

article = input("Enter article: ")
article = article.replace(',', '').replace('.', '').lower()
output = [word for word in shlex.split(article) if len(word) >= 3]
print(Counter(output).most_common(3))
