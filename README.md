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
Umas das exigencias do desafio era que a aplicação fosse capaz de suportar o processamento de outros arquivos, desde que, tenham a mesma estrutura do arquivo “arquivo_entrada.xls”. Sendo assim, a ideia de desenvolvimento foi separar as responsábilidades das funções de tal maneira que eventuais manutenções, correções de problemas e arquivos diferentes fossem fáceis de lidar. Além disso, criei um fluxo que permitesse que no momento da execução de um novo arquivo, fosse apenas descritas as colunas que devem ser formatadas.

 * Crie um arquivo .env na raiz do projeto que segue o mesmo exemplo do .env.example
 * COLUMN_ORDER: Nome da coluna que sera usado para determinar a ordem das linhas
 * ASCENDING: Para ordem crescente, deixe True. False para descrente.
 * COLUMNS_TO_FORMART: Aqui, o nome das colunas que vão ser formatadas devem ser colocadas, separando por virgulas.

Dessa maneira, o .ENV determina quais coluna devem ser formatadas, enquanto o arquivo de constantes determina qual o tipo de regra de formatação para cada coluna.

## Execução:
Após configurar o .env, para executar o projeto digite no terminal:

Linux
```bash
$ python3 main.py
```
Windows
```bash
$ python main.py
```

### Observações
* Nas instruções do desafio, não ficou muito claro como deveria ser formatado a coluna K. Devido as datas de final de ano, optei por não enviar nenhuma mensagem de dúvida. Sendo assim, criei uma formatação que adiciona "R$" no começo coloca ,00 no final em caso de não haver virgulas no número.

