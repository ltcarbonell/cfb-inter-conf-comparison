import csv
import pandas as pd
from read_conference_data import SHORTNAME_TO_LONGNAME_TEAM


def read_schedule_data():

    filtered_data = pd.read_csv('data/2023-schedule-data.csv')[["Rk", "Winner", "Loser", "Pts", "Pts.1"]].dropna()
    filtered_data = filtered_data.replace({"School": SHORTNAME_TO_LONGNAME_TEAM})

    return filtered_data
