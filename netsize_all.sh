#!/bin/bash
#imprimo el primer titulo y creo un archivo nuevo
#echo "POLINIZADORES" > netsize_all.txt
#abro el directorio de interes
#de todos los archivos .txt cuento las lineas y las guardo en el anterior archivo creado
cd $1
wc -l *.txt >> temp*.txt
cat temp*.txt >> netsize_all.txt
rm temp*.txt
#imprimo el segundo titulo en el archivo creado
#echo "PLANTAS" >> netsize_all.txt
#selecciono la primera fila de los archivos .txt y la almaceno en un documento temporal
head -n 1 *.txt > $1.txt
#imprimo el documento temporal y  borro los espacios en blanco
#luego cuento los caracteres y lo guardo en el archivo de resultado
cat $1.txt | tr -d " " |wc -m >>netsize_all.txt
#remuevo los archivos temporales
rm $*.txt
#imprimo los resultados
cat netsize_all.txt

