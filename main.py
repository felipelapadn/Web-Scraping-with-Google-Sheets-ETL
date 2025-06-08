from extract.scraper import ScraperLivros
from transform.clean_data import transform_data
from load.to_google_sheets import load_data

def run_etl():
    scraper = ScraperLivros()
    df_results = scraper.rodar()
    
    clean_data = TransformData(df_results)
    
    LoadData(clean_data)

if __name__ == "__main__":
    run_etl()
