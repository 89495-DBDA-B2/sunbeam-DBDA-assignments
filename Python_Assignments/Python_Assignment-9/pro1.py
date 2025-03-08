# 1. Write a function in Python to count and display the total number of words in a text file

def count_words_in_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the contents of the file
            text = file.read()

            # Split the text into words (split by any whitespace)
            words = text.split()

            # Count the number of words
            word_count = len(words)

            # Display the total number of words
            print(f"Total number of words in the file '{filename}': {word_count}")

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = "sample.txt"  # Replace with the path to your text file
count_words_in_file(filename)
