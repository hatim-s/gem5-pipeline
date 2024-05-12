import sys

if len(sys.argv) != 2:
    print ("[ERR] Incorrect number of arguments.")
    print ("Usage: python3 script.py benchmark version")
    sys.exit(1)

# ISA = sys.argv[1].strip().lower()
benchmark = sys.argv[1].strip().lower()

for ISA in ['arm', 'x86']:
    pc_file     = f"../functions/pc-address/{ISA}/{benchmark}.pc.{ISA}"
    inst_file   = f"../data/{benchmark}/{benchmark}.{ISA}.trunc.inst"
    out_file    = f"../data/{benchmark}/{benchmark}.{ISA}.out.trunc.inst"

    dict = {}

    with open(pc_file, 'r') as file:
        for line in file:
            words = line.strip().split()
            addr = words[0].strip()
            label = words[1].strip()
            func = words[2].strip()

            dict[addr] = (func, label)

    ignore_lines = []
    with open(inst_file, 'r') as file:
        stack = []
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if line == "":
                continue

            words = line.split()
            dic = words[0].strip()
            addr = words[1].strip()

            label = dict[addr][1]

            if label == "call":
                stack.append([dict[addr][0], line_number])
            elif label == "ret" and stack and stack[-1][0] == dict[addr][0]:
                stack.pop()

            else:
                tempstr = "Empty Stack"

                print (f"[ERR] Top of stack does not match : {line_number} {stack[-1][0] if stack else tempstr} {dict[addr][0]}\n")
                pop_count = 0
                pop_elements = []

                # Iterate over the stack
                for index, (stack_name, _) in enumerate(reversed(stack)):
                    pop_count += 1
                    pop_elements.append(stack_name)

                    # Check if the current element matches the given name
                    if stack_name == dict[addr][0]:
                        pop_count -= 1
                        print(f"[LOG] Match found for {dict[addr][0]}. Popping {pop_count} elements : {pop_elements}.\n")

                        while pop_count :
                            stack.pop()
                            pop_count -= 1

                        stack.pop()
                        break

        print(f"Left over stack: {stack}")
        for st in stack:
            ignore_lines.append(st[-1])

    with open(inst_file, 'r') as infile, open(out_file, 'w') as outfile:
        for line_number, line in enumerate(infile, start=1):
            if line_number in ignore_lines:
                continue

            inst, pc, _, _ = line.split()
            print(line.strip(), file=outfile)
            # print(f"{inst} {pc}", file=outfile)

