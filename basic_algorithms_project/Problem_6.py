def get_min_max(ints):
    if ints == []:
        return ()
    min_val = ints[0]
    max_val = ints[0]
    for item in ints[1:]:
        if item > max_val:
            max_val = item
        if item < min_val:
            min_val = item
    return (min_val, max_val)


# testing

def test_function(test_cases):
    for case in test_cases:
        if get_min_max(case[1]) == case[2]:
            print("Test case " + case[0] + ": Pass!")
        else:
            print("Test case " + case[0] + ": FAIL.")


tc_1 = ('1', [5, 1, 7, 4, 2, 8, 3, 6, 9, 0], (0, 9))  # list of ints 0-9
tc_2 = ('2', [], ())  # list of zero ints
tc_3 = ('3', [4], (4, 4))  # list of one int
tc_4 = ('4', [123, 34509, 3409, 45, 2, 445, 3405, 234098, 98, 6786],
        (2, 234098))  # list of larger ints

test_cases = [tc_1, tc_2, tc_3, tc_4]
test_function(test_cases)
