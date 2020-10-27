def sort_012(input_list):
    zero_index = 0
    two_index = len(input_list) - 1
    curr_index = 0
    while curr_index <= two_index:
        curr_elem = input_list[curr_index]
        if curr_elem == 0:
            zero_index_num = input_list[zero_index]
            input_list[zero_index] = curr_elem
            input_list[curr_index] = zero_index_num
            zero_index += 1
            curr_index += 1
        elif curr_elem == 2:
            two_index_num = input_list[two_index]
            input_list[two_index] = curr_elem
            input_list[curr_index] = two_index_num
            two_index -= 1
        else:
            curr_index += 1
    return input_list


# testing

def test_function(test_cases):
    for case in test_cases:
        if sort_012(case[1]) == sorted(case[1]):
            print("Test case " + case[0] + ": Pass!")
        else:
            print("Test case " + case[0] + ": FAIL.")


# short array, starting and ending with 0
tc_1 = ('1', [0, 0, 2, 1, 1, 2, 0])
# medium array, starting and ending with 1
tc_2 = ('2', [1, 0, 0, 2, 1, 0, 2, 1, 1, 0, 0, 2, 0, 1])
# longer aray, starting and ending with 2
tc_3 = ('3', [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 1, 2, 0, 0, 2, 1, 0, 2])
# already sorted array
tc_4 = ('4', [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# array comprised of only 1s
tc_5 = ('5', [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# array comprised of only 2s
tc_6 = ('6', [2, 2, 2, 2, 2, 2, 2])
# array comprised of only 0s and 2s
tc_7 = ('7', [0, 2, 2, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 2, 2])
# array comprised of only 0s and 1s
tc_8 = ('8', [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1])
# array comprised of only one int
tc_9 = ('9', [2])
# array comprised of only two ints
tc_10 = ('10', [1, 0])

test_cases = [tc_1, tc_2, tc_3, tc_4, tc_5, tc_6, tc_7, tc_8, tc_9, tc_10]
test_function(test_cases)
