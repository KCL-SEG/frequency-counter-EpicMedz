"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if f"{item}" in frequencies.keys():
            frequencies[f"{item}"] += 1
        else:
            frequencies[f"{item}"] = 1
    print(frequencies)
    return frequencies
