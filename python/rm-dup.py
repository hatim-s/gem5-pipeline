# Author : Arif/Hatim
# Used to remove duplicates from inst-count.txt files

import sys

if len(sys.argv) != 2:
    print("Usage: python script.py benchmark")
    sys.exit(1)

benchmark = sys.argv[1]
benchmark = benchmark.strip().lower()

# ISA = 'arm'
# ISA = 'x86'

input_file_path = f"../outputs/inst-count.txt"
prev_line = None

output_file = f"../bench-stats/{benchmark}.inst"
with open(input_file_path, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        current_line = line.strip()
        if current_line == "":
            continue

        if current_line != prev_line:
            outfile.write(line)
            prev_line = current_line
