import numpy as np
import matplotlib.pyplot as plt
from read_conference_data import *
from read_schedule_data import *
import re
import pprint

# def victory_multiplier(team_1_rank, team_2_rank):
#     return 1

def victory_multiplier(team_1_rank, team_2_rank):
    return 1 + ((team_1_rank) - team_2_rank) / max(team_1_rank, team_2_rank)

# def victory_multiplier(team_1_rank, team_2_rank):
#     return 1 + ((team_1_rank) - team_2_rank) / 14

# read the conference data
conference_data = read_conference_data()

matchups = read_schedule_data()

score_results = {}

# for each matchup, find the conference of each team, and add an entry for the conference matchup column
for i in range(len(matchups)):
    winning_team = matchups.iloc[i]['Winner']
    losing_team = matchups.iloc[i]['Loser']

    # regex to strip away '(x)' from the beginning of the team name
    winning_team = re.sub(r'^\(\d+\)\s', '', winning_team)
    losing_team = re.sub(r'^\(\d+\)\s', '', losing_team)

    winning_conference = None
    losing_conference = None
    winning_ranking = None
    losing_ranking = None
    for conference in conference_data:
        if winning_team in conference_data[conference]['School'].values:
            winning_conference = conference
            winning_ranking = conference_data[conference][conference_data[conference]['School'] == winning_team].iloc[0]['Rank']
        if losing_team in conference_data[conference]['School'].values:
            losing_conference = conference
            losing_ranking = conference_data[conference][conference_data[conference]['School'] == losing_team].iloc[0]['Rank']

    matchups.at[i, 'Winning Conference'] = winning_conference
    matchups.at[i, 'Losing Conference'] = losing_conference
    matchups.at[i, 'Winning Conference Ranking'] = winning_ranking
    matchups.at[i, 'Losing Conference Ranking'] = losing_ranking

matchups.dropna(inplace=True)

# update score results using the victory multiplier function
for i in range(len(matchups)):
    winning_conference = matchups.iloc[i]['Winning Conference']
    losing_conference = matchups.iloc[i]['Losing Conference']
    winning_ranking = matchups.iloc[i]['Winning Conference Ranking']
    losing_ranking = matchups.iloc[i]['Losing Conference Ranking']

    matchup = sorted(set([winning_conference, losing_conference]))
    if matchup[0] == matchup[-1]:
        continue

    matchup_string = matchup[0] + '-' + matchup[1]

    if matchup_string not in score_results:
        score_results[matchup_string] = "0-0"

    # parse the previous score matchup from the score results string
    score_matchup = score_results[matchup_string].split('-')
    index = matchup.index(winning_conference)

    victory_score = victory_multiplier(winning_ranking, losing_ranking)

    score_matchup[index] = "{:.3f}".format(float(score_matchup[index]) + victory_score)

    score_results[matchup_string] = score_matchup[0] + '-' + score_matchup[-1]

pprint.pprint(score_results)
