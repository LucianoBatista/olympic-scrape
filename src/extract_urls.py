import random
from time import sleep

import requests
from bs4 import BeautifulSoup
from rich import print
from tqdm import tqdm
from urlextract import URLExtract

# all news urls from olympic site
with open("./links.md", "r") as r:
    data = r.read()

extractor = URLExtract()
urls = extractor.find_urls(data)

# keeping just those urls about news
clean_urls = [url for url in urls if "noticia" in url]
unique_urls = list(set(clean_urls))

# creating an agent to be able to pull the content
session = requests.Session()


# to extract the source code
# for url in tqdm(unique_urls):
#     try:
#         print(url)
#         user_agents = [
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
#             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
#         ]
#         session.headers.update({"User-Agent": random.choice(user_agents)})
#         response = session.get(
#             url,
#             timeout=10,
#         )
#
#         # saving to try extract the content of the news
#         name = url.split("/")[-1]
#         with open("./data/text_extraction/{}.txt".format(name), "w") as f:
#             f.write(response.text)
#     except:
#         print("Sleeping more 10 seconds")
#         sleep(10)
#         user_agents = [
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
#             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
#         ]
#         session.headers.update({"User-Agent": random.choice(user_agents)})
#         response = session.get(
#             url,
#             timeout=10,
#         )
#
#         # saving to try extract the content of the news
#         name = url.split("/")[-1]
#         with open("./data/text_extraction/{}.txt".format(name), "w") as f:
#             f.write(response.text)
#
#     sleep(2)
