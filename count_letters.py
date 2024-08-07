# Author: Jake Trissel
# Github Username: trisselj
# Date: 08/07/2024
# Description: Gives the number of letters in a string of text

def countletters(s):
    letter_counts = {} # Initialize empty dictionary for letter counting
    for char in s: # Iterates through every character in the text
        upper_char = char.upper() # Converts lower case to upper case for ease of counting
        if 'A' <= upper_char <= 'Z': # Defines reading for characters only
            if upper_char in letter_counts: # If character already counted add 1
                letter_counts[upper_char] += 1 
            else: # If character not counted, set to one
                letter_counts[upper_char] = 1
    return letter_counts # Returns the number of letters