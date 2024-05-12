benchmark=$1
temp_file_path="../data/$benchmark/temp"
bench_file_path="../data/$benchmark"

mkdir -p temp/
cd ../../python/

cp ../data/$benchmark/$benchmark.arm.inst $temp_file_path/
cp ../data/$benchmark/$benchmark.x86.inst $temp_file_path/
echo -e "\e[1;32m[DONE]\e[0m Raw Inst Files Copied\n"

python3 merge-call-seq.py $benchmark
echo -e "\e[1;32m[DONE]\e[0m Call Sequence Merged\n"

python3 remove-linked-return-functions.py $benchmark
cp $temp_file_path/$benchmark.arm.out.merged $temp_file_path/$benchmark.arm.merged
cp $temp_file_path/$benchmark.x86.out.merged $temp_file_path/$benchmark.x86.merged

python3 remove-duplicate-returns.py $benchmark arm 
python3 remove-duplicate-returns.py $benchmark x86 
cp $temp_file_path/$benchmark.arm.out.merged $temp_file_path/$benchmark.arm.merged
cp $temp_file_path/$benchmark.x86.out.merged $temp_file_path/$benchmark.x86.merged

python3 remove-unclosed-func.py $benchmark arm
python3 remove-unclosed-func.py $benchmark x86
cp $temp_file_path/$benchmark.arm.out.merged $temp_file_path/$benchmark.arm.merged
cp $temp_file_path/$benchmark.x86.out.merged $temp_file_path/$benchmark.x86.merged

rm $temp_file_path/$benchmark.arm.out.merged
rm $temp_file_path/$benchmark.x86.out.merged

echo -e "\e[1;32m[DONE]\e[0m Linked-return Functions & Duplicate Returns Removed\n"

cd pycleanup/
python3 prep-dic-merged.py arm $benchmark
python3 prep-dic-merged.py x86 $benchmark
cd ../

echo -e "\e[1;32m[DONE]\e[0m Log files generated\n"

# -------------------------------------------------------- data cleaning --------------------------------------------------------
# -------------------------------------------------------- data cleaning --------------------------------------------------------
# -------------------------------------------------------- data cleaning --------------------------------------------------------
# -------------------------------------------------------- data cleaning --------------------------------------------------------
# -------------------------------------------------------- data cleaning --------------------------------------------------------
# -------------------------------------------------------- data cleaning --------------------------------------------------------
# -------------------------------------------------------- data cleaning --------------------------------------------------------
# -------------------------------------------------------- data cleaning --------------------------------------------------------
# -------------------------------------------------------- data cleaning --------------------------------------------------------
# -------------------------------------------------------- data cleaning --------------------------------------------------------

python3 extract-insts.py $benchmark
python3 rm-diff-functions.py $benchmark

cp $temp_file_path/$benchmark.arm.common.inst $temp_file_path/$benchmark.arm.inst
cp $temp_file_path/$benchmark.x86.common.inst $temp_file_path/$benchmark.x86.inst

rm $temp_file_path/$benchmark.arm.common.inst
rm $temp_file_path/$benchmark.x86.common.inst

echo -e "\e[1;32m[DONE]\e[0m Common Function-inst File Created"

head --lines 2189 $temp_file_path/$benchmark.arm.inst > $temp_file_path/$benchmark.arm.out.inst
cp $temp_file_path/$benchmark.arm.out.inst $temp_file_path/$benchmark.arm.inst
rm $temp_file_path/$benchmark.arm.out.inst

head --lines 168352 $temp_file_path/$benchmark.x86.inst > $temp_file_path/$benchmark.x86.out.inst
cp $temp_file_path/$benchmark.x86.out.inst $temp_file_path/$benchmark.x86.inst
rm $temp_file_path/$benchmark.x86.out.inst

python3 merge-call-seq.py $benchmark

echo -e "\e[1;32m[DONE]\e[0m Common log files Created"

python3 remove-warmup.py $benchmark 0
python3 prep-dic-trunc.py $benchmark

cp $bench_file_path/$benchmark.arm.out.trunc.inst $bench_file_path/$benchmark.arm.trunc.inst
cp $bench_file_path/$benchmark.x86.out.trunc.inst $bench_file_path/$benchmark.x86.trunc.inst

rm $bench_file_path/$benchmark.arm.out.trunc.inst
rm $bench_file_path/$benchmark.x86.out.trunc.inst

echo -e "\e[1;32m[DONE]\e[0m Warmup Removed"

python3 find-inst-diff.py $benchmark arm
grep -v '^$' $bench_file_path/$benchmark.arm.trunc.out.inst > $bench_file_path/$benchmark.arm.trunc.inst
grep -v '^$' $bench_file_path/$benchmark.x86.trunc.out.inst > $bench_file_path/$benchmark.x86.trunc.inst

python3 find-inst-diff.py $benchmark x86
grep -v '^$' $bench_file_path/$benchmark.arm.trunc.out.inst > $bench_file_path/$benchmark.arm.trunc.inst
grep -v '^$' $bench_file_path/$benchmark.x86.trunc.out.inst > $bench_file_path/$benchmark.x86.trunc.inst

rm $bench_file_path/$benchmark.arm.trunc.out.inst
rm $bench_file_path/$benchmark.x86.trunc.out.inst

echo -e "\e[1;32m[DONE]\e[0m < 3 Inst Distanced Points Removed"