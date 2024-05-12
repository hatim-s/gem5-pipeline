#!/bin/bash
cd ../

mkdir -p functions/
mkdir -p functions/dump/

mkdir -p functions/names/

mkdir -p functions/raw-pc-address/
mkdir -p functions/raw-pc-address/arm/
mkdir -p functions/raw-pc-address/x86/

mkdir -p functions/pc-address/
mkdir -p functions/pc-address/arm/
mkdir -p functions/pc-address/x86/

# Extracting function names from GDB Dumps
cd python/

# C programs
python3 function-names.py mcf
python3 function-names.py xz
python3 function-names.py lbm
python3 function-names.py nab
python3 function-names.py specrand-fr
python3 function-names.py specrand-ir
# python3 function-names.py x264

# # C++ programs
# python3 function-names.py omnetpp
python3 function-names.py xalancbmk
# python3 function-names.py imagick
python3 function-names.py deepsjeng
python3 function-names.py leela
python3 function-names.py namd
# python3 function-names.py parest

# # C/C++ programs
# python3 function-names.py povray
# python3 function-names.py blender

# # SPEC2006 programs
python3 function-names.py bzip2
python3 function-names.py gobmk
# python3 function-names.py h264ref
# python3 function-names.py hmmer
python3 function-names.py libquantum
python3 function-names.py milc
python3 function-names.py sjeng

# python3 function-names.py povray-06
# python3 function-names.py omnetpp-06
python3 function-names.py mcf-06
python3 function-names.py namd-06
# python3 function-names.py specrand-998-06
# python3 function-names.py specrand-999-06
python3 function-names.py sphinx3

echo -e "\e[1;32m[DONE]\e[0m Extracted function names from GDB Dumps (benchmark.func.names)"
cd ../

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# Extracting pc-address with function-names
cd python/

# C programs
python3 pc-address.py mcf arm
python3 pc-address.py mcf x86
python3 pc-address.py xz arm
python3 pc-address.py xz x86
python3 pc-address.py lbm x86
python3 pc-address.py lbm arm
python3 pc-address.py nab arm
python3 pc-address.py nab x86
python3 pc-address.py specrand-fr arm
python3 pc-address.py specrand-fr x86
python3 pc-address.py specrand-ir arm
python3 pc-address.py specrand-ir x86
# python3 pc-address.py x264 x86
# python3 pc-address.py x264 arm

# # C++ programs
# python3 pc-address.py omnetpp x86
# python3 pc-address.py omnetpp arm
python3 pc-address.py xalancbmk x86
python3 pc-address.py xalancbmk arm
# python3 pc-address.py imagick x86
# python3 pc-address.py imagick arm
python3 pc-address.py deepsjeng arm
python3 pc-address.py deepsjeng x86
python3 pc-address.py leela arm
python3 pc-address.py leela x86
python3 pc-address.py namd arm
python3 pc-address.py namd x86
# python3 pc-address.py parest x86
# python3 pc-address.py parest arm

# # C/C++ programs
# python3 pc-address.py povray x86
# python3 pc-address.py povray arm
# python3 pc-address.py blender x86
# python3 pc-address.py blender arm

# # SPEC2006 programs
python3 pc-address.py bzip2 arm
python3 pc-address.py bzip2 x86
python3 pc-address.py gobmk arm
python3 pc-address.py gobmk x86
# python3 pc-address.py h264ref x86
# python3 pc-address.py h264ref arm
# python3 pc-address.py hmmer x86
# python3 pc-address.py hmmer arm
python3 pc-address.py libquantum arm
python3 pc-address.py libquantum x86
python3 pc-address.py milc arm
python3 pc-address.py milc x86
python3 pc-address.py sjeng arm
python3 pc-address.py sjeng x86

# python3 pc-address.py omnetpp-06 x86
# python3 pc-address.py omnetpp-06 arm
# python3 pc-address.py povray-06 x86
# python3 pc-address.py povray-06 arm
python3 pc-address.py mcf-06 arm
python3 pc-address.py mcf-06 x86
python3 pc-address.py namd-06 arm
python3 pc-address.py namd-06 x86
# python3 pc-address.py specrand-998-06 x86
# python3 pc-address.py specrand-998-06 arm
# python3 pc-address.py specrand-999-06 x86
# python3 pc-address.py specrand-999-06 arm
python3 pc-address.py sphinx3 x86
python3 pc-address.py sphinx3 arm

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# C programs
python3 pc-sync.py mcf
python3 pc-sync.py xz
python3 pc-sync.py lbm
python3 pc-sync.py imagick
python3 pc-sync.py nab
python3 pc-sync.py specrand-fr
python3 pc-sync.py specrand-ir
# python3 pc-sync.py x264

# # C++ programs
# python3 pc-sync.py omnetpp
python3 pc-sync.py xalancbmk
# python3 pc-sync.py imagick
python3 pc-sync.py deepsjeng
python3 pc-sync.py leela
python3 pc-sync.py namd
# python3 pc-sync.py parest

# # C/C++ programs
# python3 pc-sync.py povray
# python3 pc-sync.py blender

# # SPEC2006 programs
python3 pc-sync.py bzip2
python3 pc-sync.py gobmk
# python3 pc-sync.py h264ref
# python3 pc-sync.py hmmer
python3 pc-sync.py libquantum
python3 pc-sync.py milc
python3 pc-sync.py sjeng

# python3 pc-sync.py omnetpp-06
# python3 pc-sync.py povray-06
python3 pc-sync.py mcf-06
python3 pc-sync.py namd-06
# python3 pc-sync.py specrand-998-06
# python3 pc-sync.py specrand-999-06
python3 pc-sync.py sphinx3

cd ../
echo -e "\e[1;32m[DONE]\e[0m Created benchmark.pc.txt"
