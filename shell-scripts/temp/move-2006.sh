#!/bin/bash
cd ../

cd spec2006/benchspec/CPU2006/

# SPEC2006 benchmarks
# cd 462.libquantum/exe
# cp libquantum_base.arm ../../../../../bin/arm/libquantum.arm
# cp libquantum_base.x86 ../../../../../bin/x86/libquantum.x86
# cp libquantum_base.x86-dynamic ../../../../../bin/dynamic/libquantum.dynamic
# cd ../../
# echo "\e[1;32m[DONE]\e[0m Copied libquantum"

cd 401.bzip2/exe
cp bzip2_base.arm ../../../../../bin/arm/bzip2.arm
cp bzip2_base.x86 ../../../../../bin/x86/bzip2.x86
cp bzip2_base.x86-dynamic ../../../../../bin/dynamic/bzip2.dynamic
cd ../../
echo "\e[1;32m[DONE]\e[0m Copied bzip2"

cd 445.gobmk/exe
cp gobmk_base.arm ../../../../../bin/arm/gobmk.arm
cp gobmk_base.x86 ../../../../../bin/x86/gobmk.x86
cp gobmk_base.x86-dynamic ../../../../../bin/dynamic/gobmk.dynamic
cd ../../
echo "\e[1;32m[DONE]\e[0m Copied gobmk"

cd 456.hmmer/exe
cp hmmer_base.arm ../../../../../bin/arm/hmmer.arm
cp hmmer_base.x86 ../../../../../bin/x86/hmmer.x86
cp hmmer_base.x86-dynamic ../../../../../bin/dynamic/hmmer.dynamic
cd ../../
echo "\e[1;32m[DONE]\e[0m Copied hmmer"

cd 458.sjeng/exe
cp sjeng_base.arm ../../../../../bin/arm/sjeng.arm
cp sjeng_base.x86 ../../../../../bin/x86/sjeng.x86
cp sjeng_base.x86-dynamic ../../../../../bin/dynamic/sjeng.dynamic
cd ../../
echo "\e[1;32m[DONE]\e[0m Copied sjeng"

cd 464.h264ref/exe
cp h264ref_base.arm ../../../../../bin/arm/h264ref.arm
cp h264ref_base.x86 ../../../../../bin/x86/h264ref.x86
cp h264ref_base.x86-dynamic ../../../../../bin/dynamic/h264ref.dynamic
cd ../../
echo "\e[1;32m[DONE]\e[0m Copied h264ref"

cd 433.milc/exe
cp milc_base.arm ../../../../../bin/arm/milc.arm
cp milc_base.x86 ../../../../../bin/x86/milc.x86
cp milc_base.x86-dynamic ../../../../../bin/dynamic/milc.dynamic
cd ../../
echo "\e[1;32m[DONE]\e[0m Copied milc"

cd 482.sphinx3/exe
cp sphinx_livepretend_base.arm ../../../../../bin/arm/sphinx3.arm
cp sphinx_livepretend_base.x86 ../../../../../bin/x86/sphinx3.x86
cp sphinx_livepretend_base.x86-dynamic ../../../../../bin/dynamic/sphinx3.dynamic
cd ../../
echo "\e[1;32m[DONE]\e[0m Copied sphinx3"


