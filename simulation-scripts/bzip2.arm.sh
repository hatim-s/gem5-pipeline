benchmark="bzip2"
ISA="arm"         # x86 or arm used in paths and cli
ISA_build="ARM"   # X86 or ARM used in the ./build...

bench_exec_path="../../bin/data/$benchmark/test/input"
bench_options="$bench_exec_path/dryer.jpg 2"
config_file="configs/deprecated/example/se.py"
executable="../../bin/${ISA}/${benchmark}.${ISA}"
bench_input=""

# cd pyscripts/
# python3 extract-address.py $benchmark
# cd ../

# echo "" > outputs/inst-count.txt
# echo "" > m5out/stats.txt

# # running first pass
# ./build/${ISA_build}/gem5.opt $config_file --maxinsts 5000000000 -c $executable --input=$bench_input --options="$bench_options" 
# echo -e "\e[1;32m[Simulation]\e[0m First Pass Complete"

# cd pyscripts/
# python3 rm-dup.py $benchmark
# cd ../

# mkdir -p ../../data/$benchmark
# cp bench-stats/$benchmark.inst ../../data/$benchmark/$benchmark.$ISA.inst

echo "" > m5out/stats.txt

cp ../../data/$benchmark/$benchmark.$ISA.trunc.inst inputs/equipoints.txt

# running second pass
./build/${ISA_build}/gem5.opt $config_file --cpu-type=DerivO3CPU --caches --l2cache --equipoints=1 --equifile "inputs/equipoints.txt" -c $executable --input=$bench_input --options="$bench_options"

echo -e "\e[1;32m[Simulation]\e[0m Second Pass Complete"

cp "m5out/stats.txt" "bench-stats/${benchmark}.${ISA}.stat"

cd pyscripts/
python3 prep-stats.py $benchmark
cd ../

cp bench-stats/$benchmark.$ISA.csv  ../../data/$benchmark/$benchmark.$ISA.csv
cp bench-stats/$benchmark.$ISA.stat ../../data/$benchmark/$benchmark.$ISA.stat