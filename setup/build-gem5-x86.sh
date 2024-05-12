cd ../

index=1
while [ $index -lt 10 ]
do
    cd gem5-x86/x86-${index}
    scons build/X86/gem5.opt -j {#cpus}

    cd ../../

    index=`expr $index + 1`
done
