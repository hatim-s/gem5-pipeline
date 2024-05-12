"""
Author: Hatim

Reads function names from benchmark's function-name file and extracts PC
addresses for specified ISA.
"""

import sys

if len(sys.argv) != 2:
    print("Usage: python3 script.py benchmark isa")
    print ("[ERR] Invalid usage. Refer the usage guidelines.")
    sys.exit(1)

benchmark = sys.argv[1].strip().lower()

functions = []

function_file = f"../functions/pc-address/func/{benchmark}.func"

with open(function_file, 'r') as file:
    for line in file:
        line = line.strip()
        functions.append(line)

source_file = f"../bin/source/arm/{benchmark}.arm.txt"
equi_points = []

linked_return_functions = []

with open(source_file, 'r') as file:
    current_function = None
    flag = False
    lookout = False
    line_number = 0
    current_function = None
    for line in file:
        line_number += 1
        line = line.strip()

        if line == "":
            lookout = False
            continue

        if line == "Disassembly of section .text:":
            flag = True
        elif "Disassembly of section" in line:
            flag = False
            current_function = None

        if not flag:
            continue

        words = line.split()

        # pc <name>:
        if len(words) == 2 and words[-1][-1] == ":": # line containing a label
            if words[1][1:-2] in functions:
                current_function = words[1][1:-2]
            else:
                current_function = None

        elif len(words) > 3 and (
            "pop" == words[2][:3] and (
                "lr" in line[line.find('{') + 1:line.find("}")].split(', ')
            )
        ) and current_function != None:
            lookout = True
            continue

        elif lookout == True and words[2] == "b":
            print (f"\033[94m[INFO] remove-linked-return-functions.py: {current_function.rjust(20)}, line: {line_number-1} \033[0m")
            linked_return_functions.append(current_function)
            
        lookout = False


for isa in ['arm', 'x86']:
    merged_file_path = f"../data/{benchmark}/temp/{benchmark}.{isa}.merged"
    merged_out_file_path = f"../data/{benchmark}/temp/{benchmark}.{isa}.out.merged"

    with open(merged_file_path, 'r') as mergedfile, open(merged_out_file_path, 'w') as outfile:
        for line in mergedfile:
            line = line.strip()

            if line == "":
                continue

            _, _, _, func = line.split()

            if func in linked_return_functions:
                continue
            else:
                print(line, file=outfile)