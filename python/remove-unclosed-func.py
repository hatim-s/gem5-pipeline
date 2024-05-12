"""
Author: Hatim

Removes functions which do not have a return
"""

import sys

if len(sys.argv) != 3:
	print ("Usage: python3 rm-duplicate-return.py benchmark isa")
	sys.exit(1)

benchmark = sys.argv[1].strip().lower()
isa = sys.argv[2].strip().lower()
# function = sys.argv[3].strip()

merged_file_path = f"../data/{benchmark}/temp/{benchmark}.{isa}.merged"
out_merged_path = f"../data/{benchmark}/temp/{benchmark}.{isa}.out.merged"

function_call = {}
function_ret = {}

with open(merged_file_path, 'r') as mergedfile:
	for line in mergedfile:
		line = line.strip()

		if line == "":
			continue

		_, _, label, func = line.split()

		if label == "call":
			function_call[func] = function_call.get(func, 0) + 1
		else:
			function_ret[func] = function_ret.get(func, 0) + 1

call_functions = function_call.keys()
retn_functions = function_ret.keys()

remove_functions = [func for func in call_functions if func not in retn_functions]
print (remove_functions)

with open(merged_file_path, 'r') as mergedfile, open(out_merged_path, 'w') as outfile:
	for line in mergedfile:
		line = line.strip()

		if line == "":
			continue

		_, _, _, func = line.split()

		if func in remove_functions:
			continue

		print(line, file=outfile)