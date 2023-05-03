import sys

try:
    assert len(sys.argv) <= 2, "more than one argument are provided"
    try:
        n = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    except IndexError:
        sys.exit()
except (AssertionError, ValueError) as msg:
    print("Assertion Error:", msg)
    sys.exit()

print("I'm Odd" if n % 2 == 1 else "I'm Even")
