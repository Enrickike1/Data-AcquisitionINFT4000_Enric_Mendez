import pandas as pd
from bs4 import BeautifulSoup
from html import unescape
from io import StringIO


trafficking = pd.read_csv(
    "data/human_trafficking.csv",
    low_memory=False,
).sample(
    n=10000,
    random_state=42,
)

trafficking = trafficking[~trafficking["citizenship"].isin(["-99", "00"])]

victims = (
    trafficking.groupby("citizenship")
    .size()
    .reset_index(name="victim_count")
)

print(victims.head())
print(f"Rows in sample: {len(trafficking)}")
print(f"Countries found: {len(victims)}")

with open("data/world_bank_poverty.html", encoding="utf-8") as file:
    saved_page = BeautifulSoup(file.read(), "html.parser")

html = "\n".join(
    line.get_text() for line in saved_page.select(".line-content")
)
html = unescape(html)

poverty = pd.read_html(
    StringIO(html),
    attrs={"id": "scrollTable"},
)[0]

print(poverty.head())
print(poverty.columns)