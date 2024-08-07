# Author: Jake Trissel
# Github Username: trisselj
# Date: 08/07/2024
# Description: Gives the number of letters in a string of text

def count_letters(s):
    letter_counts = {} # Initialize empty dictionary for letter counting
    for char in s: # Iterates through every character in the text
        if 'a' <= char <= 'z':  # Checks if the character is a lowercase letter
            upper_char = chr(ord(char) - 32)  # Convert to uppercase using ASCII values
        elif 'A' <= char <= 'Z':  # Checks if the character is already an uppercase letter
            upper_char = char
        else:
            continue # Continues with code
        if 'A' <= upper_char <= 'Z': # Defines reading for characters only
            if upper_char in letter_counts: # If character already counted add 1
                letter_counts[upper_char] += 1 
            else: # If character not counted, set to one
                letter_counts[upper_char] = 1
    return letter_counts # Returns the number of letters