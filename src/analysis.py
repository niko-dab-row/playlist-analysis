import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)

    df["ts"] = pd.to_datetime(df["ts"])

    return df


def calculate_top_artists(df, top_n=10):

    result = (
        df.groupby("master_metadata_album_artist_name")
        ["ms_played"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        / (1000 * 60 * 60)
    )

    return result


def calculate_top_tracks(df, top_n=10):

    result = (
        df.groupby("master_metadata_track_name")
        ["ms_played"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        / (1000 * 60)
    )

    return result


def listening_by_year(df):

    return (
        df.groupby(df["ts"].dt.year)
        ["ms_played"]
        .sum()
        / (1000 * 60 * 60)
    )


def listening_by_month(df):

    month_data = (
        df.groupby(
            df["ts"].dt.to_period("M")
        )["ms_played"]
        .sum()
        / (1000 * 60 * 60)
    )

    return month_data


if __name__ == "__main__":

    df = load_data("../data/spotify_history.csv")

    print("Top Artists")
    print(calculate_top_artists(df))

    print("\nTop Songs")
    print(calculate_top_tracks(df))
