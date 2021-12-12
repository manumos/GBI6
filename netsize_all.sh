#!/bin/bash
#abro el directorio de interes
cd $1
#POLINIZADORES
#de todos loS archivos .txt cuenta las lineas y las guardo en archivos temporales
wc -l *.txt > tempA*.txt
#imprimo todos los archivos temporales en un solo archivo final
cat tempA*.txt

#PLANTAS
#selecciono la primera fila de los archivos .txt y la almaceno en un documento temporal
head -n 1 *.txt > tempB*.txt
cat tempB*.txt | tr -d " " |wc -m > tempB*.txt
#remuevo los archivos temporales
cat temp*.txt
#imprimo los resultados
rm temp*.txt

