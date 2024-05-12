cd ../

mkdir -p data/

index=1
while [ $index -lt 10 ]
do
    cd gem5-arm/arm-${index}/
    mkdir inputs/
    touch inputs/pc-address.txt
    touch inputs/equipoints.txt

    mkdir outputs/
    touch outputs/inst-count.txt
    touch outputs/benchmark.first.out

    mkdir bench-stats/
    mkdir pyscripts/

    cd ../../../

    echo -e "\e[1;32m[DONE]\e[0m Created file structure for arm-${index}"
    
    index=`expr $index + 1`
done
echo -e "\e[1;32m[DONE] Created File Structures for ARM\e[0m"

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

index=1
while [ $index -lt 10 ]
do
    cd gem5-x86/x86-${index}/
    mkdir inputs/
    touch inputs/pc-address.txt
    touch inputs/equipoints.txt

    mkdir outputs/
    touch outputs/inst-count.txt
    touch outputs/benchmark.first.out

    mkdir bench-stats/
    mkdir pyscripts/

    cd ../../../

    echo -e "\e[1;32m[DONE]\e[0m Created file structure for x86-${index}"
    
    index=`expr $index + 1`
done
echo -e "\e[1;32m[DONE] Created File Structures for X86\e[0m"
