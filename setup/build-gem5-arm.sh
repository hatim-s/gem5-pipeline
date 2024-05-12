cd ../

index=1
while [ $index -lt 10 ]
do
    cd gem5-arm/arm-${index}
    scons build/ARM/gem5.opt -j {#cpus}

    cd ../../

    index=`expr $index + 1`
done