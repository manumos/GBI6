#Importar los paquetes de interés
import Bio
from Bio import Entrez as en
from bio import Medline as md
import pandas as pd
import numpy as np
import re

#Siempre decirle quien eres a NCBI
Entrez.email = "manuela.moscoso@est.ikiam.edu.ec.com"

#PRIMERA FUNCION
def download_pubmed(x):
    """Descargar la data de pubmed"""
    #definir termino de busqueda
    busqueda=x+"[Title/Abstract]"
    #realizar la busqueda
    handle= en.esearch(db="pubmed", term=busqueda)
    record = en.read(handle)
    record ["IdList"]
    #Descargar resultados de PUBMED
    idlist = record["IdList"]
    handle = en.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
        return
            records = Medline.parse(handle)

#SEGUNDA FUNCION
def mining_pubs(y)
    """Organizar la informacion en dataframes"""
    if y==DP
        #PMID y el DP_year
        records["PMID"]["DP"]
        return pd.dataframe()

    if y==AU
        #PMID y el num_auth
        records["PMID"]["AU"]
        return pd.dataframe()
    if y==AD
        #Country y el num_auth.
        records["PMID"]["AD"]["AU"]
            return pd.dataframe()
