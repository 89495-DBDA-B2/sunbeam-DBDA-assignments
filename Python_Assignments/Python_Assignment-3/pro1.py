# 1. Write a Python program that finds the longest word in a list of strings. Use map() to calculate the length of each word, and filter() to get the word with the maximum length.
   
# words = ["python", "functional", "programming", "is", "powerful"]


def fun():
    
    words = ["python", "functional", "programming", "is", "powerful"]
    
    lengths=list(map(len,words))
    maxl=max(lengths)
    
    longest_words = list(filter(lambda word: len(word) == maxl, words))
    print(longest_words)
fun()






















