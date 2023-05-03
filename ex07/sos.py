import sys


def convert_to_morse(string: str) -> str:
    """convert_to_morse(string: str) -> str

Takes a string and returns its morse representation as a new string.
Raises an Assertion Error in case if any character is neither alphanumeric
nor a space."""
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. "
    }
    morse = ""
    for c in sys.argv[1].upper():
        morseChar = NESTED_MORSE.get(c)
        assert morseChar is not None, "string contains invalid characters"
        morse += morseChar
    return morse


def main():
    """main function of sos.py

Converts the argument to morse and prints the result.
Raises an Assertion Error if the number of arguments is different from 1
or if the argument contains any characters which are neither alphanumeric
nor spaces"""
    try:
        assert len(sys.argv) == 2, "wrong number of arguments"
        morse = convert_to_morse(sys.argv[1])
        print(morse[:-1])
    except AssertionError as msg:
        print("Assertion Error:", msg)


if __name__ == "__main__":
    main()
