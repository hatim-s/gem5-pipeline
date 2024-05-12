import sys

if len(sys.argv) != 2:
    print("Usage: python3 script.py benchmark")
    print ("[ERR] Invalid usage. Refer the usage guidelines.")
    sys.exit(1)

benchmark = sys.argv[1]
benchmark = benchmark.strip()

arm_functions = []
x86_functions = []  

arm_input_path = f"../functions/raw-pc-address/arm/{benchmark}.pc.arm"
x86_input_path = f"../functions/raw-pc-address/x86/{benchmark}.pc.x86"

with open(arm_input_path, 'r') as armfile:
    for line in armfile:
        line = line.strip()

        _, label, func = line.split()

        if label == "call":
            arm_functions.append(func)

with open(x86_input_path, 'r') as x86file:
    for line in x86file:
        line = line.strip()

        _, label, func = line.split()

        if label == "call":
            x86_functions.append(func)

# with open (f'../functions/pc-address/isa-func/{benchmark}.isa.func', 'w') as funcfile:
#     print("ARM functions: ", file=funcfile)
#     print(arm_functions, file=funcfile)
#     print(len(arm_functions))

#     print("\n\n\n\n\n\n", file=funcfile)

#     print("X86 functions: ", file=funcfile)
#     print(x86_functions, file=funcfile)
#     print(len(x86_functions))

#     diff_functions = [func for func in arm_functions if func not in x86_functions]
#     print ("Functions not in X86: ", diff_functions)

#     diff_functions = [func for func in x86_functions if func not in arm_functions]
#     print ("Functions not in ARM: ", diff_functions)

common_functions = [func for func in arm_functions if func in x86_functions]

dynamic_source_file = f"../bin/source/dynamic/{benchmark}.dynamic.txt"
with open(dynamic_source_file, 'r') as sourcefile:
    for line in sourcefile:
        line = line.strip()

        if line == "":
            continue

        if line == "Disassembly of section .text:":
            flag = True
            continue

        elif "Disassembly of section" in line:
            flag = False
            continue

        if not flag:
            continue

        if line[-1] == ":": # function call
            current_func = line.split()[1][1:-2]

            if current_func in common_functions:
                consider_function = True
                function_call_count[current_func] = 0
            else:
                consider_function = False

            continue

        if not consider_function:
            continue
            
        words = line.split()

        if "call" in words:
            call_func = words[-1][1:-1]

            if call_func in common_functions:
                function_call_count[current_func] += 1

print(f"\033[94m [INFO] dag.py: func_call_count: {function_call_count} \033[0m")

dag_functions = [func for func in function_call_count.keys() if function_call_count[func] > 0]

function_file = f"../functions/pc-address/func/{benchmark}.func"
with open(function_file, 'w') as funcfile:
    for func in dag_functions:
        print(func, file=funcfile)

arm_output_path = f"../functions/pc-address/arm/{benchmark}.pc.arm"
x86_output_path = f"../functions/pc-address/x86/{benchmark}.pc.x86"

with open(arm_input_path, 'r') as armin, open(arm_output_path, 'w') as armout:
    for line in armin:
        line = line.strip()

        funcname = line.split()[-1]
        if funcname in dag_functions:
            print(line, file=armout)

with open(x86_input_path, 'r') as x86in, open(x86_output_path, 'w') as x86out:
    for line in x86in:
        line = line.strip()

        funcname = line.split()[-1]
        if funcname in dag_functions:
            print(line, file=x86out)
        