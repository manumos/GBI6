#!/bin/bash
echo "POLINIZADORES" > netsize_all.txt
for n*.txt in Saavedra2013; do cat |wc -l >> netsize_all.txt; done
echo "PLANTAS" >> netsize_all.txt
for n*.txt in Saavedra2013;do head -n 1 $1 > $1.txt |cat $1.txt | tr -d " " |wc -m >> netsize_all.txt | rm $1.txt;done
cat netsize_all.txt
