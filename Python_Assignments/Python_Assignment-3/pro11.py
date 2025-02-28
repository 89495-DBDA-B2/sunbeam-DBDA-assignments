# 11.  Write a Python program that filters out all palindromes from a list of strings using the filter() function.
words = ['level', 'radar', 'hello', 'world', 'madam']

palindromes=list(filter(lambda m: m[::-1]==m,words))

print(palindromes)
