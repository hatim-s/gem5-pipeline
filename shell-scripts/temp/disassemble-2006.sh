#/bin/bash
cd ../

# Disassembling static binaries - X86
cd bin/x86

# SPEC2006 benchmarks
# objdump -d "libquantum.x86"     > "../source/x86/libquantum.x86.txt"
objdump -d "bzip2.x86"     > "../source/x86/bzip2.x86.txt"
objdump -d "gobmk.x86"     > "../source/x86/gobmk.x86.txt"
objdump -d "hmmer.x86"     > "../source/x86/hmmer.x86.txt"
objdump -d "sjeng.x86"     > "../source/x86/sjeng.x86.txt"
objdump -d "h264ref.x86"     > "../source/x86/h264ref.x86.txt"
objdump -d "milc.x86"     > "../source/x86/milc.x86.txt"
objdump -d "sphinx3.x86"     > "../source/x86/sphinx3.x86.txt"
cd ../../
echo "\e[1;32m[DONE]\e[0m Disassembled x86 source codes"


# Disassembling static binaries - ARM
cd bin/arm

# SPEC2006 benchmarks
# aarch64-linux-gnu-objdump -d "libquantum.arm"     > "../source/arm/libquantum.arm.txt"
aarch64-linux-gnu-objdump -d "bzip2.arm"     > "../source/arm/bzip2.arm.txt"
aarch64-linux-gnu-objdump -d "gobmk.arm"     > "../source/arm/gobmk.arm.txt"
aarch64-linux-gnu-objdump -d "hmmer.arm"     > "../source/arm/hmmer.arm.txt"
aarch64-linux-gnu-objdump -d "sjeng.arm"     > "../source/arm/sjeng.arm.txt"
aarch64-linux-gnu-objdump -d "h264ref.arm"     > "../source/arm/h264ref.arm.txt"
aarch64-linux-gnu-objdump -d "milc.arm"     > "../source/arm/milc.arm.txt"
aarch64-linux-gnu-objdump -d "sphinx3.arm"     > "../source/arm/sphinx3.arm.txt"
cd ../../
echo "\e[1;32m[DONE]\e[0m Disassembled arm source codes"


# Disassembling dynamic X86 binaries
cd bin/dynamic

# SPEC2006 benchmarks
# objdump -d "libquantum.dynamic"     > "../source/dynamic/libquantum.dynamic.txt"
objdump -d "bzip2.dynamic"     > "../source/dynamic/bzip2.dynamic.txt"
objdump -d "gobmk.dynamic"     > "../source/dynamic/gobmk.dynamic.txt"
objdump -d "hmmer.dynamic"     > "../source/dynamic/hmmer.dynamic.txt"
objdump -d "sjeng.dynamic"     > "../source/dynamic/sjeng.dynamic.txt"
objdump -d "h264ref.dynamic"     > "../source/dynamic/h264ref.dynamic.txt"
objdump -d "milc.dynamic"     > "../source/dynamic/milc.dynamic.txt"
objdump -d "sphinx3.dynamic"     > "../source/dynamic/sphinx3.dynamic.txt"
cd ../../
echo "\e[1;32m[DONE]\e[0m Disassembled Dynamic x86 source codes"


# Extracting functions from dynamic binaries
cd bin/dynamic/

# SPEC2006 benchmarks
> gdb.txt
gdb "libquantum.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/libquantum.func.dump

> gdb.txt
gdb "bzip2.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/bzip2.func.dump

> gdb.txt
gdb "gobmk.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/gobmk.func.dump

> gdb.txt
gdb "hmmer.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/hmmer.func.dump

> gdb.txt
gdb "sjeng.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/sjeng.func.dump

> gdb.txt
gdb "h264ref.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/h264ref.func.dump

> gdb.txt
gdb "milc.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/milc.func.dump

> gdb.txt
gdb "sphinx3.dynamic" -q  -batch-silent -ex 'set pagination off' -ex 'set logging enable on' -ex 'info functions' -ex 'q'
cp gdb.txt ../../functions/dump/sphinx3.func.dump


rm gdb.txt
cd ../../
echo "\e[1;32m[DONE]\e[0m Created function-name dumps from GDB (benchmark.func.dump)"


