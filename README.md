# Projeto ETL - Books to Scrape

Este projeto realiza um pipeline **ETL (Extract, Transform, Load)** para coletar informações de livros no site [Books to Scrape](https://books.toscrape.com), transformá-las e carregá-las em uma planilha do Google Sheets.

## Estrutura do Projeto

```bash
etl_books/
│
├── data/                 # Arquivos raw e processado
│
├── extract/                # Scripts de extração (web scraping)
│   └── scraper.py
│
├── transform/              # Scripts de limpeza e transformação
│   └── clean_data.py
│
├── load/                   # Scripts de carga (Google Sheets)
│   └── to_google_sheets.py
│
└── main.py                 # Orquestra o processo ETL completo
```

## Funcionalidades

* **Extração**:

  * Realiza scraping de todos os livros disponíveis no site.
  * Coleta título, preço, disponibilidade, classificação e categoria.

* **Transformação**:

  * Tranformação de colunas textuais em números.
      * Coluna de price: remoção do símbolo.
      * Coluna de estoque: separação do dado `In stock (22 available)` em duas colunas, uma para a existência do estoque (bool) e outra com a quantidade.
  * Exclusão das colunas com valores constantes.
  * Padronização do nome das colunas.

* **Load**:

  * Carrega as credenciais da API do google sheets.
  * Atualiza a planilha com os dados tratados.

## Tecnologias Utilizadas

* `requests`, `BeautifulSoup` – Web scraping.
* `pandas` – Transformação de dados.
* `google`, `google_auth_oauthlib`, `googleapiclient` – Conexção com o Google Cloud.
* `docker` - contrução de imagens e containers.

## Como Executar

### Pré-requisitos

* [Docker](https://www.docker.com/products/docker-desktop) instalado na máquina.
* (Opcional) [Make](https://www.gnu.org/software/make/) instalado para facilitar os comandos.
* É altamente recomendado seguir o tutorial para criar as credenciais: [Guia de início rápido do Python](https://developers.google.com/workspace/sheets/api/quickstart/python?hl=pt-br)

### 1. Build da imagem Docker

Se preferir rodar manualmente:

```bash
docker build -t nome-da-imagem .
```

Ou usando o Makefile:

```bash
make docker
```

### 2. Executar o container

Manual:

```bash
docker run -it nome-do-container
```

Ou via Makefile:

```bash
make run
```

### 4. Parar e remover o container (se executado em modo background)

Manual:

```bash
docker stop nome-do-container
docker rm nome-do-container
```

Ou via Makefile:

```bash
make clean
```

## Autor

**Felipe Lapa do Nascimento** ([LinkedIn](https://www.linkedin.com/in/felipelapadn/) | [Email](mailto:felipelapadn@gmail.com)) 