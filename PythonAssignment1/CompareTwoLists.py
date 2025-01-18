def compare_two_lists(list1, list2):

    if sorted(list1) == sorted(list2):
        return "Provided Two lists are Identical"
    else:
        return "Provided Two lists are not Identical"

print(compare_two_lists([1, 2, 3], [1, 2, 3]))
