def sqrt(number):
    if number < 0:
        return "This sqrt is not a real number!"
    low = 0
    high = number
    mid = (low + high) // 2
    return get_sqrt(number, low, mid, high)


def get_sqrt(num, low, mid, high):
    if num - mid**2 >= 0 and mid**2 + (2 * mid) >= num:
        return mid
    if mid**2 > num:
        high = mid - 1
        mid = (low + high) // 2
        return get_sqrt(num, low, mid, high)
    elif mid**2 < num:
        low = mid + 1
        mid = (low + high) // 2
        return get_sqrt(num, low, mid, high)


# testing

def test_function(test_cases):
    for test in test_cases:
        if test[1]:
            print("Test case " + test[0] + ": Pass!")
        else:
            print("Test case " + test[0] + ": FAIL.")


tc_1 = ("1", 3 == sqrt(9))  # correct sqrt
tc_2 = ("2", 0 == sqrt(0))  # correct sqrt for 0
tc_3 = ("3", 1 == sqrt(1))  # correct sqrt for 1
tc_4 = ("4", 5 == sqrt(35))  # rounded down to nearest int
tc_5 = ("5", 1000 == sqrt(1000073))  # rounded down to nearest int - large num
tc_6 = ("6", "This sqrt is not a real number!" == sqrt(-2))  # negative input

test_cases = [tc_1, tc_2, tc_3, tc_4, tc_5, tc_6]
test_function(test_cases)
