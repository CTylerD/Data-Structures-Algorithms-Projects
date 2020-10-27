import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


calls_dict = {}


def build_calls_dict():
    for idx, call in enumerate(calls):
        # Make sure caller in dict
        calls_dict.setdefault(calls[idx][0], 0)
        calls_dict[calls[idx][0]] += int(calls[idx][3])
        calls_dict.setdefault(calls[idx][1], 0)
        calls_dict[calls[idx][1]] += int(calls[idx][3])
    print_results(calls_dict)
"""
        # Make sure receiver in dict
        if calls[idx][1] not in calls_dict:
            calls_dict.update({calls[idx][1] : int(calls[idx][3])})
        # Update dict minute total
        else:
            calls_dict[calls[idx][1]] += int(calls[idx][3])"""
    


def print_results(dict):
    chattiest_number = str(max(dict, key=dict.get))
    print(chattiest_number + " spent the longest time, " + str(dict.get(chattiest_number)) + " seconds, on the phone during September 2016.")


build_calls_dict()
