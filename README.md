# Desafio Nexxera

Projeto realizado para o desafio de estágio de tradução da Nexxera

## Descrição

O projeto recebe uma planilha no formato XLSX, da qual os dados são extraídos e formatados de acordo com um padrão pré-definido. Ao final do processamento, é gerado um arquivo CSV contendo as modificações aplicadas

### Instalação

* Clone o projeto com o comando:

```bash
$ git clone https://github.com/grodrigues04/Desafio-Nexxera
```
* Entre dentro da pasta "Desafio-Nexxera"
* Na raiz do projeto, digite o seguinte comando para instalar as dependências :

```bash
$ pip install -r ./requirements/requirements.txt
```

## Configurações e raciocínio:
Uma das exigências do desafio era que a aplicação fosse capaz de processar outros arquivos, desde que estes mantivessem a mesma estrutura do arquivo “arquivo_entrada.xls”. Diante disso, a abordagem adotada no desenvolvimento foi a separação das responsabilidades das funções, de modo a facilitar futuras manutenções, correções de problemas e a adaptação para novos arquivos.

Para a função responsável pelas formatações, optei pelo uso da estrutura match case do Python em vez de múltiplos if, aliada ao uso de constantes, com o objetivo de tornar o código mais legível e facilitar possíveis manutenções futuras.

## Execução:
Depois de baixar as dependências , o código pode ser executado da seguinte maneira:

```bash
$ python3 main.py nome_arquivo_de_entrada nome_para_o_arquivo_de_saida
```
Exemplo de uso:

```bash
$ python3 main.py data/arquivo_entrada.xlsx output
```
 * Caso nenhum nome seja passado para o arquivo de saída, é gerado com com nome padrão "output".

### Observações
* Nas instruções do desafio, não ficou muito claro como deveria ser formatado a coluna K. Sendo assim, implementei a lógica onde o número tem virgulas a cada 3 digitos, finalizando com uma virgula para os últimos dois.

