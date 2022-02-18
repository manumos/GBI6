#!/bin/bash
cd $1
touch null
cat null>$2

for i in *.txt
do
wc -l $i >$pol
cut -d " " -f 1 $i |wc -c >$pla
echo " Archivo="$1" Polinizadores= "$pol" Plantas="$pla" ">$2

done
cat $2



#cat null>$2
#for i in *.txt
#do
#Polinizadores= 'wc -l $i'
#Plantas= 'cut -d " " -f 1 $i > f.txt |wc -c f2.txt'
#echo "Archivo = "$i", "$Polini
