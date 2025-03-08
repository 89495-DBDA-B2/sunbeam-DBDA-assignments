def count_lines_not_starting_with_c(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Initialize the counter for lines not starting with "C"
            count = 0

            # Iterate through each line in the file
            for line in file:
                # Strip any leading/trailing whitespace (including newlines)
                line = line.strip()

                # Check if the line doesn't start with "C"
                if not line.startswith('C'):
                    count += 1

            # Display the total number of lines not starting with "C"
            print(f"Number of lines not starting with 'C': {count}")
    
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = "story.txt"  # Replace with the actual path to your text file
count_lines_not_starting_with_c(filename)
