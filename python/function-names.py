import sys

if len(sys.argv) != 2:
    print ("[ERR] Incorrect number of arguments")
    print ("Usage: python3 script.py benchmark_name")
    sys.exit(1)

benchmark = sys.argv[1]
benchmark = benchmark.strip()

# print (benchmark, isa)

raw_file = f"../functions/dump/{benchmark}.func.dump"

arm_source_file = f"../bin/source/arm/{benchmark}.arm.txt"
x86_source_file = f"../bin/source/x86/{benchmark}.x86.txt"
dynamic_source_file = f"../bin/source/dynamic/{benchmark}.dynamic.txt"

out_file = f"../functions/names/{benchmark}.func.names"

function_names = []

with open(raw_file, 'r') as rawf:
    for line in rawf:
        line = line.strip()
        if line == "":
            continue

        if "Non-debugging symbols" in line:
            break

        if line[-1] == ';':
            try:
                # changed this for C++ benchmarks
                function_declaration = line.split(":")[-1].strip()
                type_and_name = function_declaration.split("(")[0].strip()

                function_name = type_and_name.split(" ")[-1].strip()
                function_name = function_name.split('::')[-1].strip()
                function_name = function_name.replace("*", "")
                function_names.append(function_name)
                            
            except Exception as e:
                print(f"[ERR] Something went wrong: {benchmark}")
                print(f"Parsing line: {line}")
                print(e)
                
                exit()
                
source_function_names = ['main']
with open(dynamic_source_file, 'r') as source:
    flag = False
    for line in source:
        if "Disassembly of section .text" in line:
            flag = True
            continue
        elif "Disassembly of section" in line:
            flag = True
            continue

        if not flag:
            continue

        if line.strip()[-2:] != ">:":
           continue

        source_name = line.split()[1][1:-2]
        
        found = False
        for name in function_names:
            if name in source_name:
                found = True
                break

        if not found:
            continue

        source_function_names.append(source_name)

function_called_arm = {}
for func in source_function_names:
    function_called_arm[func] = False

function_called_arm['main'] = True
with open(arm_source_file, 'r') as source:
    flag = False
    for line in source:
        if "Disassembly of section .text" in line:
            flag = True
            continue
        elif "Disassembly of section" in line:
            flag = False
            continue

        if not flag:
            continue

        line = line.strip().split()

        if len(line) >= 3 and line[2][0] == "b" and (
            line[-1][0] == "<" and line[-1][-1] == ">"
        ):
            label_called = line[-1][1:-1]

            if '+' in label_called:
                continue

            if label_called in function_called_arm.keys():
                function_called_arm[label_called] = True

function_called_x86 = {}
for func in source_function_names:
    function_called_x86[func] = False

function_called_x86['main'] = True
with open(x86_source_file, 'r') as source:
    flag = False
    for line in source:
        if "Disassembly of section .text" in line:
            flag = True
            continue
        elif "Disassembly of section" in line:
            flag = False
            continue

        if not flag:
            continue

        line = line.strip().split()

        if len(line) >= 3 and line[-3] == "call" and (
            line[-1][0] == "<" and line[-1][-1] == ">"
        ):
            label_called = line[-1][1:-1]

            if '+' in label_called:
                continue

            if label_called in function_called_x86.keys():
                function_called_x86[label_called] = True

with open(out_file, 'w') as outfile:
    for func in source_function_names:
        if (
            function_called_arm[func] == True 
            and function_called_x86[func] == True
        ):    
            print(func, file=outfile)