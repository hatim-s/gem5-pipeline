"""
Author: Hatim
Calculates the 100-million Coarse Grained (Actual) Ticks

Usage: python3 coarse-grained.by benchmark
"""

import sys
import pandas as pd
import random

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
print ("Migration Ticks: ", migration_ticks)
phase_insts = int(1e7)      #100,000,000

isa = 'x86'

base = 0
phase = 0
while base < len(df):
    base_insts = df.at[base, f'{isa}_insts']

    index = base
    while base_insts + phase_insts > df.at[index, f'{isa}_insts']:
        index += 1

        if index == len(df) - 1:
            break

    phase += 1
    print(f"[INFO] Phase: {str(phase).ljust(4)} | base: {base} to index: {index} | isa: {isa}")

    total_ticks += (df.at[index, f'{isa}_ticks'] - df.at[base, f'{isa}_ticks'])

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
    
    coin_toss = random.random()
    print(coin_toss)

    if isa == 'x86':
        should_migrate = arm_ticks + migration_ticks < x86_ticks
        should_migrate = should_migrate if coin_toss < 0.9 else not should_migrate

        if should_migrate:
            migration_count += 1
            isa = 'arm'

    else: # isa == 'arm'
        should_migrate = x86_ticks + migration_ticks < arm_ticks
        should_migrate = should_migrate if coin_toss < 0.9 else not should_migrate

        if should_migrate:
            migration_count += 1
            isa = 'x86'

total_ticks += (migration_count * migration_ticks)
print("Total ticks: ", total_ticks)
print("# Migations: ", migration_count)

with open(f"../../stats/coarse-grained.txt", 'a') as outfile:
    print(f"{benchmark.ljust(20)} {str(total_ticks).ljust(15)} {migration_count}", file=outfile)