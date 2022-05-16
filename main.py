import pandas as pd
import numpy as np
import random

from datetime import datetime, timedelta


def create_dataframe(city, first_date, nb_year):
    date = [first_date + timedelta(days=i) for i in range(365)]
    nb_cities = len(city)
    date = date * nb_cities
    cities = list(city.keys()) * nb_year * 365
    date.sort()
    df = pd.DataFrame({"date": date, "cities": cities})
    for c in city:
        df.loc[df[df["cities"] == str(c)].index, "population"] = city[c][
            "population"
        ]
        df.loc[df[df["cities"] == str(c)].index, "nb_bikes"] = city[c][
            "nb_bikes"
        ]

    return df


def add_nb_users(df):
    for idx, row in df.iterrows():
        if row["cities"] == "Lyon":
            df.loc[idx, "Temp_Nb_User"] = random.randint(
                row["population"] * 0.005, row["population"] * 0.008
            )
        if row["cities"] == "Paris":
            df.loc[idx, "Temp_Nb_User"] = random.randint(
                row["population"] * 0.005, row["population"] * 0.008
            )
        if row["cities"] == "Rennes":
            df.loc[idx, "Temp_Nb_User"] = random.randint(
                row["population"] * 0.01, row["population"] * 0.02
            )
        if row["cities"] == "Nantes":
            df.loc[idx, "Temp_Nb_User"] = random.randint(
                row["population"] * 0.01, row["population"] * 0.02
            )
        if row["cities"] == "Berlin":
            df.loc[idx, "Temp_Nb_User"] = random.randint(
                row["population"] * 0.002, row["population"] * 0.004
            )
    for idx, row in df.iterrows():
        if row["cities"] == "Lyon":
            df.loc[idx, "Broken_Bikes_Temp"] = random.uniform(
                row["nb_bikes"] * 0.02, row["nb_bikes"] * 0.09
            )
        if row["cities"] == "Paris":
            df.loc[idx, "Broken_Bikes_Temp"] = random.uniform(
                row["nb_bikes"] * 0.05, row["nb_bikes"] * 0.08
            )
        if row["cities"] == "Rennes":
            df.loc[idx, "Broken_Bikes_Temp"] = random.uniform(
                row["nb_bikes"] * 0.05, row["nb_bikes"] * 0.08
            )
        if row["cities"] == "Nantes":
            df.loc[idx, "Broken_Bikes_Temp"] = random.uniform(
                row["nb_bikes"] * 0.05, row["nb_bikes"] * 0.08
            )
        if row["cities"] == "Berlin":
            df.loc[idx, "Broken_Bikes_Temp"] = random.uniform(
                row["nb_bikes"] * 0.01, row["nb_bikes"] * 0.02
            )
    i = 0
    for idx, row in df[df["cities"] == "Lyon"].iterrows():
        df.loc[idx, "Nb_User"] = list(
            df["Temp_Nb_User"].sort_values(ascending=True)
        )[i]
        i += 1

    for idx, row in df[df["cities"] == "Paris"].iterrows():
        df.loc[idx, "Nb_User"] = list(
            df["Temp_Nb_User"].sort_values(ascending=True)
        )[i]
        i += 1

    for idx, row in df[df["cities"] == "Rennes"].iterrows():
        df.loc[idx, "Nb_User"] = list(
            df["Temp_Nb_User"].sort_values(ascending=True)
        )[i]
        i += 1

    for idx, row in df[df["cities"] == "Nantes"].iterrows():
        df.loc[idx, "Nb_User"] = list(
            df["Temp_Nb_User"].sort_values(ascending=True)
        )[i]
        i += 1

    for idx, row in df[df["cities"] == "Berlin"].iterrows():
        df.loc[idx, "Nb_User"] = list(
            df["Temp_Nb_User"].sort_values(ascending=True)
        )[i]
        i += 1

    i = 0
    for idx, row in df[df["cities"] == "Lyon"].iterrows():
        df.loc[idx, "Broken_Bikes"] = list(
            df["Broken_Bikes_Temp"].sort_values(ascending=False)
        )[i]
        i += 1

    for idx, row in df[df["cities"] == "Paris"].iterrows():
        df.loc[idx, "Broken_Bikes"] = list(
            df["Broken_Bikes_Temp"].sort_values(ascending=False)
        )[i]
        i += 1

    for idx, row in df[df["cities"] == "Rennes"].iterrows():
        df.loc[idx, "Broken_Bikes"] = list(
            df["Broken_Bikes_Temp"].sort_values(ascending=False)
        )[i]
        i += 1

    for idx, row in df[df["cities"] == "Nantes"].iterrows():
        df.loc[idx, "Broken_Bikes"] = list(
            df["Broken_Bikes_Temp"].sort_values(ascending=False)
        )[i]
        i += 1

    for idx, row in df[df["cities"] == "Berlin"].iterrows():
        df.loc[idx, "Broken_Bikes"] = list(
            df["Broken_Bikes_Temp"].sort_values(ascending=False)
        )[i]
        i += 1

    del df["Broken_Bikes_Temp"]
    del df["Temp_Nb_User"]
    return df


def add_nb_trips_km(df):
    for idx, row in df.iterrows():
        if row["cities"] == "Lyon":
            df.loc[idx, "Nb_Trips"] = random.randint(
                row["Nb_User"] * 2, row["Nb_User"] * 3
            )
        if row["cities"] == "Paris":
            df.loc[idx, "Nb_Trips"] = random.randint(
                row["Nb_User"] * 2, row["Nb_User"] * 3
            )
        if row["cities"] == "Rennes":
            df.loc[idx, "Nb_Trips"] = random.randint(
                row["Nb_User"] * 3, row["Nb_User"] * 4
            )
        if row["cities"] == "Nantes":
            df.loc[idx, "Nb_Trips"] = random.randint(
                row["Nb_User"] * 3, row["Nb_User"] * 4
            )
        if row["cities"] == "Berlin":
            df.loc[idx, "Nb_Trips"] = random.randint(
                row["Nb_User"] * 5, row["Nb_User"] * 6
            )

    for idx, row in df.iterrows():
        if row["cities"] == "Lyon":
            df.loc[idx, "Nb_Km"] = random.uniform(
                row["Nb_Trips"] * 1, row["Nb_Trips"] * 1.5
            )
        if row["cities"] == "Paris":
            df.loc[idx, "Nb_Km"] = random.uniform(
                row["Nb_Trips"] * 1, row["Nb_Trips"] * 1.5
            )
        if row["cities"] == "Rennes":
            df.loc[idx, "Nb_Km"] = random.uniform(
                row["Nb_Trips"] * 2, row["Nb_Trips"] * 3
            )
        if row["cities"] == "Nantes":
            df.loc[idx, "Nb_Km"] = random.uniform(
                row["Nb_Trips"] * 0.2, row["Nb_Trips"] * 0.5
            )
        if row["cities"] == "Berlin":
            df.loc[idx, "Nb_Km"] = random.uniform(
                row["Nb_Trips"] * 2, row["Nb_Trips"] * 2.5
            )
    return df


if __name__ == "__main__":
    first_date = datetime.strptime("01/01/2020", "%m/%d/%Y")

    city = ["Paris", "Rennes", "Nantes", "Berlin", "Lyon"]
    city = {
        "Lyon": {"population": 500000, "nb_bikes": 400},
        "Paris": {"population": 2100000, "nb_bikes": 200},
        "Rennes": {"population": 215000, "nb_bikes": 100},
        "Nantes": {"population": 300000, "nb_bikes": 150},
        "Berlin": {"population": 3600000, "nb_bikes": 150},
    }
    df = create_dataframe(city, first_date, 1)
    df = add_nb_users(df)
    df = add_nb_trips_km(df)

    df.to_csv(r"./data/results.csv", index=False)
