def NULL_not_found(object: any) -> int:
    types = {
        None: "Nothing:",
        '': "Empty:",
        False: "Fake:"
    }
    if (object != object):
        string = "Cheese:"
    elif (object == 0):
        string = "Zero:"
    else:
        string = types.get(object)
    if (string is not None):
        print(string, object, type(object))
        return 0
    else:
        print("Type not Found")
        return 1
