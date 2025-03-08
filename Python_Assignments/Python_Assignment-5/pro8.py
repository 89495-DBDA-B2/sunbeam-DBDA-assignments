def translate(text):
    # Define vowels
    vowels = "aeiouAEIOU"
    
    # Initialize an empty string to store the result
    translated_text = ""
    
    # Iterate through each character in the input text
    for char in text:
        # Check if the character is a consonant (i.e., a letter that is not a vowel)
        if char.isalpha() and char not in vowels:
            # Double the consonant and add "o" in between
            translated_text += char + "o" + char
        else:
            # If it's a vowel or non-alphabet character (like space), add it as is
            translated_text += char
    
    return translated_text

# Example usage:
input_text = "this is fun"
translated_text = translate(input_text)
print(translated_text)
