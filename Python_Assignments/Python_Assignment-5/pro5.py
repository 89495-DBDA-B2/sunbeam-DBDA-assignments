# Define the ROT-13 key dictionary
key = {
    'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a',
    'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 
    'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 
    'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'
}

def rot13(text):
    # Initialize an empty result string
    result = ''
    
    # Loop over each character in the input text
    for char in text:
        # If the character is in the key dictionary, replace it with the corresponding value
        if char in key:
            result += key[char]
        else:
            # If the character is not a letter (like spaces or punctuation), leave it unchanged
            result += char
    
    return result

# Example usage:
# Decoding the message
encoded_message = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
decoded_message = rot13(encoded_message)
print("Decoded message:", decoded_message)

# Encoding the message (it will be the same as decoding for ROT-13)
encoded_message_again = rot13(decoded_message)
print("Encoded message again:", encoded_message_again)
