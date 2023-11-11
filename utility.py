# Função para extrair as informações da nota fiscal do dicionário
def extrair_infos_nf(dic_arquivo):
    if "NFe" in dic_arquivo:
        return dic_arquivo["NFe"]["infNFe"]
    elif "nfeProc" in dic_arquivo:
        return dic_arquivo['nfeProc']["NFe"]["infNFe"]
    else:
        return dic_arquivo["NFSe"]["infNFSe"]

# Função para extrair o peso bruto da nota fiscal
def extrair_peso_bruto(infos_nf):
    if "transp" in infos_nf and "vol" in infos_nf['transp']:
        return infos_nf['transp']['vol']['pesoB']
    else:
        return 'Nao informado'

# Função para extrair as informações do cliente da nota fiscal
def extrair_infos_cliente(infos_nf):
    if "dest" in infos_nf:
        return infos_nf['dest']['xNome'], infos_nf['dest']['enderDest']
    else:
        return infos_nf['DPS']['infDPS']['toma']['xNome'], infos_nf['DPS']['infDPS']['toma']['end']