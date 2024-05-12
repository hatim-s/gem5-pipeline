benchmark=$1

cd $benchmark/

mkdir -p stats/

grep "simInsts" $benchmark.arm.stat > stats/$benchmark.arm.inst
grep "simInsts" $benchmark.x86.stat > stats/$benchmark.x86.inst

grep "simTicks" $benchmark.arm.stat > stats/$benchmark.arm.tick
grep "simTicks" $benchmark.x86.stat > stats/$benchmark.x86.tick

cd ../../python/

python3 generate-raw-stats.py   $benchmark
python3 generate-func-stats.py  $benchmark

cd ../data/$benchmark/stats
rm $benchmark.*.inst
rm $benchmark.*.tick
