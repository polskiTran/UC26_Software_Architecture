"""
Reads words from standard input.
Counts how many times each word appears.
Outputs words that appear at least N times (where N is provided as a command-line argument)
"""

import sys


def word_frequency_filter(words, min_count) -> list[str]:
    """
    Filters words that appear at least min_count times.

    Args:
        words (list): List of words to filter.
        min_count (int): Minimum number of times a word must appear to be included.

    Returns:
        list: Filtered list of words.
    """
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return [word for word, count in word_count.items() if count >= min_count]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_frequency_filter.py <min_count>")
        sys.exit(1)
    if sys.argv[1] <= "0":
        print("Error: <min_count> must be a positive integer")
        sys.exit(1)
    min_count = int(sys.argv[1])
    input_content = []
    for line in sys.stdin:
        input_content.append(line.strip())
    words = " ".join(input_content).split()
    filtered_words = word_frequency_filter(words, min_count)
    for word in filtered_words:
        print(word)
