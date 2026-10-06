import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def top_artists_chart(df):

    artists = (
        df.groupby("master_metadata_album_artist_name")
        ["ms_played"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        / (1000 * 60 * 60)
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=artists.values,
        y=artists.index
    )

    plt.title("Top 10 Artists")
    plt.xlabel("Hours Listened")

    plt.tight_layout()
    plt.savefig("../plots/top_artists.png")
    plt.close()


def monthly_activity_chart(df):

    monthly = (
        df.groupby(
            df["ts"].dt.to_period("M")
        )["ms_played"]
        .sum()
        / (1000 * 60 * 60)
    )

    plt.figure(figsize=(12, 5))

    monthly.plot()

    plt.title("Listening Activity by Month")
    plt.ylabel("Hours Listened")

    plt.tight_layout()
    plt.savefig("../plots/monthly_activity.png")
    plt.close()


def listening_by_hour(df):

    hourly = (
        df.groupby(df["ts"].dt.hour)
        ["ms_played"]
        .sum()
        / (1000 * 60 * 60)
    )

    plt.figure(figsize=(10, 5))

    hourly.plot(kind="bar")

    plt.title("Listening Activity by Hour")
    plt.xlabel("Hour")
    plt.ylabel("Hours Listened")

    plt.tight_layout()
    plt.savefig("../plots/listening_hours.png")
    plt.close()


if __name__ == "__main__":

    df = pd.read_csv("../data/spotify_history.csv")

    df["ts"] = pd.to_datetime(df["ts"])

    top_artists_chart(df)
    monthly_activity_chart(df)
    listening_by_hour(df)
