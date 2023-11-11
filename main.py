import xmltodict
import os
import pandas as pd
from utility import extrair_infos_nf, extrair_peso_bruto, extrair_infos_cliente

# Função para ler e parsear o arquivo XML
def ler_arquivo_xml(nome_arquivo):
    with open(f'nfs/{nome_arquivo}', 'rb') as arquivo_xml:
        return xmltodict.parse(arquivo_xml)


# Função principal para extrair todas as informações
def pegar_infos(nome_arquivo, valores):
    dic_arquivo = ler_arquivo_xml(nome_arquivo)
    infos_nf = extrair_infos_nf(dic_arquivo)
    numero_da_nota = infos_nf['@Id']
    emissor_da_nota = infos_nf['emit']['xNome']
    nome_do_cliente, endereco = extrair_infos_cliente(infos_nf)
    peso_bruto = extrair_peso_bruto(infos_nf)
    valores.append([numero_da_nota, emissor_da_nota, nome_do_cliente, endereco, peso_bruto])


lista_arquivos = os.listdir('nfs')


colunas = ["numero_da_nota",
           "emissor_da_nota",
           "nome_do_cliente",
           "endereco",
           "peso_bruto"]
valores = []

for arquivo in lista_arquivos:
    pegar_infos(arquivo, valores)
    
tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel('NotasFiscais.xlsx', index=False)