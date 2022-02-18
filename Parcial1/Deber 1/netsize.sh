#!/bin/bash
#Este script busca determinar el número de filas (polinizadores) y columnas (plantas) del los archivos .txt contenido sen el directorio CSB/unix/data/Saavedra2013.

##1. Determinar el número de filas = POLINIZADORES

#Creo un nuevo archivo para almacernar los resultados y etiqueto el primer resultado
echo "POLINIZADORES" > netsize.txt
#imprimo el archivo argumento y cuenta las filas
#almaceno la respuesta  en el archivo creado
cat $1 |wc -l >> netsize.txt

###########################################################
##2. Determinar el número de columnas = PLANTAS

#creo la etiqueta para los sigueintes datos dentro del archivo
echo "PLANTAS" >> netsize.txt

#selecciono la primera fila de l archivo argumentos $1 y la guardo en el archivo temporal correspondiente
head -n 1 $1 > $1.txt


#imprimo el archivo temporal que contiene la única fila del archivo argumento
#y elimino los espacios en blanco " "
#por último cuento los caracteres, que corresponden al número de filas
cat $1.txt | tr -d " " |wc -m >> netsize.txt

#remuevo los archivos temporales
rm $1.txt

#imprimo los resultado almacenados
cat netsize.txt
