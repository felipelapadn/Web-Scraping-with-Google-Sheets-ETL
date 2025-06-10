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

        colunas_constantes = self.ncontrar_colunas_constantes(self.df)

        df_tratado = self.df.drop(columns=colunas_constantes)

        if df_tratado[df_tratado.price_com_taxa == df_tratado.price_sem_taxa].shape[0] == df_tratado.shape[0]:
            df_tratado["price_gbp"] = df_tratado.price_com_taxa
            df_tratado.drop(["price_com_taxa", "price_sem_taxa"], axis=1, inplace=True)

        df_tratado['price_gbp'] = df_tratado['price_gbp'].replace('[£]', '', regex=True).astype(float)
        df_tratado['available_stock'] = df_tratado['estoque'].str.extract(r'(\d+)').astype(int)
        df_tratado['stock'] = df_tratado['estoque'].str.contains('In stock')

        df_tratado.drop(["estoque"], axis=1, inplace=True)

        df_tratado = df_tratado.rename(columns=self.dict_rename)

        colunas = ['name', 'rating', 'book_genre', 'price_gbp', 'available_stock', 'stock', 'image']
        df_tratado = df_tratado[colunas]
        
        return df_tratado