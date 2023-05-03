import sys


def get_input() -> str:
    """get_input() -> str

If exactly one argument is given, return that. Otherwise prompts for a
text input, reads from stdin until EOF and returns the input as string"""
    print("What is the text to count?")
    if (len(sys.argv) == 2):
        return (sys.argv[1])
    else:
        return (sys.stdin.read())


def check_string(input: str) -> dict:
    """check_string(input: str) -> dict

ounts upper letters, lower letters, punctuation marks, spaces and
digits and returns a dictionary with the values"""
    counts = {
        "upper letters": 0,
        "lower letters": 0,
        "punctuation marks": 0,
        "spaces": 0,
        "digits": 0
    }
    for c in input:
        if c.isupper():
            counts["upper letters"] += 1
        if c.islower():
            counts["lower letters"] += 1
        if c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            counts["punctuation marks"] += 1
        if c.isspace():
            counts["spaces"] += 1
        if c.isdigit():
            counts["digits"] += 1
    return counts


def print_result(inputStr: str, counts: dict):
    """print_result(inputStr: str, counts: dict)

prints first the total length of the input, then a breakdown of the
character types depending on the 'counts' dictionary"""
    print("The text contains %d characters:" % len(inputStr))
    for element in counts:
        print("%s %s" % (counts[element], element))


def main():
    """main function of building.py

determines the input string with get_input, creates a dictionary with
character type counts with check_string and prints it with print_result.
Raises an Assertion Error in case of too any arguments"""
    try:
        assert len(sys.argv) <= 2, "more than one argument provided"
        inputStr = get_input()
        counts = check_string(inputStr)
        print_result(inputStr, counts)
    except AssertionError as msg:
        print("Assertion Error:", msg)


if __name__ == "__main__":
    main()
