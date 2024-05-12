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

# df = pd.read_csv(stat_file, header=None)
# df.columns = ['function', 'arm_ticks', 'arm_insts', 'x86_ticks', 'x86_insts']

migration_ticks = int(2 * 1e9 * 1e-6 * 0.04 * 500)
print ("Migration ticks: ", migration_ticks)

arm_cost = df.at[0, 'arm_ticks']
x86_cost = df.at[0, 'x86_ticks']

arm_migrations = 0
x86_migrations = 0

for index in range(1, len(df)):
    next_arm_cost = df.at[index, 'arm_ticks'] + min(arm_cost, x86_cost + migration_ticks * 2)
    next_x86_cost = df.at[index, 'x86_ticks'] + min(x86_cost, arm_cost + migration_ticks * 2)

    arm_migrations += int((x86_cost + migration_ticks * 2) < arm_cost) * 2
    x86_migrations += int((arm_cost + migration_ticks * 2) < x86_cost) * 2

    arm_cost = next_arm_cost
    x86_cost = next_x86_cost

total_ticks = min(arm_cost, x86_cost)
migration_count = arm_migrations if arm_cost < x86_cost else x86_migrations

print("Total ticks: ", total_ticks)
print("# Migations: ", migration_count)
print("# Rows: ", len(df))

with open(f"../../stats/function-oracle.txt", 'a') as outfile:
    print(f"{benchmark.ljust(20)} {str(total_ticks).ljust(15)} {migration_count}", file=outfile)