import csv 

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def print_results():
    #  Mutable variables for easily requesting different calls/texts
    call_row = len(calls) - 1
    text_row = 0
    # Message for printing text data
    print("First record of texts, " + str(texts[text_row][0]) + " texts " + str  (texts[text_row][1]) + " at time " + str(texts[text_row][2]))
    # Message for printing call data
    print("Last record of calls, " + str(calls[call_row][0]) + " calls " + str(calls[call_row][1]) + " at time " + str(calls[call_row][2]) + ", lasting " + str(calls[call_row][3]) + " seconds")
 
print_results()
