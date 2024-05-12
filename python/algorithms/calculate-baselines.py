# """
# Author: Hatim
# """

# coarse_grained_file                     = f"../../stats/coarse-grained.txt"
# nkb_window_file                         = f"../../stats/nkb-window.txt"
# static_function_affinity_file           = f"../../stats/static-function-affinity.txt"
# static_function_affinity_oracle_file    = f"../../stats/static-function-affinity-oracle.txt"
# switch_spikes_file                      = f"../../stats/switch-spikes.txt"
# function_oracle_file                    = f"../../stats/function-oracle.txt"

# with (
#     open(coarse_grained_file, 'r') as coarsefile, 
#     open(nkb_window_file, 'r') as nkbfile, 
#     open(static_function_affinity_file, 'r') as staticfile, 
#     open(static_function_affinity_oracle_file, 'r') as staticoraclefile, 
#     open(switch_spikes_file, 'r') as switchspikesfile,
#     open(function_oracle_file, 'r') as oraclefile, 
# ):
#     gmean_nkb = 1
#     gmean_static = 1
#     gmean_static_oracle = 1
#     gmean_switch_spike = 1
#     gmean_func_oracle = 1

#     counter = 0

#     for (
#         coarseline, nkbline, staticline, staticoracleline, switchspikesline, oracleline
#     ) in zip(
#         coarsefile, nkbfile, staticfile, staticoraclefile, switchspikesfile, oraclefile
#     ):

#         if coarseline.strip() == "":
#             break

#         benchmark, ticks_coarse, _  = coarseline.strip().split()

#         if benchmark in ['sjeng']:
#             continue

#         _, ticks_nkb, _             = nkbline.strip().split()
#         _, ticks_static, _          = staticline.strip().split()
#         _, ticks_static_oracle, _   = staticoracleline.strip().split()
#         _, ticks_switch_spike, _    = switchspikesline.strip().split()
#         _, ticks_func_oracle, _     = oracleline.strip().split()

#         ticks_coarse             = int(ticks_coarse)
#         speed_nkb                = ticks_coarse / int(ticks_nkb)
#         speed_static             = ticks_coarse / int(ticks_static)
#         speed_static_oracle      = ticks_coarse / int(ticks_static_oracle)
#         speed_switch_spike       = ticks_coarse / int(ticks_switch_spike)
#         speed_func_oracle        = ticks_coarse / int(ticks_func_oracle)

#         gmean_nkb *= speed_nkb
#         gmean_static *= speed_static
#         gmean_static_oracle *= speed_static_oracle
#         gmean_switch_spike *= speed_switch_spike
#         gmean_func_oracle *= speed_func_oracle

#         speed_nkb = str(speed_nkb)
#         speed_static = str(speed_static)
#         speed_static_oracle = str(speed_static_oracle)
#         speed_switch_spike = str(speed_switch_spike)
#         speed_func_oracle = str(speed_func_oracle)

#         print (f"{benchmark.ljust(20)}: {speed_nkb.ljust(25)} {speed_static.ljust(25)} {speed_static_oracle.ljust(25)} {speed_switch_spike.ljust(25)} {speed_func_oracle.ljust(25)}")

#         counter += 1

#     gmean_nkb = gmean_nkb ** (1/counter)
#     gmean_static = gmean_static ** (1/counter)
#     gmean_static_oracle = gmean_static_oracle ** (1/counter)
#     gmean_switch_spike = gmean_switch_spike ** (1/counter)
#     gmean_func_oracle = gmean_func_oracle ** (1/counter)

#     print (f"{'gmean'.ljust(20)}: {str(gmean_nkb).ljust(25)} {str(gmean_static).ljust(25)} {str(gmean_static_oracle).ljust(25)} {str(gmean_switch_spike).ljust(25)} {str(gmean_func_oracle).ljust(25)}")






"""
Author: Hatim
"""

coarse_grained_file                     = f"../../stats/coarse-grained.txt"
nkb_window_file                         = f"../../stats/nkb-window.txt"
function_oracle_file                    = f"../../stats/function-oracle.txt"

with (
    open(coarse_grained_file, 'r') as coarsefile, 
    open(nkb_window_file, 'r') as nkbfile,
    open(function_oracle_file, 'r') as oraclefile, 
):
    gmean_nkb = 1
    gmean_func_oracle = 1

    counter = 0

    for (
        coarseline, nkbline, oracleline
    ) in zip(
        coarsefile, nkbfile, oraclefile
    ):

        if coarseline.strip() == "":
            break

        benchmark, ticks_coarse, _  = coarseline.strip().split()

        if benchmark in ['sjeng', 'xz']:
            continue

        _, ticks_nkb, _             = nkbline.strip().split()
        _, ticks_func_oracle, _     = oracleline.strip().split()

        ticks_coarse             = int(ticks_coarse)
        speed_nkb                = ticks_coarse / int(ticks_nkb)
        speed_func_oracle        = ticks_coarse / int(ticks_func_oracle)

        gmean_nkb *= speed_nkb
        gmean_func_oracle *= speed_func_oracle

        speed_nkb = str(speed_nkb)
        speed_func_oracle = str(speed_func_oracle)

        print (f"{benchmark.ljust(20)}: {speed_nkb.ljust(25)} {speed_func_oracle.ljust(25)}")

        counter += 1

    gmean_nkb = gmean_nkb ** (1/counter)
    gmean_func_oracle = gmean_func_oracle ** (1/counter)

    print (f"{'gmean'.ljust(20)}: {str(gmean_nkb).ljust(25)} {str(gmean_func_oracle).ljust(25)}")

