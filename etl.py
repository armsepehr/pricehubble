from core.extract import Extractor
from core.transform import Transformer
from core.load import Loader

#extraction
e = Extractor()
df = e.load()

# transformer
t = Transformer(df)
t.drop_invalidate_data()
t.convert_format()
t.get_price()
t.drop_unnccessary_column()
t.requirement()

# loader
l = Loader()
l.store(t.data,".")
