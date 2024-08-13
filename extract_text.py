import os

import polars as pl
from bs4 import BeautifulSoup

files = os.listdir("./data/text_extraction/")

authors = []
titles = []
contents = []

for file in files:
    with open("./data/text_extraction/{}".format(file), "r") as f:
        text = f.read()

    soup = BeautifulSoup(text, "html.parser")
    span_author = soup.find("span", {"data-cy": "story-header-author"})
    span_title = soup.find("h1", {"data-cy": "story-header-title"})

    # Not every data is available on the html tags we are looking for
    try:
        authors.append(span_author.get_text())
    except:
        authors.append(None)

    try:
        titles.append(span_title.get_text())
    except:
        titles.append(None)

    try:
        contents.append(soup.get_text())
    except:
        contents.append(None)


df_blogposts = pl.DataFrame(
    {
        "author": authors,
        "title": titles,
        "content": contents,
        "names": [file.split(".")[0] for file in files],
    }
)
df_urls = pl.read_csv("./data/url_name_table.csv")
final_df = df_blogposts.join(df_urls, on="names", how="left")
final_df.write_csv("./data/paris_pt_news_2024.csv")
