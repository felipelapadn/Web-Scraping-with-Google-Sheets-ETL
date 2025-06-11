class TransformData:
    
    def __init__(self, df):
        self.df = df.copy()
        self.map_rating = {
            "Zero": 0,
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }
        self.dict_rename = {
            "genero": "book_genre",
            "nome": "name",
            "imagem": "image"
        }

    def encontrar_colunas_constantes(self):
        colunas_constantes = []
        for coluna in self.df.columns:
            if self.df[coluna].nunique() == 1:
                colunas_constantes.append(coluna)
        return colunas_constantes

    def processar(self):
        
        self.df.rating = self.df.rating.map(self.map_rating)

        if self.df[self.df.price_com_taxa == self.df.price_sem_taxa].shape[0] == self.df.shape[0]:
            self.df["price_gbp"] = self.df.price_com_taxa
            self.df.drop(["price_com_taxa", "price_sem_taxa"], axis=1, inplace=True)

        self.df['price_gbp'] = self.df['price_gbp'].replace('[£]', '', regex=True).astype(float)
        self.df['available_stock'] = self.df['estoque'].str.extract(r'(\d+)').astype(int)
        self.df['stock'] = self.df['estoque'].str.contains('In stock')

        self.df.drop(["estoque"], axis=1, inplace=True)

        self.df = self.df.rename(columns=self.dict_rename)
        
        colunas_constantes = self.encontrar_colunas_constantes()

        self.df = self.df.drop(columns=colunas_constantes)
        
        self.df.to_csv("data/processed_dataset.csv", index=False)

        return self.df