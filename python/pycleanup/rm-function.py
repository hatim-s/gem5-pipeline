"""
Author: Hatim

Removes all instances of a function
"""

import sys

if len(sys.argv) != 4:
	print ("Usage: python3 rm-duplicate-return.py benchmark isa function")
	sys.exit(1)

benchmark = sys.argv[1].strip().lower()
isa = sys.argv[2].strip().lower()
function = sys.argv[3].strip()

merged_file_path = f"../../data/{benchmark}/temp/{benchmark}.{isa}.merged"
out_merged_path = f"../../data/{benchmark}/temp/{benchmark}.{isa}.out.merged"

with open(merged_file_path, 'r') as mergedfile, open(out_merged_path, 'w') as outfile:
	for line in mergedfile:
		line = line.strip()

		if line == "":
			continue

		_, _, _, func = line.split()

		if func != function:
			print(line, file=outfile)