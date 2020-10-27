import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def create_lists_of_users():
    outgoing_callers = set()
    not_telemarketers = set()
    for idx, call in enumerate(calls):
        outgoing_callers.add(calls[idx][0])
        not_telemarketers.add(calls[idx][1])
    for idx, text in enumerate(texts):
        not_telemarketers.add(texts[idx][0])
        not_telemarketers.add(texts[idx][1])
    find_telemarketers(outgoing_callers, not_telemarketers)


def find_telemarketers(out_calls, not_telemarketers):
    potential_telemarketers = out_calls.difference(not_telemarketers)
    print_results(potential_telemarketers)


def print_results(potential_telemarketers):
    print("These numbers could be telemarketers:")
    for number in sorted(potential_telemarketers):
        print(number, sep="\n")


create_lists_of_users()
