#!/bin/sh
DIR=`pwd`
clear
printf "\n\nTy's Single Alignment Fast Track Tool\n---------------------------------------------------\n\n"
echo "CURRENT DIRECTORY: $DIR"
cd ~/Links/Alignments
shopt -s nullglob
echo ""
echo ""
echo "Starting up FAFILE<------>FASTA LINKER"
echo "--------------------------------------------"
echo ""
sleep 2

for i in *.fasta; do
    filename=$i
    new_file=${filename%.*}
    printf "QUERY: $new_file\n----------------------\n"
    sleep 0.5
    cd ~/Links/fafiles
    file_FA=$new_file".fa"
    lines=$(find  -type f -name $file_FA | wc -l)
   
    if [ $lines -eq 1 ]; then 
       echo "FOUND: $new_file"".fa"
       
       printf "\nAligning...\n"
       echo ""
       sleep 1
       cd $DIR
       sh ./align_Single.sh $new_file
    else
    printf "NOT FOUND\n\n"
    sleep 1
    fi
    cd ~/Links/Alignments
done

cd ~/Links/fafiles
echo ""
echo ""
echo "From FAFILES"
echo "-----------------------"
echo ""

for i in *.fa; do
    filename=$i
    new_file=${filename%.*}
    echo "$new_file"
done
