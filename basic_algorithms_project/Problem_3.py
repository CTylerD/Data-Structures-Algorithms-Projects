def mergesort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1
    merged += left[left_index:]
    merged += right[right_index:]
    return merged


def rearrange_digits(input_list):
    if len(input_list) == 0 or len(input_list) == 1:
        return input_list
    sorted_list = mergesort(input_list)
    output_1 = ''
    output_2 = ''
    for idx in range(len(sorted_list) - 1, -1, -2):
        output_1 += str(sorted_list[idx])
    for jdx in range(len(sorted_list) - 2, -1, -2):
        output_2 += str(sorted_list[jdx])
    return [int(output_1), int(output_2)]


# testing

def test_function(test_cases):
    for case in test_cases:
        output = rearrange_digits(case[1])
        solution = case[2]
        if sum(output) == sum(solution):
            print("Test case " + case[0] + ": Pass!")
        else:
            print("Test case " + case[0] + ": FAIL.")


tc_1 = ("1", [1, 2, 3, 4, 5], [542, 31])  # odd number of digits
tc_2 = ("2", [4, 6, 2, 5, 9, 8], [964, 852])  # even number of digits
tc_3 = ("3", [2, 7], [7, 2])  # two digits
tc_4 = ("4", [9], [9])  # single digit
tc_5 = ("5", [], [])  # no digits

test_cases = [tc_1, tc_2, tc_3, tc_4, tc_5]
test_function(test_cases)
