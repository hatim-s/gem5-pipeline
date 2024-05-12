import sys

if len(sys.argv) != 3:
    print ("[ERR] Incorrect number of arguments.")
    print ("Usage: python3 script.py benchmark")
    sys.exit(1)

ISA = sys.argv[1]
ISA = ISA.strip().lower()

benchmark = sys.argv[2]
benchmark = benchmark.strip().lower()

pc_file     = f"../../functions/pc-address/{ISA}/{benchmark}.pc.{ISA}"
inst_file   = f"../../data/{benchmark}/temp/{benchmark}.{ISA}.merged"
dic_file    = f"../../data/{benchmark}/temp/{benchmark}.{ISA}.merged.dic"
seq_file    = f"../../data/{benchmark}/temp/{benchmark}.{ISA}.merged.seq"
log_file    = f"../../data/{benchmark}/temp/{benchmark}.{ISA}.merged.log"

stack = []
dict = {}

with open(pc_file, 'r') as file:
    for line in file:
        words = line.strip().split()
        addr = words[0].strip()
        label = words[1].strip()
        func = words[2].strip()

        dict[addr] = (func, label)

# print (dict)

with open(inst_file, 'r') as file, open(dic_file, 'w') as dicfile, open(seq_file, 'w') as seqfile, open(log_file, 'w') as logfile:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()
        if line == "":
            continue

        words = line.split()
        dic = words[0].strip()
        addr = words[1].strip()

        label = dict[addr][1]
        print(f"{label} {dict[addr][0]}", file=seqfile)

        if label == "call":
            stack.append([dict[addr][0], int(dic)])
        elif label == "ret" and stack and stack[-1][0] == dict[addr][0]:
            dic_count = int(dic) - stack[-1][1]
            print (f"{dict[addr][0]} {dic_count}", file=dicfile)
            stack.pop()

            for index, value in enumerate(stack):
                value[1] = value[1] + dic_count
        else:
            # if not stack: 
            #     print ("Stack Empty!")
            #     continue
            tempstr = "Empty Stack"

            print (f"[ERR] Top of stack does not match : {line_number} {stack[-1][0] if stack else tempstr} {dict[addr][0]}\n", file=logfile )
            pop_count = 0
            pop_elements = []
            # Iterate over the stack
            for index, (stack_name, _) in enumerate(reversed(stack)):
                pop_count += 1
                pop_elements.append(stack_name)

                # Check if the current element matches the given name
                if stack_name == dict[addr][0]:
                    pop_count -=1
                    print(f"Match found for {dict[addr][0]}. Popping {pop_count} elements : {pop_elements}.\n", file=logfile)

                    while pop_count :
                        stack.pop()
                        pop_count -=1

                    dic_count = int(dic) - stack[-1][1]
                    print (f"{dict[addr][0]} {dic_count}", file=dicfile)
                    stack.pop()

                    for index, value in enumerate(stack):
                        value[1] = value[1] + dic_count

                    break



