import sys
import csv

if len(sys.argv) != 2:
    print("Usage: python3 script.py benchmark")
    print ("[ERR] Invalid usage. Refer the usage guidelines.")
    sys.exit(1)

benchmark = sys.argv[1].strip().lower()

arm_csv_file = f"../data/{benchmark}/{benchmark}.arm.csv"
x86_csv_file = f"../data/{benchmark}/{benchmark}.x86.csv"
trunc_file = f"../data/{benchmark}/{benchmark}.arm.trunc.inst"

function_call_index = {}
with (
    open(trunc_file, 'r') as truncfile, 
    open(arm_csv_file, 'r') as armcsvfile, 
    open(x86_csv_file, 'r') as x86csvfile
):
    stack = []
    for line_number, line in enumerate(truncfile):
        line = line.strip()

        _, _, label, func = line.split()

        if label == "call":
            stack.append((func, line_number))
            continue

        # label == 'ret'
        line = armcsvfile.readline()
        line = line.split(',')

        try:
            armticks = line[1]
        except:
            print(line, line_number)

        arminsts = line[5]

        line = x86csvfile.readline()
        line = line.split(',')

        try:
            x86ticks = line[1]
            x86insts = line[5]
        except:
            print(line)
            sys.exit()

        call_index = stack[-1][1]
        stack.pop()

        function_call_index[call_index] = [func, armticks, arminsts, x86ticks, x86insts]

func_stat_file = f"../stats/{benchmark}.funcstat.csv"
with open(func_stat_file, 'w') as statfile:
    indexes = list(function_call_index.keys())
    indexes.sort()

    csvwriter = csv.writer(statfile)
    csvwriter.writerow(['function', 'arm_ticks', 'arm_insts', 'x86_ticks', 'x86_insts'])

    for index in indexes:
        row = function_call_index[index]
        # print(f"{func} {armticks} {arminsts} {x86ticks} {x86insts}", file=statfile)
        csvwriter.writerow(row)