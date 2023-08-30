def list_to_string(lst):
    # check if the list is empty
    if not lst:
        return ""
    # check if the list has only one item
    elif len(lst) == 1:
        return lst[0]
    else:
        return ", ".join(lst[:-1]) + ", and " + lst[-1]
empty = []
print(list_to_string(empty))
