"""
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def isUnique(input_string):
    # With additional data structure
    output_dictionary = {}
    for letter in input_string:
        if (letter in output_dictionary):
            return False
        else:
            output_dictionary[letter] = 1
    return True


def isUniqueNoDataStructure(input_string):
    # No additional data structure
    string_array = list(input_string)
    string_array.sort()
    prev_letter = None
    for letter in string_array:
        if letter == prev_letter:
            return False
        else:
            prev_letter = letter
    return True
