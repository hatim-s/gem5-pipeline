"""
Author: Hatim
Extracts the PC-Addresses from the file generated by
`print-functions.py`. Assumes that the format is:
	PC-Address Label Function-Name
"""

import sys

if len(sys.argv) != 2:
	print ("Usage: python3 extract-inst benchmark")
	sys.exit(1)

benchmark = sys.argv[1].strip().lower()

for isa in ['arm', 'x86']:
	input_file = f"../data/{benchmark}/temp/{benchmark}.{isa}.merged"
	output_file = f"../data/{benchmark}/temp/{benchmark}.{isa}.inst"

	with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
		for line in infile:
			line = line.strip()
			
			if line == "":
				continue

			inst, addr, _, _ = line.split()

			print(f"{inst} {addr}", file=outfile)