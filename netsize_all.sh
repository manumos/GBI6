#!/bin/bash
#abro el directorio de interes
cd $1
#POLINIZADORES
#de todos loS archivos .txt cuenta las lineas y las guardo en archivos temporales
echo "POLINIZADORES"
wc -l *.txt > j.txt
#imprimo todos los archivos temporales en un solo archivo final
cat j.txt
rm j.txt

#PLANTAS
echo "PLANTAS"
head -n 1 *.txt > *T.txt 
cat *T.txt | tr -d " " |wc -m > k.txt
cat k.txt
#imprimo los resultados
rm *T.txt
rm k.txt



