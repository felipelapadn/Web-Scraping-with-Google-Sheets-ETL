from extract.scraper import ScraperLivros
from transform.clean_data import TransformData
from load.to_google_sheets import load_data

def run_etl():
    scraper = ScraperLivros()
    df_results = scraper.rodar()
    
    processor = TransformData(df_results)
    df_tratado = processor.processar()    
    
    LoadData(df_tratado)

if __name__ == "__main__":
    run_etl()
