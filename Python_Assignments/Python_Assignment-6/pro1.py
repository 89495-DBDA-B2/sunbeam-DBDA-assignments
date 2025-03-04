# 1 . A pangram is a sentence that contains all the letters of the English alphabet at least once.
# for example: The quick brown fox jumps over the lazy dog. 
# Your task here is to write a function to check a sentence to see if it is a pangram or not.


def is_pangram(sentence):
    print(f"Oriinal String; {sentence}")
    
    sentence = sentence.replace(" ", "").lower()


    str=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    flag= True

    for letter in str:
        if letter not in sentence:  # If the letter is not found in the sentence
            flag = False  # It's not a pangram
            break  # Exit the 

    # Output result
    if flag:
        print("The sentence contains all the letters of the English alphabet at least once.")
    else:
        print("The sentence does not contain all the letters of the English alphabet.")



is_pangram("The quick brown fox jumps over the lazy dog")
