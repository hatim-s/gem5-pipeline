# Script to copy train-test-ref data
cd ../

mkdir -p bin/data/

cd spec2017/benchspec/CPU

# cd 538.imagick_r/
# mkdir -p ../../../../bin/data/imagick
# cp -R data/ ../../../../bin/data/imagick
# cd ../
# echo "\e[1;32m[DONE]\e[0m Copied imagick"

cd 519.lbm_r/
mkdir -p ../../../../bin/data/lbm
cp -R data/ ../../../../bin/data/lbm
cd ../
echo "\e[1;32m[DONE]\e[0m Copied lbm"

cd 505.mcf_r/
mkdir -p ../../../../bin/data/mcf
cp -R data/ ../../../../bin/data/mcf
cd ../
echo "\e[1;32m[DONE]\e[0m Copied mcf"

cd 544.nab_r/
mkdir -p ../../../../bin/data/nab
cp -R data/ ../../../../bin/data/nab
cd ../
echo "\e[1;32m[DONE]\e[0m Copied nab"

# cd 525.x264_r/
# mkdir -p ../../../../bin/data/x264
# cp -R data/ ../../../../bin/data/x264
# cd ../
# echo "\e[1;32m[DONE]\e[0m Copied x264"

cd 557.xz_r/
mkdir -p ../../../../bin/data/xz
cp -R data/ ../../../../bin/data/xz
cd ../
echo "\e[1;32m[DONE]\e[0m Copied xz"

cd 526.blender_r/
mkdir -p ../../../../bin/data/blender
cp -R data/ ../../../../bin/data/blender
cd ../
echo "\e[1;32m[DONE]\e[0m Copied blender"

cd 531.deepsjeng_r/
mkdir -p ../../../../bin/data/deepsjeng
cp -R data/ ../../../../bin/data/deepsjeng
cd ../
echo "\e[1;32m[DONE]\e[0m Copied deepsjeng"

cd 541.leela_r/
mkdir -p ../../../../bin/data/leela
cp -R data/ ../../../../bin/data/leela
cd ../
echo "\e[1;32m[DONE]\e[0m Copied leela"

cd 508.namd_r/
mkdir -p ../../../../bin/data/namd
cp -R data/ ../../../../bin/data/namd
cd ../
echo "\e[1;32m[DONE]\e[0m Copied namd"

cd 520.omnetpp_r/
mkdir -p ../../../../bin/data/omnetpp
cp -R data/ ../../../../bin/data/omnetpp
cd ../
echo "\e[1;32m[DONE]\e[0m Copied omnetpp"

# cd 510.parest_r/
# mkdir -p ../../../../bin/data/parest
# cp -R data/ ../../../../bin/data/parest
# cd ../
# echo "\e[1;32m[DONE]\e[0m Copied parest"

# cd 511.povray_r/
# mkdir -p ../../../../bin/data/povray
# cp -R data/ ../../../../bin/data/povray
# cd ../
# echo "\e[1;32m[DONE]\e[0m Copied povray"

cd 523.xalancbmk_r/
mkdir -p ../../../../bin/data/xalancbmk
cp -R data/ ../../../../bin/data/xalancbmk
cd ../
echo "\e[1;32m[DONE]\e[0m Copied xalancbmk"

cd ../../../

cd spec2006/benchspec/CPU2006/

cd 401.bzip2/
mkdir -p ../../../../bin/data/bzip2
cp -R data/ ../../../../bin/data/bzip2
cd ../
echo "\e[1;32m[DONE]\e[0m Copied bzip2"

cd 445.gobmk/
mkdir -p ../../../../bin/data/gobmk
cp -R data/ ../../../../bin/data/gobmk
cd ../
echo "\e[1;32m[DONE]\e[0m Copied gobmk"

# cd 456.hmmer/
# mkdir -p ../../../../bin/data/hmmer
# cp -R data/ ../../../../bin/data/hmmer
# cd ../
# echo "\e[1;32m[DONE]\e[0m Copied hmmer"

cd 458.sjeng/
mkdir -p ../../../../bin/data/sjeng
cp -R data/ ../../../../bin/data/sjeng
cd ../
echo "\e[1;32m[DONE]\e[0m Copied sjeng"

# cd 464.h264ref/
# mkdir -p ../../../../bin/data/h264ref
# cp -R data/ ../../../../bin/data/h264ref
# cd ../
# echo "\e[1;32m[DONE]\e[0m Copied h264ref"

cd 433.milc/
mkdir -p ../../../../bin/data/milc
cp -R data/ ../../../../bin/data/milc
cd ../
echo "\e[1;32m[DONE]\e[0m Copied milc"

cd 482.sphinx3/
mkdir -p ../../../../bin/data/sphinx3
cp -R data/ ../../../../bin/data/sphinx3
cd ../
echo "\e[1;32m[DONE]\e[0m Copied sphinx3"