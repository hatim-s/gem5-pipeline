import sys
import csv

if len(sys.argv) != 2:
    print ("[ERR] Incorrect number of arguments")
    print ("Usage: python3 script.py benchmark")
    sys.exit(1)

benchmark = sys.argv[1].strip().lower()

arm_siminsts_file = f"../data/{benchmark}/stats/{benchmark}.arm.inst"
x86_siminsts_file = f"../data/{benchmark}/stats/{benchmark}.x86.inst"

arm_simticks_file = f"../data/{benchmark}/stats/{benchmark}.arm.tick"
x86_simticks_file = f"../data/{benchmark}/stats/{benchmark}.x86.tick"

trunc_inst_file = f"../data/{benchmark}/{benchmark}.arm.trunc.inst"

stat_file_out = f"../stats/{benchmark}.rawstat.csv"

with (
    open(arm_siminsts_file, 'r') as arminstfile, 
    open(arm_simticks_file, 'r') as armtickfile, 
    open(x86_siminsts_file, 'r') as x86instfile, 
    open(x86_simticks_file, 'r') as x86tickfile, 
    open(trunc_inst_file, 'r') as truncfile,
    open(stat_file_out, 'w') as outfile
):
    csvwriter = csv.writer(outfile)
    csvwriter.writerow(['function', 'arm_ticks', 'arm_insts', 'x86_ticks', 'x86_insts'])

    for (
        linetrunc, linearminst, linearmtick, 
        linex86inst, linex86tick
    ) in zip(
        truncfile, arminstfile, armtickfile, 
        x86instfile, x86tickfile
    ):
        linetrunc = linetrunc.strip()

        linearminst = linearminst.strip()
        linearmtick = linearmtick.strip()

        linex86inst = linex86inst.strip()
        linex86tick = linex86tick.strip()

        _, _, label, func = linetrunc.split()

        if label == "ret":
            continue

        _, arminst = linearminst.split()
        _, armtick = linearmtick.split()

        _, x86inst = linex86inst.split()
        _, x86tick = linex86tick.split()

        row = [func, armtick, arminst, x86tick, x86inst]

        # print(f"{armtick} {arminst} {x86tick} {x86inst}", file=outfile)
        csvwriter.writerow(row)