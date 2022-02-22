def download_pubmed(keyword): 
    """Descargar la data de pubmed"""
    import Bio
    from Bio.Seq import Seq
    from Bio import Entrez
    Entrez.email = "manuela.moscoso@est.ikiam.edu.ec.com"
    resultados = Entrez.esearch(db="pubmed", 
                        term="keyword[Title/Abstract]")
    dic_resultados = Entrez.read(resultados)
    resultados.close()
    return dic_resultados.keys()

#def mining_pubs(tipo):
    #"""Según el tipo de dato extraer infromación específica"""
    #import re
    #if tipo == "AD":
        
    
    #return 

    
