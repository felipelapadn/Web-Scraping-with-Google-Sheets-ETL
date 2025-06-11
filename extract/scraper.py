from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import logging
from tqdm import tqdm

logging.basicConfig(filename='example.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class ScraperLivros:
    def __init__(self):
        self.links = list()
        self.df_results = pd.DataFrame()
        self.logger = logging.getLogger(__name__)

    def buscar_html(self, url):
        response = urlopen(url)
        html = response.read()
        if response.getcode() == 200:
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        else:
            raise Exception(
                f"Erro ao acessar {self.url}: {response.status_code}")

    def extrair_paginas_livros(self, num_pags: int = 50):
        for page in range(1, num_pags+1):
            url = f"https://books.toscrape.com/catalogue/page-{page}.html"
            try:
                soup = self.buscar_html(url)
            except Exception as e:
                raise e
            else:
                for h in soup.find("section").find_all_next("h3"):
                    href = h.find("a").get("href")
                    link = f"https://books.toscrape.com/catalogue/{href}"
                    self.links.append(link)
                self.logger.info(f'Scrapping da página {page} realizado.')

    def contruir_dataset_livros(self):
        for url in tqdm(self.links):
            df_book = pd.DataFrame()
            try:
                soup = self.buscar_html(url)
            except Exception as e:
                raise e
            else:
                h1_active = soup.find("h1")
                df_book["nome"] = [h1_active.get_text()]

                df_book["rating"] = [
                    soup.find("p", {"class": "star-rating"}).get('class')[-1]]

                ul_breadcrumb = soup.find(
                    "ul", {"class": "breadcrumb"}).find_all("a")
                df_book["genero"] = [ul_breadcrumb[-1].get_text()]

                infos = soup.find("table").find_all('tr')
                df_book["tipo"] = [infos[1].find("td").get_text()]
                df_book["price_com_taxa"] = [infos[2].find("td").get_text()]
                df_book["price_sem_taxa"] = [infos[3].find("td").get_text()]
                df_book["taxa"] = [infos[4].find("td").get_text()]
                df_book["estoque"] = [infos[5].find("td").get_text()]

                src = soup.find("div", {"class": "item"}
                                ).find("img").get("src")
                df_book["imagem"] = [
                    f"https://books.toscrape.com/{src.split('../..')[-1]}"]
                self.df_results = pd.concat([self.df_results, df_book])
                self.logger.info(f'Scrapping da url {url} realizado.')
        self.df_results.to_csv("data/raw_dataset.csv", index=False)

    def rodar(self):
        self.extrair_paginas_livros()
        self.logger.info('Páginas coletadas.')
        self.contruir_dataset_livros()
        self.logger.info('Dataset feito')
        return self.df_results
