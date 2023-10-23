import pandas as pd

class Transformer:

    def __init__(self,df: pd.DataFrame = None):
        self.data = df
    
    def __set_data__(self):
        pass

    def drop_invalidate_data(self):
        df = self.data

        # string contain a price
        has_digit = df['raw_price'].str.contains(r'\d', regex=True)
        df = df[has_digit]
        df = df.reset_index(drop=True)

        # check string format
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        mask = df['scraping_date'].str.match(pattern)
        df.drop(df[~mask].index, inplace=True)

        # check for possible value for property type
        mask = df['property_type'].isin(["apartment","house"])
        df = df[mask]
        df = df.reset_index(drop=True)

        self.data = df

    def get_price(self):
        df = self.data
        df['price'] = df['raw_price'].str.extract(r'(\d+\.\d+)').astype(float)
        df = df.drop("raw_price", axis=1)
        self.data = df

    def convert_format(self):
        df = self.data
        df['living_area'] = df['living_area'].astype(float)
        self.data = df        

    def drop_unnccessary_column(self):
        df = self.data
        df = df.drop("municipality", axis=1)
        self.data = df
        
    def requirement(self):
        df = self.data
        price_per_square_meter = df["price"]/df["living_area"]
        mask = (500<price_per_square_meter) & (price_per_square_meter<15000)
        df = df[mask]
        self.data = df
