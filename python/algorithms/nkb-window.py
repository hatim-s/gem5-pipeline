import sys
import pandas as pd

if len(sys.argv) != 2:
	print ("Usage: python3 extract-address.py benchmark")
	sys.exit(1)

benchmark = sys.argv[1]
benchmark = benchmark.strip().lower()

stat_file = f"../../stats/{benchmark}.funcstat.csv"

df = pd.read_csv(stat_file)
df.columns = ['function', 'arm_ticks', 'arm_insts', 'x86_ticks', 'x86_insts']

migration_ticks = int(2 * 1e9 * 1e-6 * 0.04 * 500)
print ("Migration ticks: ", migration_ticks)

func_isa = {}
func_window_index = {}
func_time_19 = {}

for func in df.function.unique():
    func_isa[func] = 'x86'
    func_window_index[func] = 1
    func_time_19[func] = 0

window_nkb = 20

total_ticks = 0
migration_count = 0

current_isa = 'x86'

for index, row in df.iterrows():
    func = row.function

    f_isa = func_isa[func]
    f_index = func_window_index[func]

    if f_index <= window_nkb - 1:
        total_ticks += row[f'{f_isa}_ticks']
        func_window_index[func] = f_index + 1

        if current_isa != f_isa:
            migration_count += 2

        current_isa = f_isa

        if f_index == window_nkb - 1:
            func_time_19[func] = row[f'{f_isa}_ticks']

        continue

    f_isa = 'x86' if f_isa == 'arm' else 'arm'

    total_ticks += row[f'{f_isa}_ticks']
    func_window_index[func] = 1

    if current_isa != f_isa:
        migration_count += 2

    current_isa = f_isa

    time_19 = func_time_19[func]
    time_20 = row[f'{f_isa}_ticks']

    if time_19 < time_20:
        f_isa = 'x86' if f_isa == 'arm' else 'arm'

    func_isa[func] = f_isa

total_ticks += (migration_count * migration_ticks)

print("Total ticks: ", total_ticks)
print("# Migations: ", migration_count)
print("# Rows: ", len(df))

with open(f"../../stats/nkb-window.txt", 'a') as outfile:
    print(f"{benchmark.ljust(20)} {str(total_ticks).ljust(15)} {migration_count}", file=outfile)