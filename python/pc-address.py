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

def check(word, functions):
    return word in functions

def search(words, key="pc"):
    for word in words:
        if word[:2] == key:
            return True
    return False

benchmark = sys.argv[1].strip().lower()
isa = sys.argv[2].strip().lower()

functions = []

function_file = f"../functions/names/{benchmark}.func.names"

try:
    with open(function_file, 'r') as file:
        for line in file:
            line = line.strip()
            functions.append(line)

except FileNotFoundError:
    print (f"[Err] {function_file} not found.\n")

except Exception as E:
    print (f"[Err] Unexpected error occurred: {E}\n")

source_file = f"../bin/source/{isa}/{benchmark}.{isa}.txt"
equi_points = []

try:
    with open(source_file, 'r') as file:
        current_function = None
        flag = False
        for line in file:
            line = line.strip()

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
                if check(words[1][1:-2], functions):
                    current_function = words[1][1:-2]

                    pc_address = words[0]
                    label = "call"

                    if isa == "x86":
                        equi_points.append({
                            "pc_address": "{:0>16}".format(pc_address)[-16:],
                            "label": label,
                            "function_name": current_function
                        })
                    else: # isa == "arm"
                        equi_points.append({
                            "pc_address": "{:0>8}".format(pc_address)[-8:],
                            "label": label,
                            "function_name": current_function
                        })
                else:
                    current_function = None

            elif isa == "x86" and "ret" in words and current_function != None:
                pc_address = "{:0>16}".format(words[0][:-1])
                label = "ret "

                equi_points.append({
                    "pc_address": pc_address,
                    "label": label,
                    "function_name": current_function
                })

            elif isa == "arm" and len(words) > 3 and (
                ("bx" == words[2][0:2] and "lr" == words[3]) or 
                ("pop" == words[2][0:3] and search(words, 'pc'))
            ) and current_function != None:
                pc_address = "{:0>8}".format(words[0][:-1])
                label = "ret "

                equi_points.append({
                    "pc_address": pc_address,
                    "label": label,
                    "function_name": current_function
                })

                
except FileNotFoundError:
    print (f"[Err] {source_file} not found.")
except Exception as E:
    print (f"[Err] Unexpected error occurred: {E}")
    print (f"ISA: {isa}")

for point in equi_points:
    label = point.label
    pcaddr = point.pc_address
    func = point.function_name

    if label == "call":
        call_dict[func] = pcaddr

    else:
        if func in ret_dict.keys():
            ret_dict[func].append(pcaddr)
        else:
            ret_dict[func] = [pcaddr]

out_file_path = f"../functions/raw-pc-address/{isa}/{benchmark}.pc.{isa}"

call_functions = call_dict.keys()
retn_functions = ret_dict.keys()

functions_with_returns = [func for func in call_functions if func in retn_functions]
functions_with_diff_call_rets = [func for func in functions_with_returns if call_dict[func] not in ret_dict[func]]

with open(out_file_path, 'w') as outfile:
    for function in functions_with_diff_call_rets:
        print(f"{call_dict[function]} call {function}", file=outfile)
        for ret_addr in ret_dict[function]:
            print(f"{ret_addr} ret  {function}", file=outfile)
