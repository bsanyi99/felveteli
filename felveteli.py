#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd

fileName = "data.csv"
dateCol = "date"


def main():
    # Adatok beolvasása CSV fileból
    df = pd.read_csv(fileName, header=0, parse_dates=[dateCol])
    # print(df.shape)
    print(df.info())

    # dátum szerint rendezés
    df = df.sort_values(by="date")

    # adatok csoportosítása
    gdf = df.groupby("asset")

    # Árfolyam- idő chartok ábrázolása
    for group_name, group_data in gdf:
        plt.plot(group_data["date"], group_data["price"], label=group_name)

    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend(title="Assets")
    # plt.show()
    plt.savefig("assets.png")

    # Statisztika készítése asset-re lebontva
    statistics = gdf["price"].agg(["min", "max", "median", "mean", "std"])
    print(statistics)


##############################################################################

if __name__ == "__main__":
    main()
