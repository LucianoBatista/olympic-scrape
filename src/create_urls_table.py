import os

import polars as pl
from bs4 import BeautifulSoup
from urlextract import URLExtract

# urls
with open("./links.md", "r") as r:
    data = r.read()

extractor = URLExtract()
urls = extractor.find_urls(data)
clean_urls = [url for url in urls if "noticia" in url]
unique_urls = list(set(clean_urls))
urls_name = zip(unique_urls, [unique.split("/")[-1] for unique in unique_urls])

df = pl.DataFrame(urls_name).rename({"column_0": "urls", "column_1": "names"})
df.write_csv("./data/url_name_table.csv")
