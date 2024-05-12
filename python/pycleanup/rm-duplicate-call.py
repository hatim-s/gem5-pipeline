"""
Author: Hatim

Removes continous duplicates of input function's returns
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

line_sequence = [-1]
line_number = 0
with open(merged_file_path, 'r') as mergedfile:
	for line in mergedfile:
		line = line.strip()
		line_number += 1

		if line == "":
			continue

		_, _, label, func = line.split()

		if label == "call" and func == function:
			line_sequence[-1] = line_number
			# line_sequence.append(-1)
		elif label == "ret" and func == function:
			line_sequence.append(line_number)
			line_sequence.append(-1)

print (line_sequence[:100])

line_number = 0
index = 0
with open(merged_file_path, 'r') as mergedfile, open(out_merged_path, 'w') as outfile:
	for line in mergedfile:
		line_number += 1
		line = line.strip()

		if line == "":
			print("", file=outfile)
			continue

		_, _, label, func = line.split()

		if func != function:
			print(line, file=outfile)
			continue

		if label == "ret":
			print (line, file=outfile)
			index += 1
		else:
			if line_number == line_sequence[index]:
				print (line, file=outfile)
				index += 1
			else:
				print ("", file=outfile)

		