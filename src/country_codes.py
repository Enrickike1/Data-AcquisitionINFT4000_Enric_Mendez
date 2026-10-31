import pandas as pd
import pycountry


COUNTRY_ALIASES = {
    "Bahamas, The": "BS",
    "Congo, Dem. Rep.": "CD",
    "Congo, Rep.": "CG",
    "Cote d'Ivoire": "CI",
    "Curacao": "CW",
    "Egypt, Arab Rep.": "EG",
    "Gambia, The": "GM",
    "Hong Kong SAR, China": "HK",
    "Iran, Islamic Rep.": "IR",
    "Korea, Dem. People's Rep.": "KP",
    "Korea, Rep.": "KR",
    "Lao PDR": "LA",
    "Macao SAR, China": "MO",
    "Micronesia, Fed. Sts.": "FM",
    "Niger": "NE",
    "Nigeria": "NG",
    "Kosovo": "XK",
    "Puerto Rico (US)": "PR",
    "Russian Federation": "RU",
    "Somalia, Fed. Rep.": "SO",
    "St. Kittsand Nevis": "KN",
    "St. Kitts and Nevis": "KN",
    "St. Lucia": "LC",
    "St. Martin (French part)": "MF",
    "St. Vincent and the Grenadines": "VC",
    "Taiwan, China": "TW",
    "Turkiye": "TR",
    "Venezuela, RB": "VE",
    "Virgin Islands (U.S.)": "VI",
    "West Bank and Gaza": "PS",
    "Yemen, Rep.": "YE",
}


def country_to_iso2(name):
    if name in COUNTRY_ALIASES:
        return COUNTRY_ALIASES[name]

    for country in pycountry.countries:
        names = [
            getattr(country, "name", ""),
            getattr(country, "common_name", ""),
            getattr(country, "official_name", ""),
        ]
        if name.casefold() in {value.casefold() for value in names if value}:
            return country.alpha_2

    return pd.NA
