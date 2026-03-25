"""
Reads words from standard input.
Converts all words to lowercase.
Outputs lowercase words.
"""

import sys


def lowercase_filter(word: str) -> str:
    """
    Converts a word to lowercase.

    Args:
        word (str): The word to convert.

    Returns:
        str: The lowercase word.
    """
    return word.lower()


if __name__ == "__main__":
    for line in sys.stdin:
        print(lowercase_filter(line.strip()))
