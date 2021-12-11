#!/bin/bash
#Este script busca determinar el número de filas (polinizadores) y columnas (plantas) del los archivos .txt contenido sen el directorio CSB/unix/data/Saavedra2013.
#1. Determinar el número de filas = POLINIZADORES
#wc -l $1 > netsize.txt
#cat netsize.txt

##2. Determinar el número de columnas = PLANTAS
#selecciono la primera fila de l archivo argumentos $1 y la guardo en el archivo temporal correspondiente
head -n 1 $1 > $1.txt
#imprimo el archivo temporal que contiene la única fila del archivo argumento
#y elimino los espacios en blanco " "
#por último cuento los caracteres, que corresponden al número de filas
cat $1.txt | tr -d " " |wc -m > netsize.txt
#remuevo los archivos temporales
rm $1.txt
#imprimo los resultado almacenados
cat netsize.txt




