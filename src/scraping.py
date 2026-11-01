import requests
from bs4 import BeautifulSoup


def scrape_table(url, table_id=None):
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", id=table_id) if table_id else soup.find("table")
    if table is None:
        raise ValueError(f"No table found at {url}")

    rows = []
    for row in table.find_all("tr"):
        cells = row.find_all(["th", "td"])
        values = [cell.get_text(" ", strip=True) for cell in cells]
        if values:
            rows.append(values)

    return rows
