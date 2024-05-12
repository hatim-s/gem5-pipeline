import sys

if len(sys.argv) != 3:
	print ("Usage: python3 extract-address.py benchmark")
	sys.exit(1)

benchmark = sys.argv[1]
benchmark = benchmark.strip().lower()

isa = sys.argv[2]
isa = isa.strip().lower()

inst_file = f"../data/{benchmark}/stats/{benchmark}.{isa}.inst"
trunc_inst_file = f"../data/{benchmark}/{benchmark}.{isa}.trunc.inst"

last_inst = 0
count = 0

remove_lines = []

with open(trunc_inst_file, 'r') as truncfile:
    stack = []
    for line_number, line in enumerate(truncfile):
        line = line.strip()

        if line == "":
            continue

        inst, _, label, func = line.split()
        inst = int(inst)

        if inst - last_inst <= 3:
            if label == "call":
                stack.append((func, line_number, True))
                count += 1
                last_inst = inst

                continue

            _, line_call, _ = stack[-1]
            stack.pop()

            remove_lines.append(line_call)
            remove_lines.append(line_number)

            count += 1
            last_inst = inst

            continue

        if label == "call":
            stack.append((func, line_number, False))
            last_inst = inst

            continue

        # label == "ret"
        _, line_call, remove_call = stack[-1]
        stack.pop()

        if remove_call == True:
            remove_lines.append(line_call)
            remove_lines.append(line_number)

        last_inst = inst

print(count)

for ISA in ['arm', 'x86']:
    trunc_inst_file = f"../data/{benchmark}/{benchmark}.{ISA}.trunc.inst"
    trunc_out_inst_file = f"../data/{benchmark}/{benchmark}.{ISA}.trunc.out.inst"

    with open(trunc_inst_file, 'r') as truncfile, open(trunc_out_inst_file, 'w') as outfile:
        for line_number, line in enumerate(truncfile):
            if line_number in remove_lines:
                print("", file=outfile)
                continue

            print(line, end="", file=outfile)