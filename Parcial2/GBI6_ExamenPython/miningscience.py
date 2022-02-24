#PRIMERA FUNCION
def download_pubmed(keyword):
    """Descargar la data de pubmed
            -Parametros
                keyword= string con el termino de busqueda
            -Output
                Lista que contiene los IDs de los resultados encontrados
    """
    
    #importar paquetes
    import Bio
    from Bio import Entrez as en
    from Bio import Medline as md
    
    #notificar correo
    en.email = "manuela.moscoso@est.ikiam.edu.ec.com"

    #definir termino de busqueda
    busqueda=keyword+"[Title/Abstract]"
    
    #realizar la busqueda
    handle= en.esearch(db="pubmed", term=busqueda)
    record = en.read(handle)
    return (record.get("IdList"))

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
    import Bio
    from Bio import Entrez as en
    from Bio import Medline as md
    import pandas as pd
    import numpy as np
    import re
    
    #notificar correo
    en.email = "manuela.moscoso@est.ikiam.edu.ec.com"
    
    #definir termino de busqueda
    busqueda=keyword+"[Title/Abstract]"

    #realizar la busqueda
    handle= en.esearch(db="pubmed", term=busqueda)
    record = en.read(handle)
    idlist = record["IdList"]
    handle = en.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")

    #almacenar los resultados para su manipulacion
    records=md.parse(handle)

    #crear las listas con los resultados
    lsresult=[]
    for record in records:
        
        #registrar los PMIDs
        pubmedid=record['PMID']
        pmid_dict.append(pubmedid)
        
        if tipo=='AU':
        #mostrar los autores
        autores=record['AU']
        au_dict.append(autores)
        #generar la sumatoria de autores
        contador=[len (i) for i in au_dict ]
        return df_autores=pd.DataFrame(list(zip(pmid_dict,contador)),columns=['PMID','num_auth'])
        
        if tipo=='AD'
        #mostrar los paises
        paises=record['AD'] #He estado usando AD y me da SYNTAX ERROR
        ad_dict.append(paises)
        return df_paises=pd.DataFrame(list(zip(ad_dict,contador)),columns=['country','num_auth'])

        if tipo=='DP'
        #mostrar la fecha
        fecha=record['DP']
        dp_dict.append(fecha)
        #crear los data frames a partir de las listas obtenidas
        return df_fecha=pd.DataFrame(list(zip(pmid_dict,dp_dict)),columns=['PMID','DP_year'])

