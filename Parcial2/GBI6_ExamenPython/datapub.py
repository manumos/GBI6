# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 13:52:48 2022

@author: Manuela
"""

#PRIMERA FUNCION
def download_pubmed(keyword):
    """Descargar la data de pubmed
            -Parametros
                keyword= string con el termino de busqueda
            -Output
                Lista que contiene los IDs de los resultados encontrados
    """
    
    #importar paquetes
    from Bio import Entrez as en

    
    #notificar correo
    en.email = "manuela.moscoso@est.ikiam.edu.ec.com"
    
    #realizar la busqueda
    handle= en.esearch(db="pubmed", term=keyword, usehistory="y",retmax=1000,retmode='xml')
    record = en.read(handle)
    
    #obtener ids
    idlist = record["IdList"]
    i_d=",".join(idlist)
    
    #buscar con los ids obtenidos
    en.email = "manuela.moscoso@est.ikiam.edu.ec.com"
    handle = en.efetch(db="pubmed", id=i_d, retmode="xml")
    
    
    #la funcion arroja la lista de ids
    respuesta = i_d.split(",")
    return (respuesta)


#SEGUNDA FUNCION
def mining_pubs(keyword,tipo):
    """Generar data frames para las variables introducidas
            -Parametros
                keyword= string con el termino de busqueda
                tipo=Sring con el codigo para obtener infromacion especifica de cada resultado
                      'AD' = Afiliacion
                      'PD' = Fecha de publicacion
                      'AU' = Autores
            -Output
                *Si el tipo es "DP" recupera el año de publicación del artículo. El retorno es un dataframe con el PMID y el DP_year.
                *Si el tipo es "AU" recupera el número de autores por PMID. El retorno es un dataframe con el PMID y el num_auth.
                *Si el tipo es "AD" recupera el conteo de autores por país. El retorno es un dataframe con el country y el num_auth.
                """
    
    #importar paquetes
    from Bio import Entrez as en
    import pandas as pd
    from collections import Counter
    import re
 
    #notificar correo
    en.email = "manuela.moscoso@est.ikiam.edu.ec.com"


    #realizar la busqueda
    handle= en.esearch(db="pubmed", term=keyword,usehistory="y",retmax=100,retmode=xml)
    record = en.read(handle)
    idlist = record["IdList"]
    i_d=",".join(idlist)
    #handle = en.efetch(db="pubmed", id=i_d, retmode="text")
    #record = en.read(handle)
   #POSIBLE MODIFICACION 
    resultados=[]
    for item in idlist:
        with en.efetch(db="pubmed", rettype="gb", retmode="text", id=item)as handle:
            resultados.append(en.read(handle))
            return resultados
    #almacenar datos     
    
    #PMID
    PMID = re.findall("PMID- (\d*)", resultados)
    
    #Fecha de publicacion (DP)
    DP = re.findall("DP\s{2}-\s(\d{4})", resultados) 
    
    #Autores (AU)
    AU = resultados.split("PMID- ")
    
    #a continuacion contar el numero de autores 
    AU.pop(0)
    n_au= []
    for item in range(len(AU)):
        autores = re.findall("AU -", AU[item])
        au = (len(autores))
        n_au.append(au)
    
    #Afiliacion (AD)
    #buscar unicamente los paises en cada direccion
    resultados = re.sub(r"Av\.","", resultados)
    AD = texto.split("AD  - ")
    #contar las repeticiones por pais
    n_ad = []
    for item in range(len(AD)): 
        pais = re.findall("\S, ([A-Za-z]*)\.", AD[item])
        if not pais_n == []: 
            if not len(pais_n) >= 2:  
                if re.findall("^[A-Z]", pais_n[0]): 
                    n_ad.append(pais_n[0])
    repeticiones=Counter(n_paises)
    resultado = {}
    for elemento in repeticiones:
        valor = repeticiones[elemento]
        if valor != 1: 
            resultado[elemento] = valor
            rep_pais = pd.DataFrame()
            rep_pais["country"] = resultado.keys()
            rep_pais["num_auth"] = resultado.values()
            
    #Mostrar los rsultados de acuerdo al TIPO
    if tipo == "DP":
        return pd.DataFrame(list(zip(PMID,DP)),columns=['PMID','DP_year'])
    
    elif tipo == "AU":
        return pd.DataFrame(list(zip(PMID,n_au)),columns=['PMID','num_auth'])
    
    elif tipo == "AD":
        return rep.pais