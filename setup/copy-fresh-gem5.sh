#!/bin/bash

mkdir -p ../gem5-arm/

index=1
while [ $index -lt 10 ]
do
    cp -R ../gem5 ../gem5-arm/arm-${index}
    echo -e "\e[1;32m[DONE]\e[0m Copied arm-${index}"

    index=`expr $index + 1`
done
echo -e "\e[1;32m[DONE] Copied Fresh Gem5 to Arm\e[0m"

mkdir -p ../gem5-x86/

index=1
while [ $index -lt 10 ]
do
    cp -R ../gem5 ../gem5-x86/x86-${index}
    echo -e "\e[1;32m[DONE]\e[0m Copied x86-${index}"

    index=`expr $index + 1`
done
echo -e "\e[1;32m[DONE] Copied Fresh Gem5 to X86\e[0m"