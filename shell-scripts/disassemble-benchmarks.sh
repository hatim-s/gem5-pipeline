#/bin/bash
cd ../

mkdir -p source/

# Disassembling static binaries - X86
cd bin/
mkdir -p source/x86/
cd x86/

# # SPEC2017 benchmarks

objdump -d "lbm.x86"            > "../source/x86/lbm.x86.txt"
objdump -d "mcf.x86"            > "../source/x86/mcf.x86.txt"
objdump -d "nab.x86"            > "../source/x86/nab.x86.txt"
objdump -d "specrand-fr.x86"    > "../source/x86/specrand-fr.x86.txt"
objdump -d "specrand-ir.x86"    > "../source/x86/specrand-ir.x86.txt"
objdump -d "xz.x86"             > "../source/x86/xz.x86.txt"
# objdump -d "x264.x86"           > "../source/x86/x264.x86.txt"

# objdump -d "blender.x86"        > "../source/x86/blender.x86.txt"
objdump -d "deepsjeng.x86"      > "../source/x86/deepsjeng.x86.txt"
objdump -d "leela.x86"          > "../source/x86/leela.x86.txt"
objdump -d "namd.x86"           > "../source/x86/namd.x86.txt"
# objdump -d "omnetpp.x86"        > "../source/x86/omnetpp.x86.txt"
# objdump -d "parest.x86"         > "../source/x86/parest.x86.txt"
# objdump -d "povray.x86"         > "../source/x86/povray.x86.txt"
objdump -d "xalancbmk.x86"      > "../source/x86/xalancbmk.x86.txt"
# objdump -d "imagick.x86"        > "../source/x86/imagick.x86.txt"

# SPEC2006 benchmarks
objdump -d "bzip2.x86"          > "../source/x86/bzip2.x86.txt"
objdump -d "gobmk.x86"          > "../source/x86/gobmk.x86.txt"
# objdump -d "h264ref.x86"        > "../source/x86/h264ref.x86.txt"
# objdump -d "hmmer.x86"          > "../source/x86/hmmer.x86.txt"
objdump -d "libquantum.x86"     > "../source/x86/libquantum.x86.txt"
objdump -d "milc.x86"           > "../source/x86/milc.x86.txt"
objdump -d "sjeng.x86"          > "../source/x86/sjeng.x86.txt"

# objdump -d "povray-06.x86"         > "../source/x86/povray-06.x86.txt"
# objdump -d "omnetpp-06.x86"        > "../source/x86/omnetpp-06.x86.txt"
objdump -d "mcf-06.x86"             > "../source/x86/mcf-06.x86.txt"
objdump -d "namd-06.x86"            > "../source/x86/namd-06.x86.txt"
objdump -d "sphinx3.x86"            > "../source/x86/sphinx3.x86.txt"
# objdump -d "specrand-998-06.x86"    > "../source/x86/specrand-998-06.x86.txt"
# objdump -d "specrand-999-06.x86"    > "../source/x86/specrand-999-06.x86.txt"

cd ../../
echo -e "\e[1;32m[DONE]\e[0m Disassembled x86 source codes"

# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

# Disassembling static binaries - ARM
cd bin/
mkdir -p source/arm/
cd arm/

# SPEC2017 benchmarks
arm-linux-gnueabi-objdump -d "lbm.arm"              > "../source/arm/lbm.arm.txt"
arm-linux-gnueabi-objdump -d "mcf.arm"              > "../source/arm/mcf.arm.txt"
arm-linux-gnueabi-objdump -d "nab.arm"              > "../source/arm/nab.arm.txt"
arm-linux-gnueabi-objdump -d "specrand-fr.arm"      > "../source/arm/specrand-fr.arm.txt"
arm-linux-gnueabi-objdump -d "specrand-ir.arm"      > "../source/arm/specrand-ir.arm.txt"
arm-linux-gnueabi-objdump -d "xz.arm"               > "../source/arm/xz.arm.txt"
# arm-linux-gnueabi-objdump -d "x264.arm"             > "../source/arm/x264.arm.txt"

# arm-linux-gnueabi-objdump -d "blender.arm"          > "../source/arm/blender.arm.txt"
arm-linux-gnueabi-objdump -d "deepsjeng.arm"        > "../source/arm/deepsjeng.arm.txt"
arm-linux-gnueabi-objdump -d "leela.arm"            > "../source/arm/leela.arm.txt"
arm-linux-gnueabi-objdump -d "namd.arm"             > "../source/arm/namd.arm.txt"
# arm-linux-gnueabi-objdump -d "omnetpp.arm"          > "../source/arm/omnetpp.arm.txt"
# arm-linux-gnueabi-objdump -d "parest.arm"           > "../source/arm/parest.arm.txt"
# arm-linux-gnueabi-objdump -d "povray.arm"           > "../source/arm/povray.arm.txt"
arm-linux-gnueabi-objdump -d "xalancbmk.arm"        > "../source/arm/xalancbmk.arm.txt"
# arm-linux-gnueabi-objdump -d "imagick.arm"        > "../source/arm/imagick.arm.txt"

# SPEC2006 benchmarks
arm-linux-gnueabi-objdump -d "bzip2.arm"            > "../source/arm/bzip2.arm.txt"
arm-linux-gnueabi-objdump -d "gobmk.arm"            > "../source/arm/gobmk.arm.txt"
# arm-linux-gnueabi-objdump -d "h264ref.arm"          > "../source/arm/h264ref.arm.txt"
# arm-linux-gnueabi-objdump -d "hmmer.arm"            > "../source/arm/hmmer.arm.txt"
arm-linux-gnueabi-objdump -d "libquantum.arm"       > "../source/arm/libquantum.arm.txt"
arm-linux-gnueabi-objdump -d "milc.arm"             > "../source/arm/milc.arm.txt"
arm-linux-gnueabi-objdump -d "sjeng.arm"            > "../source/arm/sjeng.arm.txt"

# arm-linux-gnueabi-objdump -d "omnetpp-06.arm"          > "../source/arm/omnetpp-06.arm.txt"
# arm-linux-gnueabi-objdump -d "povray-06.arm"           > "../source/arm/povray-06.arm.txt"
arm-linux-gnueabi-objdump -d "mcf-06.arm"             > "../source/arm/mcf-06.arm.txt"
arm-linux-gnueabi-objdump -d "namd-06.arm"            > "../source/arm/namd-06.arm.txt"
arm-linux-gnueabi-objdump -d "sphinx3.arm"            > "../source/arm/sphinx3.arm.txt"
# arm-linux-gnueabi-objdump -d "specrand-998-06.arm"    > "../source/arm/specrand-998-06.arm.txt"
# arm-linux-gnueabi-objdump -d "specrand-999-06.arm"    > "../source/arm/specrand-999-06.arm.txt"

cd ../../
echo -e "\e[1;32m[DONE]\e[0m Disassembled arm source codes"


# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------


# Disassembling dynamic X86 binaries
cd bin/
mkdir -p source/dynamic/
cd dynamic/

# # SPEC2017 benchmarks
objdump -d "lbm.dynamic"            > "../source/dynamic/lbm.dynamic.txt"
objdump -d "mcf.dynamic"            > "../source/dynamic/mcf.dynamic.txt"
objdump -d "nab.dynamic"            > "../source/dynamic/nab.dynamic.txt"
objdump -d "specrand-fr.dynamic"    > "../source/dynamic/specrand-fr.dynamic.txt"
objdump -d "specrand-ir.dynamic"    > "../source/dynamic/specrand-ir.dynamic.txt"
objdump -d "xz.dynamic"             > "../source/dynamic/xz.dynamic.txt"
# objdump -d "x264.dynamic"           > "../source/dynamic/x264.dynamic.txt"

# objdump -d "blender.dynamic"        > "../source/dynamic/blender.dynamic.txt"
objdump -d "deepsjeng.dynamic"      > "../source/dynamic/deepsjeng.dynamic.txt"
objdump -d "leela.dynamic"          > "../source/dynamic/leela.dynamic.txt"
objdump -d "namd.dynamic"           > "../source/dynamic/namd.dynamic.txt"
# objdump -d "omnetpp.dynamic"        > "../source/dynamic/omnetpp.dynamic.txt"
# objdump -d "parest.dynamic"         > "../source/dynamic/parest.dynamic.txt"
# objdump -d "povray.dynamic"         > "../source/dynamic/povray.dynamic.txt"
objdump -d "xalancbmk.dynamic"      > "../source/dynamic/xalancbmk.dynamic.txt"
# objdump -d "imagick.dynamic"      > "../source/dynamic/imagick.dynamic.txt"

# # SPEC2006 benchmarks
objdump -d "bzip2.dynamic"          > "../source/dynamic/bzip2.dynamic.txt"
objdump -d "gobmk.dynamic"          > "../source/dynamic/gobmk.dynamic.txt"
# objdump -d "h264ref.dynamic"        > "../source/dynamic/h264ref.dynamic.txt"
# objdump -d "hmmer.dynamic"          > "../source/dynamic/hmmer.dynamic.txt"
objdump -d "libquantum.dynamic"     > "../source/dynamic/libquantum.dynamic.txt"
objdump -d "milc.dynamic"           > "../source/dynamic/milc.dynamic.txt"
objdump -d "sjeng.dynamic"          > "../source/dynamic/sjeng.dynamic.txt"

# objdump -d "omnetpp-06.dynamic"        > "../source/dynamic/omnetpp-06.dynamic.txt"
# objdump -d "povray-06.dynamic"         > "../source/dynamic/povray-06.dynamic.txt"
objdump -d "mcf-06.dynamic"             > "../source/dynamic/mcf-06.dynamic.txt"
objdump -d "namd-06.dynamic"            > "../source/dynamic/namd-06.dynamic.txt"
objdump -d "sphinx3.dynamic"            > "../source/dynamic/sphinx3.dynamic.txt"
# objdump -d "specrand-998-06.dynamic"    > "../source/dynamic/specrand-998-06.dynamic.txt"
# objdump -d "specrand-999-06.dynamic"    > "../source/dynamic/specrand-999-06.dynamic.txt"

cd ../../
echo -e "\e[1;32m[DONE]\e[0m Disassembled Dynamic x86 source codes"

# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

# Extracting functions from dynamic binaries
cd bin/dynamic/

# # SPEC2017 benchmarks

> gdb.txt
gdb "mcf.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/mcf.func.dump

# > gdb.txt
# gdb "omnetpp.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
# cp gdb.txt ../../functions/dump/omnetpp.func.dump

> gdb.txt
gdb "xalancbmk.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/xalancbmk.func.dump

# > gdb.txt
# gdb "imagick.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
# cp gdb.txt ../../functions/dump/imagick.func.dump

# > gdb.txt
# gdb "x264.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
# cp gdb.txt ../../functions/dump/x264.func.dump

> gdb.txt
gdb "deepsjeng.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/deepsjeng.func.dump

> gdb.txt
gdb "leela.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/leela.func.dump

> gdb.txt
gdb "xz.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/xz.func.dump

> gdb.txt
gdb "namd.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/namd.func.dump

# > gdb.txt
# gdb "parest.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
# cp gdb.txt ../../functions/dump/parest.func.dump

# > gdb.txt
# gdb "povray.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
# cp gdb.txt ../../functions/dump/povray.func.dump

> gdb.txt
gdb "lbm.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/lbm.func.dump

# > gdb.txt
# gdb "blender.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
# cp gdb.txt ../../functions/dump/blender.func.dump

> gdb.txt
gdb "nab.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/nab.func.dump

> gdb.txt
gdb "specrand-fr.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/specrand-fr.func.dump

> gdb.txt
gdb "specrand-ir.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/specrand-ir.func.dump

# # SPEC2006 benchmarks
> gdb.txt
gdb "libquantum.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/libquantum.func.dump

> gdb.txt
gdb "bzip2.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/bzip2.func.dump

> gdb.txt
gdb "gobmk.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/gobmk.func.dump

# > gdb.txt
# gdb "hmmer.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
# cp gdb.txt ../../functions/dump/hmmer.func.dump

> gdb.txt
gdb "sjeng.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/sjeng.func.dump

# > gdb.txt
# gdb "h264ref.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
# cp gdb.txt ../../functions/dump/h264ref.func.dump

> gdb.txt
gdb "milc.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/milc.func.dump

> gdb.txt
gdb "sphinx3.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/sphinx3.func.dump

# > gdb.txt
# gdb "omnetpp-06.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
# cp gdb.txt ../../functions/dump/omnetpp-06.func.dump

# > gdb.txt
# gdb "povray-06.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
# cp gdb.txt ../../functions/dump/povray-06.func.dump

> gdb.txt
gdb "mcf-06.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/mcf-06.func.dump

> gdb.txt
gdb "namd-06.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/namd-06.func.dump

# > gdb.txt
# gdb "specrand-998-06.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
# cp gdb.txt ../../functions/dump/specrand-998-06.func.dump

# > gdb.txt
# gdb "specrand-999-06.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
# cp gdb.txt ../../functions/dump/specrand-999-06.func.dump

rm gdb.txt
cd ../../
echo -e "\e[1;32m[DONE]\e[0m Created function-name dumps from GDB (benchmark.func.dump)"
