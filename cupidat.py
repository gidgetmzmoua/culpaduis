# Input string
input_string = "Hello world! This is a test."

# Split the string into words and reverse the order
words = input_string.split()
reversed_words = words[::-1]

# Join the reversed words back into a string
reversed_string = " ".join(reversed_words)

# Print the string with words in reverse order
print(reversed_string)
