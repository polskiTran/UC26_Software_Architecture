"""
Reads lines of text from standard input and splits the text into words.
Outputs one word per line.
"""

import sys


def tokenize(line) -> list[str]:
    """
    Splits a line of text into words.

    Args:
        line (str): The line of text to tokenize.

    Returns:
        list[str]: A list of words.
    """
    return line.split()


if __name__ == "__main__":
    for line in sys.stdin:
        for word in tokenize(line.strip()):
            print(word)
