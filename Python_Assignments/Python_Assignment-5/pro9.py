import re

def is_palindrome(phrase):
    # Remove all non-alphanumeric characters (spaces, punctuation) and convert to lowercase
    cleaned_phrase = re.sub(r'[^a-zA-Z0-9]', '', phrase).lower()
    
    # Check if the cleaned phrase is equal to its reverse
    return cleaned_phrase == cleaned_phrase[::-1]

# Example usage:
phrases = [
    "Go hanga salami I'm a lasagna hog.",
    "Was it a rat I saw?", 
    "Step on no pets", 
    "Sit on a potato pan, Otis", 
    "Lisa Bonet ate no basil", 
    "Satan, oscillate my metallic sonatas", 
    "I roamed under it as a tired nude Maori",
    "Rise to vote sir", 
    "Dammit, I'm mad!"
]

for phrase in phrases:
    print(f"'{phrase}' is a palindrome: {is_palindrome(phrase)}")
