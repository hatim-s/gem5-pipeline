# import sys
# import pandas as pd

# if len(sys.argv) != 2:
# 	print ("Usage: python3 extract-address.py benchmark")
# 	sys.exit(1)

# benchmark = sys.argv[1]
# benchmark = benchmark.strip().lower()

# stat_file = f"../../stats/{benchmark}.rawstat.csv"

# df = pd.read_csv(stat_file)
# # df.columns = ['function', 'arm_ticks', 'arm_insts', 'x86_ticks', 'x86_insts']

# total_ticks = 0
# migration_count = 0

# migration_ticks = 2 * 1e9 * 1e-6 * 100 * 500

# isa = 'x86'

# base = 0
# phase = 0
# while base < len(df):
#     base_insts = df.at[base, f'x86_insts']

#     index = base
#     while base_insts + 10000000 > df.at[index, f'x86_insts']:
#         index += 1

#         if index == len(df) - 1:
#             break

#     phase += 1
#     print(f"[INFO] Phase: {str(phase).ljust(4)} | base: {base} to index: {index} | isa: {isa}")

#     total_ticks += df.at[index, f'{isa}_ticks'] - df.at[base, f'{isa}_ticks']

#     base = index

#     if base == len(df) - 1:
#         break

#     base_insts = df.at[base, f'x86_insts']

#     isa_index = base
#     while base_insts + 10000000 > df.at[isa_index, f'x86_insts']:
#         isa_index += 1

#         if isa_index == len(df) - 1:
#             break

#     arm_ticks = df.at[isa_index, f'arm_ticks'] - df.at[base, f'arm_ticks']
#     x86_ticks = df.at[isa_index, f'x86_ticks'] - df.at[base, f'x86_ticks']
    
#     if isa == 'x86':
#         arm_ticks += migration_ticks

#         if arm_ticks < x86_ticks:
#             migration_count += 1
#             isa = 'arm'

#     else: # isa == 'arm'
#         x86_ticks += migration_ticks

#         if x86_ticks < arm_ticks:
#             migration_count += 1
#             isa = 'x86'


# print("Total ticks: ", total_ticks + migration_count * migration_ticks)
# print("# Migations: ", migration_count)

# with open(f"../../stats/coarse-grained.txt", 'a') as outfile:
#     print(f"{benchmark.ljust(20)}: {total_ticks + migration_count * migration_ticks} {migration_count}", file=outfile)

import sys
import pandas as pd
# import random

if len(sys.argv) != 2:
	print ("Usage: python3 extract-address.py benchmark")
	sys.exit(1)

benchmark = sys.argv[1]
benchmark = benchmark.strip().lower()

stat_file = f"../../stats/{benchmark}.rawstat.csv"

df = pd.read_csv(stat_file)
# df.columns = ['function', 'arm_ticks', 'arm_insts', 'x86_ticks', 'x86_insts']

total_ticks = 0
migration_count = 0

migration_ticks = int(2 * 1e9 * 1e-6 * 100 * 500)
phase_insts = 10000000      #10,000,000

isa = 'x86'

base = 0
phase = 0
while base < len(df):
    base_insts = df.at[base, f'x86_insts']

    index = base
    while base_insts + phase_insts > df.at[index, f'x86_insts']:
        index += 1

        if index == len(df) - 1:
            break

    phase += 1
    print(f"[INFO] Phase: {str(phase).ljust(4)} | base: {base} to index: {index} | isa: {isa}")

    total_ticks += df.at[index, f'{isa}_ticks'] - df.at[base, f'{isa}_ticks']

    base = index

    if base == len(df) - 1:
        break

    # predicting the next ISA 
    base_insts = df.at[base, f'x86_insts']

    index = base
    while base_insts + phase_insts > df.at[index, f'x86_insts']:
        index += 1

        if index == len(df) - 1:
            break

    arm_ticks = df.at[index, f'arm_ticks'] - df.at[base, f'arm_ticks']
    x86_ticks = df.at[index, f'x86_ticks'] - df.at[base, f'x86_ticks']
    
    if isa == 'x86':
        # coin_toss = random.random()
        # print(coin_toss)

        cond = (arm_ticks + migration_ticks) < x86_ticks
        # cond = cond if coin_toss < 0.9 else not cond

        if cond:
            migration_count += 1
            isa = 'arm'

    else: # isa == 'arm'
        # coin_toss = random.random()
        # print(coin_toss)

        cond = (x86_ticks + migration_ticks) < arm_ticks
        # cond = cond if coin_toss < 0.9 else not cond

        if cond:
            migration_count += 1
            isa = 'x86'


print("Total ticks: ", total_ticks + (migration_count * migration_ticks))
print("# Migations: ", migration_count)

with open(f"../../stats/coarse-grained-oracle.txt", 'a') as outfile:
    print(f"{benchmark.ljust(20)}: {total_ticks + (migration_count * migration_ticks)} {migration_count}", file=outfile)