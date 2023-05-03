def all_thing_is_obj(object: any) -> int:
    objType = type(object)
    types = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict"
    }
    if (objType is str):
        typeString = object + " is in the kitchen"
    else:
        typeString = types.get(objType)
    if (typeString is not None):
        print(typeString, ":", objType)
    else:
        print("Type not Found")
    return 42
