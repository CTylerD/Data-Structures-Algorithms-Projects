import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


### PART A


def create_codes_set():
    codes = set()
    for idx, call in enumerate(calls):
        if calls[idx][0][0:5] == "(080)":
            if calls[idx][1][0] == "7" or \
               calls[idx][1][0] == "8" or \
               calls[idx][1][0] == "9":
                codes.add(calls[idx][1][0:4])
            elif calls[idx][1][0] == "(":
                codes.add(calls[idx][1][1:4])
            elif calls[idx][1][0] == 1:
                codes.add("140")
    print_list(sorted(codes))


def print_list(list):
    print("The numbers called by people in Bangalore have codes:")
    for code in list:
        print(code, sep="\n")


create_codes_set()


### PART B


def total_calls():
    calls_from_blr = []
    for idx, call in enumerate(calls):
        if calls[idx][0][0:5] == "(080)":
            calls_from_blr.append(calls[idx][1][0:5])
    count_blr_to_blr(calls_from_blr)


def count_blr_to_blr(calls_from_blr):
    b2b_counter = 0
    for call in calls_from_blr:
        if call == "(080)":
            b2b_counter += 1
    percent_blr_to_blr(calls_from_blr, b2b_counter)


def percent_blr_to_blr(calls_from_blr, b2b_counter):
    total_calls = len(calls_from_blr)
    percentage = round((100 * (b2b_counter/total_calls)), 2)
    print_results(percentage)


def print_results(percentage):
    print(str(percentage) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


total_calls()
