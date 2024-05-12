cd ../

index=1
while [ $index -lt 10 ]
do
    cp setup/arm/arm-index/atomic-$index.cc     gem5-arm/arm-$index/src/cpu/simple/atomic.cc
    cp setup/BaseO3CPU.py                       gem5-arm/arm-$index/src/cpu/o3/BaseO3CPU.py
    cp setup/FuncUnitConfig.py                  gem5-arm/arm-$index/src/cpu/o3/FuncUnitConfig.py
    cp setup/Options.py                         gem5-arm/arm-$index/configs/common/Options.py
    cp setup/Simulations.py                     gem5-arm/arm-$index/configs/common/Simulations.py
    cp setup/text.cc                            gem5-arm/arm-$index/src/base/stats/text.cc

    cp python/extract-address-arm.py            gem5-arm/arm-$index/pyscripts/extract-address.py
    cp python/rm-dup.py                         gem5-arm/arm-$index/pyscripts/rm-dup.py
    cp python/prep-stats-arm.py                 gem5-arm/arm-$index/pyscripts/prep-stats.py
    
    echo -e "\e[1;32m[DONE]\e[0m Injected files into arm-${index}"
    
    index=`expr $index + 1`
done
echo -e "\e[1;32m[DONE] Injected Files ARM Gem5\e[0m"

index=1
while [ $index -lt 10 ]
do
    cp setup/x86/x86-index/atomic-$index.cc     gem5-x86/x86-$index/src/cpu/simple/atomic.cc
    cp setup/BaseO3CPU.py                       gem5-x86/x86-$index/src/cpu/o3/BaseO3CPU.py
    cp setup/Options.py                         gem5-x86/x86-$index/configs/common/Options.py
    cp setup/Simulations.py                     gem5-x86/x86-$index/configs/common/Simulations.py
    cp setup/text.cc                            gem5-x86/x86-$index/src/base/stats/text.cc
    
    cp python/extract-address-x86.py            gem5-x86/x86-$index/pyscripts/extract-address.py
    cp python/rm-dup.py                         gem5-x86/x86-$index/pyscripts/rm-dup.py
    cp python/prep-stats-x86.py                 gem5-x86/x86-$index/pyscripts/prep-stats.py

    echo -e "\e[1;32m[DONE]\e[0m Injected files into x86-${index}"
    
    index=`expr $index + 1`
done
echo -e "\e[1;32m[DONE] Injected Files X86 Gem5\e[0m"