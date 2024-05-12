"""
Author: Hatim

Reads function names from benchmark's function-name file and extracts PC
addresses for specified ISA.
"""

import sys

if len(sys.argv) != 3:
    print("Usage: python3 script.py benchmark isa")
    print ("[ERR] Invalid usage. Refer the usage guidelines.")
    sys.exit(1)

benchmark = sys.argv[1].strip().lower()
isa = sys.argv[2].strip().lower()

merged_inst_file_path = f"../data/{benchmark}/temp/{benchmark}.{isa}.merged"
merged_out_inst_file_path = f"../data/{benchmark}/temp/{benchmark}.{isa}.out.merged"

call_count = {}
return_count = {}

with open(merged_inst_file_path, 'r') as mergedfile:
    for line in mergedfile:
        line = line.strip()

        _, _, label, func = line.split()

        if label == "call":
            call_count[func] = call_count.get(func, 0) + 1
        else:
            return_count[func] = return_count.get(func, 0) + 1


functions = [func for func in call_count.keys() if func in return_count.keys()]

duplicate_return_functions = [func for func in functions if call_count[func] < return_count[func]]
print(f"\033[92m [DONE] remove-duplicate-returns.py: {isa} = {duplicate_return_functions}\033[0m")

line_sequence = {} # dictionary of arrays
for func in duplicate_return_functions:
    line_sequence[func] = []

line_number = 0
with open(merged_inst_file_path, 'r') as mergedfile:
    for line in mergedfile:
        line_number += 1

        line = line.strip()
        _, _, label, func = line.split()

        if label == "call" and func in duplicate_return_functions:
            line_sequence[func].append(line_number)
            line_sequence[func].append(-1)

        elif label == "ret" and func in duplicate_return_functions:
            line_sequence[func][-1] = line_number

line_number = 0

index = {}
for func in duplicate_return_functions:
    index[func] = 0

with open(merged_inst_file_path, 'r') as mergedfile, open(merged_out_inst_file_path, 'w') as outfile:
    for line in mergedfile:
        line_number += 1

        line = line.strip()
        _, _, label, func = line.split()

        if func not in duplicate_return_functions:
            print(line, file=outfile)
            continue

        if label == "call":
            print (line, file=outfile)
        else:
            if line_number == line_sequence[func][index[func]+1]:
                print (line, file=outfile)
                index[func] += 2

