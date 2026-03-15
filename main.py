import random as rd
import pandas as pd

from typing import Union, List


def remove_ineligibles(df: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
    return df[(df["Score"] > 5) & (df["Score"] < 14)]


def weighted_random(df: pd.DataFrame | pd.Series, nbr_winner=1) -> List[str]:
    if df.empty:
        return []
    if (nbr_winner <= 0) or (nbr_winner > len(df)):
        raise ValueError(
            "Number of winners must be between 1 and the number of eligible entries."
        )
    winners = []
    for i in range(nbr_winner):
        weights = df["Score"].tolist()
        chosen = df.sample(n=1, weights=weights)
        df.drop(chosen.index, inplace=True)
        winners.append(chosen["Nom"].iloc[0])

    return winners


def main(csvfile="./example.csv", nbr_winner=2):
    df = pd.read_csv(csvfile)
    df = remove_ineligibles(df)
    choices = weighted_random(df, nbr_winner)
    pd.DataFrame(choices, columns=["Winners"]).to_csv("winners.csv", index=False)
    print(choices)


if __name__ == "__main__":
    main()
