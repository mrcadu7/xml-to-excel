# XML to XLSX

O projeto pega arquivos XML em massa, os parseia, cria um dataframe e exporta para um arquivo XLSX.

## Descrição

Este projeto consiste em ler arquivos XML em um diretório específico, fazer o parsing desses arquivos utilizando a biblioteca xmltodict e extrair informações específicas de cada arquivo. As informações extraídas são armazenadas em um dataframe utilizando a biblioteca Pandas. Por fim, o dataframe é exportado para um arquivo XLSX.

## Como executar

1. Certifique-se de ter todas as dependências listadas no arquivo `requirements.txt` instaladas em seu ambiente Python.

2. Coloque os arquivos XML que você deseja processar no diretório `nfs`.

3. Execute o arquivo `main.py` para iniciar o processamento dos arquivos XML.

4. Após a execução, o arquivo `NotasFiscais.xlsx` será gerado no diretório raiz do projeto contendo os dados extraídos dos arquivos XML.


## Contribuição

Qualquer contribuição para melhorar este projeto é bem-vinda! Sinta-se à vontade para abrir uma nova issue ou enviar um pull request.
