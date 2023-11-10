import xmltodict
import os
import pandas as pd

def pegar_infos(nome_arquivo, valores):
    with open(f'nfs/{nome_arquivo}', 'rb') as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)

        if "NFe" in dic_arquivo:
            infos_nf = dic_arquivo["NFe"]["infNFe"]
        elif "nfeProc" in dic_arquivo:
            infos_nf = dic_arquivo['nfeProc']["NFe"]["infNFe"]
        else:
            infos_nf = dic_arquivo["NFSe"]["infNFSe"]

        numero_da_nota = infos_nf['@Id']
        emissor_da_nota = infos_nf['emit']['xNome']
        
        if "dest" in infos_nf:
            nome_do_cliente = infos_nf['dest']['xNome']
            endereco = infos_nf['dest']['enderDest']
        else:
            nome_do_cliente = infos_nf['DPS']['infDPS']['toma']['xNome']
            endereco = infos_nf['DPS']['infDPS']['toma']['end']
        if "transp" in infos_nf:
            if "vol" in infos_nf['transp']:
                peso_bruto = infos_nf['transp']['vol']['pesoB']
            else:
                peso_bruto = 'Nao informado'    
        else:
            peso_bruto = 'Nao informado'
            
        valores.append([numero_da_nota, emissor_da_nota, nome_do_cliente, endereco, peso_bruto])


lista_arquivos = os.listdir('nfs')


colunas = ["numero_da_nota", "emissor_da_nota", "nome_do_cliente", "endereco", "peso_bruto"]
valores = []

for arquivo in lista_arquivos:
    pegar_infos(arquivo, valores)
    
tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel('NotasFiscais.xlsx', index=False)