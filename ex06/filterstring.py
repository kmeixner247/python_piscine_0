from ft_filter import ft_filter
import sys


def filter_string(string: str, n: int) -> list:
    """filter_string(string: str, n: int) --> list

Return a list containing all words in the string that have more than
n characters. Words are defined as being separated by spaces.
If the string contains any characters that are not letters, digits, or spaces,
an Assertion Error is raised"""
    filtered = ft_filter(lambda str: len(str) > n, string.split(" "))
    return filtered


def main():
    """main function of filterstring.py

Checks whether exactly 2 arguments are provided, the first argument
contains a string without special or invisible characters and the second
argument is a valid integer.
Raises an Assertion Error if either is not true.
Then filters the string for words longer than the given integer and prints
the resulting list."""
    try:
        assert len(sys.argv) == 3, "wrong number of arguments"
        for c in sys.argv[1]:
            if not c.isalpha() and not c.isdigit() and not c == " ":
                raise AssertionError("string contains bad character")
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("bad input for number")
        filtered = filter_string(sys.argv[1], n)
        print([e for e in filtered])
    except AssertionError as msg:
        print("Assertion Error:", msg)


if __name__ == "__main__":
    main()
