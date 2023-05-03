def get_padding_count(n: int, max: int) -> int:
    """get_padding_count(n: int, max: int) -> int

calculates with how many spaces n needs to be padded to
right-align it with max"""
    count = 0
    temp = 10
    while (temp <= max):
        if (n < temp):
            count += 1
        temp *= 10
    return count


def ft_tqdm(lst: range) -> None:
    """ft_tqdm(lst: range) -> None

A generator function that yields progress updates for a given list
as it is iterated over"""
    total = len(lst)

    for n, item in enumerate(lst):
        percentage = (n+1) / total * 100
        widthfactor = 0.44 - 0.02 * get_padding_count(0, total)
        progressbar = "█" * int(widthfactor * percentage)
        padding = " " * int(widthfactor * (100-percentage))
        share = " " * get_padding_count(n+1, total) + "%d/%d" % (n+1, total)
        percString = "\r" + " " * get_padding_count(percentage, 100)
        percString += "{0:.0f}%|".format(percentage)
        print(percString+progressbar+padding+"| "+share, end='')
        yield
