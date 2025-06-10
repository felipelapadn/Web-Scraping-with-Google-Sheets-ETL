# Projeto ETL - Books to Scrape

Este projeto realiza um pipeline **ETL (Extract, Transform, Load)** para coletar informações de livros no site [Books to Scrape](https://books.toscrape.com), transformá-las e carregá-las em uma planilha do Google Sheets.

---

## Estrutura do Projeto

```bash
etl_books/
│
├── config/                 # Configurações e credenciais
│   └── settings.yaml
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
├── main.py                 # Orquestra o processo ETL completo
└── README.md               # Este arquivo
```

---

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

  * Em andamento.

## Tecnologias Utilizadas - até o momento

* `requests`, `BeautifulSoup` – Web scraping
* `pandas` – Transformação de dados
