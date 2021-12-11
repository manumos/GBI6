#!/bin/bash
#Este script busca determinar el número de filas (polinizadores) y columnas (plantas) del los archivos .txt contenido sen el directorio CSB/unix/data/Saavedra2013.
#1. Determinar el número de filas = POLINIZADORES
wc -l $1 > netsize.txt
cat netsize.txt
#2. Determinar el número de columnas = PLANTAS
#$1 | cut -d " " > PLA.txt

