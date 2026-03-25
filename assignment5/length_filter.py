"""
Reads words from standard input and filters out words shorter or longer than a given range.
Outputs only words within the specified length range (MIN and MAX provided as arguments).
"""

import sys


def length_filter(words, min_len, max_len) -> list[str]:
    """
    Filters words by length range.

    Args:
        words (list): List of words to filter.
        min_len (int): Minimum word length.
        max_len (int): Maximum word length.

    Returns:
        list: Filtered list of words.
    """
    return [word for word in words if min_len <= len(word) <= max_len]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python length_filter.py <min_len> <max_len>")
        sys.exit(1)
    if sys.argv[1] <= "0" or sys.argv[2] <= "0":
        print("Error: <min_len> and <max_len> must be a positive integer")
        sys.exit(1)
    if int(sys.argv[1]) > int(sys.argv[2]):
        print("Error: <min_len> must be less than or equal to <max_len>")
        print(f"{sys.argv}")
        sys.exit(1)

    min_len = int(sys.argv[1])
    max_len = int(sys.argv[2])
    # print(f"Filtering words between {min_len} and {max_len} characters")
    input_content = []
    for line in sys.stdin:
        input_content.append(line.strip())
    words = " ".join(input_content).split()
    filtered_words = length_filter(words, min_len, max_len)
    for word in filtered_words:
        print(word)
