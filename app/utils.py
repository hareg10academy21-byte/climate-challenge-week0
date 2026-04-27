import pandas as pd

def load_data():
    ethiopia = pd.read_csv("data/ethiopia_clean.csv")
    kenya = pd.read_csv("data/kenya_clean.csv")
    sudan = pd.read_csv("data/sudan_clean.csv")
    tanzania = pd.read_csv("data/tanzania_clean.csv")
    nigeria = pd.read_csv("data/nigeria_clean.csv")

    df = pd.concat([
        ethiopia,
        kenya,
        sudan,
        tanzania,
        nigeria
    ], ignore_index=True)

    return df