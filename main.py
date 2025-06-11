from extract.scraper import ScraperLivros
from transform.clean_data import TransformData
from load.to_google_sheets import Planilha
import os
import pandas as pd

def run_etl():
    scraper = ScraperLivros()
    df_results = scraper.rodar()
        
    processor = TransformData(df_results)
    df_tratado = processor.processar()  
      
    planilha_obj = Planilha()
    planilha = planilha_obj.carregar_credenciais()
    valores_para_add = [df_tratado.columns.tolist()] + df_tratado.values.tolist()
    planilha_obj.atualizar_planilha(planilha, valores_para_add)

if __name__ == "__main__":
    run_etl()