"""
Author : Hatim

Remove functions from DIC file which are not common to both ARM and X86
"""

import sys

if len(sys.argv) < 2:
    print ("[ERR] Incorrect number of arguments.")
    print ("Usage: python3 script.py benchmark input-version [clean/trunc]")
    sys.exit(1)

benchmark = sys.argv[1].strip().lower()
warmup = int(sys.argv[2].strip().lower()) if len(sys.argv) == 3 else 1000000000
maxinsts = int(sys.argv[3].strip().lower()) if len(sys.argv) == 4 else None

inst_file_arm = f"../data/{benchmark}/temp/{benchmark}.arm.merged"
inst_file_x86 = f"../data/{benchmark}/temp/{benchmark}.x86.merged"

trunc_file_arm = f"../data/{benchmark}/{benchmark}.arm.trunc.inst"
trunc_file_x86 = f"../data/{benchmark}/{benchmark}.x86.trunc.inst"

# warmup = 1000000000

remove_count = 0

line_number = 0
line_number_flag = False

lines_written = 0
with open(inst_file_x86, 'r') as instx86, open(trunc_file_x86, 'w') as truncx86:
    stack = []
    for line in instx86:
        line_number += 1
        line = line.strip()

        if line == "":
            continue

        inst, pc, label, func = line.split()

        if int(inst) < warmup:
            remove_count += 1

            if label == "call":
                stack.append((func, True))
            else: # label == "ret"
                try:
                    stack.pop()
                except:
                    print(f"Error in line: {line_number}")
                    print("Stack: ", stack)
                    sys.exit()

        else:
            if not line_number_flag:
                print(line_number)
                # print(stack)
                line_number_flag = True

            if maxinsts and int(inst) > maxinsts:
                break
            
            if label == "call":
                stack.append((func, False))
                print(f"{line}", file=truncx86)
                lines_written += 1
                continue

            # label == "ret"

            if len(stack) > 0 and func == stack[-1][0] and stack[-1][1] == True:
                # print("", file=truncx86)
                stack.pop()
                continue
            
            print(f"{line}", file=truncx86)
            lines_written += 1
            stack.pop()

print("Lines printed: ", lines_written)

with open(inst_file_arm, 'r') as instarm, open(trunc_file_arm, 'w') as truncarm:
    stack = []
    for line in instarm:
        line = line.strip()

        if line == "":
            continue

        inst, pc, label, func = line.split()

        if remove_count > 0:
            remove_count -= 1

            if label == "call":
                stack.append((func, True))
            else:
                stack.pop()
            
        else:
            if label == "call":
                stack.append((func, False))
                print(f"{line}", file=truncarm)
                lines_written -= 1

                if lines_written == 0:
                    break
                continue

            # if maxinsts and int(inst) > maxinsts:
            #     break
            
            # label == "ret"
            if len(stack) > 0 and func == stack[-1][0] and stack[-1][1] == True:
                # print("", file=truncarm)
                stack.pop()
                continue
            
            print(f"{line}", file=truncarm)
            lines_written -= 1

            if lines_written == 0:
                break
            stack.pop()