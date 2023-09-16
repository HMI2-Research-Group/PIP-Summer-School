import pandas as pd


def read_tsv(path):
    return pd.read_csv(path, sep="\t", skiprows=1)
