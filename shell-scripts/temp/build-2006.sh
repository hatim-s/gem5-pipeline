cd ../

cd spec2006/
source shrc
cd config

# runspec --config=myconfig-arm --action=build --verbose=1 libquantum
# runspec --config=myconfig-x86 --action=build --verbose=1 libquantum
# runspec --config=myconfig-x86-dynamic --action=build --verbose=1 libquantum
# echo "\e[1;32m[DONE]\e[0m libquantum built successfully "

runspec --config=myconfig-arm --action=build --verbose=1 bzip2
runspec --config=myconfig-x86 --action=build --verbose=1 bzip2
runspec --config=myconfig-x86-dynamic --action=build --verbose=1 bzip2
echo "\e[1;32m[DONE]\e[0m bzip2 built successfully "

runspec --config=myconfig-arm --action=build --verbose=1 gobmk
runspec --config=myconfig-x86 --action=build --verbose=1 gobmk
runspec --config=myconfig-x86-dynamic --action=build --verbose=1 gobmk
echo "\e[1;32m[DONE]\e[0m gobmk built successfully "

runspec --config=myconfig-arm --action=build --verbose=1 hmmer
runspec --config=myconfig-x86 --action=build --verbose=1 hmmer
runspec --config=myconfig-x86-dynamic --action=build --verbose=1 hmmer
echo "\e[1;32m[DONE]\e[0m hmmer built successfully "

runspec --config=myconfig-arm --action=build --verbose=1 sjeng
runspec --config=myconfig-x86 --action=build --verbose=1 sjeng
runspec --config=myconfig-x86-dynamic --action=build --verbose=1 sjeng
echo "\e[1;32m[DONE]\e[0m sjeng built successfully "

runspec --config=myconfig-arm --action=build --verbose=1 h264ref
runspec --config=myconfig-x86 --action=build --verbose=1 h264ref
runspec --config=myconfig-x86-dynamic --action=build --verbose=1 h264ref
echo "\e[1;32m[DONE]\e[0m h264ref built successfully "

runspec --config=myconfig-arm --action=build --verbose=1 milc
runspec --config=myconfig-x86 --action=build --verbose=1 milc
runspec --config=myconfig-x86-dynamic --action=build --verbose=1 milc
echo "\e[1;32m[DONE]\e[0m milc built successfully "

runspec --config=myconfig-arm --action=build --verbose=1 sphinx3
runspec --config=myconfig-x86 --action=build --verbose=1 sphinx3
runspec --config=myconfig-x86-dynamic --action=build --verbose=1 sphinx3
echo "\e[1;32m[DONE]\e[0m sphinx3 built successfully "

echo "\e[1;32m[DONE] Successfully built SPEC2006 Benchmarks\e[0m"
