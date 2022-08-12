import pandas as pd
import re

from pathlib import Path

csv_p = Path("../csv/")


def to_sec(dt):
    if dt is not None:
        return dt.hour * 3600 + dt.minute * 60 + dt.second


def read_csv(type, yy, mm, dd):
    if type == "GPS":
        fl = list(csv_p.glob(f"{type}_{yy:02d}-{mm:02d}-{dd:02d}_*.csv"))
    elif type == "LI7810":
        fl = list(csv_p.glob(f"{type}_{yy:02d}{mm:02d}{dd:02d}_*.csv"))
    else:
        raise ValueError("Invalid data type")

    if len(fl) != 1:
        raise ValueError("Issue with csv file setup")

    return fl[0]


def get_pq(yy, mm, dd):
    # Process GPS record
    df_gps = pd.read_csv(read_csv("GPS", yy, mm, dd))

    df_gps.time = pd.to_datetime(df_gps.time) - pd.Timedelta(hours=17)
    df_gps.time = df_gps.time.apply(to_sec)

    df_gps = df_gps[["time", "lat", "lon", "alt"]]

    # Process LI7810 record
    df_li = pd.read_csv(
        read_csv("LI7810", yy, mm, dd),
        encoding="ISO-8859-1",
        skiprows=5,
        sep="\t",
    )

    df_li = df_li.drop(0)

    df_li["time"] = df_li[["DATE", "TIME"]].agg(" ".join, axis=1)
    df_li.time = pd.to_datetime(df_li["time"]) - pd.Timedelta(seconds=34)
    df_li.time = df_li.time.apply(to_sec)
    df_li = df_li[["time", "H2O", "CO2", "CH4"]]

    return df_gps, df_li
