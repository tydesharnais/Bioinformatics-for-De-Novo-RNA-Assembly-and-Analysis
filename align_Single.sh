#!/bin/sh
DIR=`pwd`
echo "Working for $1"

to_fa=$1".fa"
cd ~/Links/fafiles/
cp -v $to_fa $DIR
out_F=$1".out"
cd $DIR
blastp -db Trinity.fasta.transdecoder.pep -query $to_fa -outfmt 6 -out $out_F


data=`head -n 1 $out_F | awk '{ print $2 }'`
file_Name=`head -n 1 $out_F | awk '{ print $1 }'`
file_Exten=$file_Name".txt"

echo "$file_Exten"
echo $data >> $file_Exten

vars=`basename "$PWD"`
folder=`echo $vars | sed -n 's/trinity_//p'`
file_Op=$folder"_"$file_Name".txt"
echo "$file_Op"
perl /home/xiaoyu/bin/scripts/fasta_pick.pl -i Trinity.fasta.transdecoder.pep -s $file_Exten -o $file_Op
peptide=`awk 'NR>1' $file_Op`
mafft_file=$file_Name"_mafftReady.txt"
touch $mafft_file
echo "$mafft_file"
echo ">"$folder >> $mafft_file
echo $peptide >> $mafft_file

fasta=$mafft_file".fasta"
rm $file_Exten
rm $file_Op
rm $out_F


cp $mafft_file $fasta

rm $mafft_file
to_fasta=$1".fasta"

cd ~/Links/Alignments
cp -v $to_fasta $DIR
cd $DIR
mafftFILENAME=$1"_Complete.fasta"
mafft --add $fasta $to_fasta > $mafftFILENAME
cp $mafftFILENAME MafftComplete
rm $fasta

cd MafftComplete
cp $mafftFILENAME $to_fasta
#CLEANUP
rm $mafftFILENAME

printf "------------------------------------------------------------------"
printf "--------------------Completed Alignment --------------------------"
printf "\n\nSTORED IN THE MAFFTCOMPLETE SUBDIRECTIORY\n\n"
