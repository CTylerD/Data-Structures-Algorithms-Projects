import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def count_phone_numbers():
    all_numbers = set()
    for idx, call in enumerate(calls):
        all_numbers.add(calls[idx][0])
        all_numbers.add(calls[idx][1])
    for idx, text in enumerate(texts):
        all_numbers.add(texts[idx][0])
        all_numbers.add(texts[idx][1])
    return len(all_numbers)


def print_total_numbers():
    total_numbers = count_phone_numbers()
    print("There are " + str(total_numbers) + " different telephone numbers in the records.")


print_total_numbers()
