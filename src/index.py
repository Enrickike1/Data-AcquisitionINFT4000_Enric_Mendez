import pandas as pd

from country_codes import country_to_iso2
from scraping import scrape_table


# Load a reproducible sample and count victims by nationality.
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


# Scrape and prepare the World Bank poverty table.
poverty_rows = scrape_table(
    "https://wdi.worldbank.org/table/1.2",
    table_id="scrollTable",
)
poverty = pd.DataFrame(
    [
        row[:5]
        for row in poverty_rows
        if len(row) >= 5
        and row[1] in {".."} | set(str(year) for year in range(1900, 2101))
    ],
    columns=[
        "country_name",
        "poverty_year",
        "poverty_rate",
        "poverty_rate_4_20",
        "poverty_rate_8_30",
    ],
).iloc[:, [0, 1, 2]]
poverty.columns = ["country_name", "poverty_year", "poverty_rate"]
poverty["poverty_rate"] = pd.to_numeric(
    poverty["poverty_rate"].replace("..", pd.NA),
    errors="coerce",
)
poverty["citizenship"] = poverty["country_name"].apply(country_to_iso2)

merged = victims.merge(poverty, on="citizenship", how="left")
merged.to_csv("data/trafficking_poverty.csv", index=False)

print(merged.head())
print(f"Matched countries: {merged['poverty_rate'].notna().sum()} of {len(merged)}")
print("Countries not converted:", poverty.loc[
    poverty["citizenship"].isna(),
    "country_name",
].tolist())


# Scrape and prepare the corruption ranking.
corruption_rows = scrape_table(
    "https://factsinstitute.com/ranking/most-corrupt-countries-in-the-world/"
)
corruption = pd.DataFrame(
    [
        row[:4]
        for row in corruption_rows
        if len(row) >= 4 and row[1].isdigit()
    ],
    columns=[
        "country_name",
        "corruption_score",
        "corruption_score_2021",
        "corruption_score_2016",
    ],
)
corruption["corruption_score"] = pd.to_numeric(
    corruption["corruption_score"],
    errors="coerce",
)
corruption["citizenship"] = corruption["country_name"].apply(country_to_iso2)

final = merged.merge(
    corruption[
        [
            "citizenship",
            "corruption_score",
            "corruption_score_2021",
            "corruption_score_2016",
        ]
    ],
    on="citizenship",
    how="left",
)

final.to_csv("data/trafficking_poverty_corruption.csv", index=False)

print(final.head())
print(
    "Matched corruption countries:",
    final["corruption_score"].notna().sum(),
    "of",
    len(final),
)
print("Corruption countries not converted:", corruption.loc[
    corruption["citizenship"].isna(),
    "country_name",
].tolist())
