"""
Author : Hatim

Remove functions from DIC file which are not common to both ARM and X86
"""

import sys

if len(sys.argv) != 2:
    print ("[ERR] Incorrect number of arguments.")
    print ("Usage: python3 script.py benchmark input-version [clean/trunc]")
    sys.exit(1)

benchmark = sys.argv[1].strip().lower()

inst_file_arm = f"../data/{benchmark}/temp/{benchmark}.arm.inst"
inst_file_x86 = f"../data/{benchmark}/temp/{benchmark}.x86.inst"

pc_file_arm = f"../functions/pc-address/arm/{benchmark}.pc.arm"
pc_file_x86 = f"../functions/pc-address/x86/{benchmark}.pc.x86"

pcdictarm = {}
pcdictx86 = {}

# Reading PC - to - Functions ---------------------------------------------------------------
with open(pc_file_arm, 'r') as armpcfile:
    for line in armpcfile:
        line = line.strip()

        if line == "":
            continue

        # line = "0060ab70 call ptr_difference_const"

        pcaddr = line.split()[0]
        func = line.split()[2]

        pcdictarm[pcaddr] = func

with open(pc_file_x86, 'r') as x86pcfile:
    for line in x86pcfile:
        line = line.strip()

        if line == "":
            continue

        # line = "0060ab70 call ptr_difference_const"

        pcaddr = line.split()[0]
        func = line.split()[2]

        pcdictx86[pcaddr] = func

print("\033[92m[INFO] rm-diff-functions.py:\033[0m ARM and X86 PC Files read and PC Addresses Stored")

# Collecting common Functions ------------------------------------------------------------------
armfunc = []
x86func = []

with open(inst_file_arm, 'r') as armfile:
    for line in armfile:
        line = line.strip()

        if (line == ""):
            continue

        # line = "4782 00400520"
        pcaddr = line.split()[1]
        func = pcdictarm[pcaddr]

        if func not in armfunc:
            armfunc.append(func)

print("\033[92m[INFO] rm-diff-functions.py:\033[0m ARM Functions read")

with open(inst_file_x86, 'r') as x86file:
    for line in x86file:
        line = line.strip()

        if (line == ""):
            continue

        # line = "4782 00400520"
        pcaddr = line.split()[1]
        func = pcdictx86[pcaddr]

        if func not in x86func:
            x86func.append(func)

print("\033[92m[INFO] rm-diff-functions.py:\033[0m X86 Functions read")

# set containing common functions
commonFunc = [func for func in armfunc if func in x86func]

# TODO: create new file to put removed functions from .inst files
commonfile_arm_path = f"../data/{benchmark}/temp/{benchmark}.arm.common.inst"
commonfile_x86_path = f"../data/{benchmark}/temp/{benchmark}.x86.common.inst"

with open(commonfile_arm_path, 'w') as commonfilearm, open(inst_file_arm, 'r') as instfilearm: 
    for line in instfilearm:
        line = line.strip()
        if (line == ""):
            continue

        # line = "4782 00400520"
        pcaddr = line.split()[1]
        func = pcdictarm[pcaddr]

        if func in commonFunc:
            print (line, file=commonfilearm)

print("\033[92m[INFO] rm-diff-functions.py:\033[0m ARM common file generated")

with open(commonfile_x86_path, 'w') as commonfilex86, open(inst_file_x86, 'r') as instfilex86: 
    for line in instfilex86:
        line = line.strip()
        if (line == ""):
            continue

        # line = "4782 00400520"
        pcaddr = line.split()[1]
        func = pcdictx86[pcaddr]

        if func in commonFunc:
            print (line, file=commonfilex86)

print("\033[92m[INFO] rm-diff-functions.py:\033[0m X86 common file generated")