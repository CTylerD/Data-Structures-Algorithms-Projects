def rotated_array_search(input_list, number):
    if len(input_list) == 0:
        return -1
    start = 0
    end = len(input_list) - 1
    return rot_arr_search_helper(input_list, number, start, end)


def rot_arr_search_helper(arr, num, start, end):
    mid = (start + end) // 2
    # see if start, mid, or end are num
    if arr[start] == num:
        return start
    elif arr[end] == num:
        return end
    elif arr[mid] == num:
        return mid
    # check if left half of arr is sorted
    elif arr[start] < arr[mid]:
        # check if num within range of sorted half
        if arr[start] < num < arr[mid]:
            return rot_arr_search_helper(arr, num, start + 1, mid - 1)
        else:
            return rot_arr_search_helper(arr, num, mid + 1, end - 1)
    # check if right half of arr is sorted
    elif arr[mid] < arr[end]:
        # check if num within range of sorted half
        if arr[mid] < num < arr[end]:
            return rot_arr_search_helper(arr, num, mid + 1, end - 1)
        else:
            return rot_arr_search_helper(arr, num, start + 1, mid - 1)
    else:
        return -1


# testing
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


# testing

def test_function(test_cases):
    for case in test_cases:
        if (linear_search(case[1], case[2]) ==
           rotated_array_search(case[1], case[2])):
            print("Test case " + case[0] + ": Pass!")
        else:
            print("Test case " + case[0] + ": FAIL.")


tc_1 = ("1", [6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4], 6)  # num is first
tc_2 = ("2", [6, 7, 8, 9, 10, 1, 2, 3, 4], 4)  # num is last
tc_3 = ("3", [6, 7, 8, 9, 10, 1, 2, 3, 4], 8)  # num in sorted left half
tc_4 = ("4", [6, 7, 8, 9, 10, 1, 2, 3, 4], 2)  # num in sorted right half
tc_5 = ("5", [8, 9, 10, 1, 2, 3, 4, 5, 6, 7], 10)  # num in unsorted left half
tc_6 = ("6", [6, 7, 8, 9, 10, 11, 3, 4, 5], 3)  # num in unsorted right half
tc_7 = ("7", [6, 7, 8, 1, 2, 3, 4], 1)  # num is middle of odd arr(len)
tc_8 = ("8", [6, 7, 8, 9, 1, 2, 3, 4], 1)  # num is middle of even arr(len)
tc_9 = ("9", [6, 7, 8, 1, 2, 3, 4], 10)  # num not in arr
tc_10 = ("10", [], 3)  # edge case empty list

test_cases = [tc_1, tc_2, tc_3, tc_4, tc_5, tc_6, tc_7, tc_8, tc_9, tc_10]
test_function(test_cases)
