import sys
import csv

if len(sys.argv) != 2:
    print ("[ERR] Incorrect number of arguments")
    print ("Usage: python3 script.py benchmark")
    sys.exit(1)

benchmark = sys.argv[1]
benchmark = benchmark.strip().lower()

# ISA = 'arm'
ISA = 'x86'

stat_file = f"../bench-stats/{benchmark}.{ISA}.stat"
inst_file = f"../inputs/equipoints.txt"
# inst_file = f"../../../../data/{benchmark}/{benchmark}.{ISA}.common.inst"
pcaddr_file = f"../../../../functions/pc-address/{ISA}/{benchmark}.pc.{ISA}"
output_file = f"../bench-stats/{benchmark}.{ISA}.csv"
seq_file = f"../bench-stats/{benchmark}.{ISA}.seq"
log_file = f"../bench-stats/{benchmark}.{ISA}.log"

functions = {}

with open(pcaddr_file, 'r') as addr_file:
    for line in addr_file:
        line = line.strip().split()

        addr = line[0]
        label = line[1]
        name = line[2]

        functions[addr] = (name, label)

with open(stat_file, 'r') as statf, open(inst_file, 'r') as instf, open(output_file, 'w') as outf, open(seq_file, 'w') as seqfile, open(log_file, 'w') as logfile:
    statline = statf.readline()
    stack = []
    csvwriter = csv.writer(outf)
    
    line_number = 0
    while True:
        statline = statf.readline()
        if not statline:
            break
        
        line_number += 1
        # 1. Extracting one set of stats
        stats = []
        while statline.strip() != "":
            if "Begin" in statline or "End" in statline:
                statline = statf.readline()
                continue

            statline = statline.strip().split()
            stat = int(statline[1]) if not '.' in statline[1] else float(statline[1])
            stats.append(stat)

            statline = statf.readline()
        # print (stats)
            
        if len(stats) < 17:
            stats.insert(-1, 0)

        # 2. Extracting corresponding inst
        instline = instf.readline()

        if not instline:
            break

        instline = instline.strip().split()

        # print (instline)

        inst_value = int(instline[0])
        addr = instline[1]

        # 3. Getting Function Details
        func_name = functions[addr][0]
        label = functions[addr][1]
        print(f"{addr} {label} {func_name}", file=seqfile)

        if label == "call":
            stack.append([func_name, stats])
        elif label == "ret" and stack and stack[-1][0] == func_name:
            top = stack.pop()
            final_stats = [a-b for a, b in zip(stats, top[1])]

            row = [func_name]
            row.extend(final_stats[1:])
            csvwriter.writerow(row)

            for index, value in enumerate(stack):
                value[1] = [a+b for a, b in zip(value[1], final_stats)]
        else:
            emptyStack = "Stack is empty!\n"
            print (f"[ERR] Top of stack does not match : {line_number} {stack[-1][0] if stack else emptyStack} {func_name}\n", file=logfile )
            pop_count = 0
            # Iterate over the stack
            for index, (stack_name, _) in enumerate(reversed(stack)):
                pop_count += 1

                # Check if the current element matches the given name
                if stack_name == func_name:
                    pop_count -=1
                    print(f"Match found for {func_name}. Popping {pop_count} elements.\n", file=logfile)
                    
                    while pop_count :
                        stack.pop()
                        pop_count -=1

                    top = stack.pop()
                    final_stats = [a-b for a, b in zip(stats, top[1])]

                    row = [func_name]
                    row.extend(final_stats[1:])
                    csvwriter.writerow(row)

                    for index, value in enumerate(stack):
                        value[1] = [a+b for a, b in zip(value[1], final_stats)]
            
                    break

