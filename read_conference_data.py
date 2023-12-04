import csv
import pandas as pd
import copy as copy

SHORTNAME_TO_LONGNAME_TEAM = {
    'LSU': 'Louisiana State',
    'Ole Miss': 'Mississippi',
}

def read_conference_data():
    confences_with_divisions = set(["Big Ten", "SEC", "MAC", "Sun Belt"])

    raw_data = pd.read_csv('data/2023-conference-data.csv')
    raw_data = raw_data.replace({"School": SHORTNAME_TO_LONGNAME_TEAM})
    conference_data = {k: v for k, v in raw_data[["School", "Conf", "Pct.1", "SRS"]].groupby('Conf')}

    # iterate through the conferences and merge conferences if they match the confences_with_divisions set
    for conference in copy.copy(conference_data):
        for conf in confences_with_divisions:
            if conf in conference:
                temp_conf = conference_data[conference]
                del conference_data[conference]
                if conf in conference_data:
                    conference_data[conf] = pd.concat([conference_data[conf], temp_conf])
                else:
                    conference_data[conf] = temp_conf


    # for each conference, sort the teams by their winning pct and srs
    for conference in conference_data:
        conference_data[conference] = conference_data[conference].sort_values(by=['Pct.1', 'SRS'], ascending=False)
        conference_data[conference] = conference_data[conference].reset_index(drop=True)

        # add a column for the conference ranking
        conference_data[conference]['Rank'] = conference_data[conference].index + 1

    return conference_data