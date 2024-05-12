"""
Author: Hatim

Merges corresponding lines from bench.isa.seq and bench.isa.common.inst
"""

import sys

if len(sys.argv) != 2:
    print("Usage: python3 script.py benchmark")
    print ("[ERR] Invalid usage. Refer the usage guidelines.")
    sys.exit(1)

def check(word, functions):
    return word in functions

benchmark = sys.argv[1].strip().lower()

for isa in ['arm', 'x86']:
    inst_file_path = f"../data/{benchmark}/temp/{benchmark}.{isa}.inst"
    pc_file = f"../functions/pc-address/{isa}/{benchmark}.pc.{isa}"

    pc_address_details = {}
    with open(pc_file, 'r') as pcfile:
        for line in pcfile:
            line = line.strip()

            pc, label, func = line.split()

            pc_address_details[pc] = {
                'label': label, 
                'func': func
            }

    merge_file = f"../data/{benchmark}/temp/{benchmark}.{isa}.merged"
    with open(inst_file_path, 'r') as instfile, open(merge_file, 'w') as mergefile:
        for line in instfile:
            line = line.strip()

            inst, pc = line.split()

            label = pc_address_details[pc]['label']
            func = pc_address_details[pc]['func']

            print(f"{inst} {pc} {label} {func}", file=mergefile)

    print (f"\033[92m[DONE] merge-call-seq.py: {isa} merge file generated. \033[0m")