import pandas as pd


trafficking = pd.read_csv("data/human_trafficking.csv")

trafficking = trafficking[~trafficking["citizenship"].isin(["-99", "00"])]

victims = (
    trafficking.groupby(["citizenship", "yearOfRegistration"])
    .size()
    .reset_index(name="victim_count")
)

poverty = pd.read_csv("data/poverty.csv")

merged = victims.merge(
    poverty,
    on=["citizenship", "yearOfRegistration"],
    how="left",
)

print(merged.head())
