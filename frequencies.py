"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if item in frequencies.keys():
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    print(frequencies)
    return frequencies
