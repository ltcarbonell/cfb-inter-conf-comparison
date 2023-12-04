import numpy as np
import matplotlib.pyplot as plt

def victory_multiplier(team_1_rank, team_2_rank):
    # return 1 + ((team_1_rank) - team_2_rank) / max(team_1_rank, team_2_rank)
    return 1 + ((team_1_rank) - team_2_rank) / 14

# ACC 14 x 2 matrix, with team name and conference ranking
acc = [
       ['Clemson', 6],
       ['Florida State', 1],
       ['Louisville', 2],
       ['NC State', 3],
       ['Wake Forest', 14],
       ['Syracuse', 11],
       ['Boston College', 10],
       ['Virginia Tech', 5],
       ['Miami', 9],
       ['Georgia Tech', 4],
       ['Virginia', 13],
       ['Duke', 8],
       ['North Carolina', 7],
       ['Pittsburgh', 12]
]

# Big 10 14 x 2 matrix, with team name and conference ranking
b10 = [
    ['Ohio State', 2],
    ['Penn State', 3],
    ['Michigan State', 13],
    ['Michigan', 1],
    ['Maryland', 7],
    ['Rutgers', 8],
    ['Indiana', 14],
    ['Purdue', 12],
    ['Wisconsin', 6],
    ['Iowa', 4],
    ['Northwestern', 5],
    ['Minnesota', 10],
    ['Nebraska',11 ],
    ['Illinois', 9]
]

# SEC 14 x 2 matrix, with team name and conference ranking
sec = [
    ['Alabama', 1],
    ['Auburn', 8],
    ['LSU', 4],
    ['Texas A&M', 6],
    ['Mississippi State', 12],
    ['Ole Miss', 3],
    ['Arkansas', 13],
    ['Missouri', 5],
    ['Georgia', 2],
    ['Florida',  9],
    ['South Carolina',  11],
    ['Tennessee',  7],
    ['Kentucky',  10],
    ['Vanderbilt', 14]
]

# Big 12 10 x 2 matrix, with team name and conference ranking
b12 = [
    ['Oklahoma', 0],
    ['Oklahoma State', 0],
    ['TCU', 0],
    ['Kansas State', 0],
    ['West Virginia', 0],
    ['Texas', 0],
    ['Iowa State', 0],
    ['Baylor', 0],
    ['Texas Tech', 0],
    ['Kansas', 0]
]

# Pac 12 12 x 2 matrix, with team name and conference ranking
p12 = [
    ['Washington', 0],
    ['Washington State', 0],
    ['Oregon', 0],
    ['Stanford', 0],
    ['California', 0],
    ['Oregon State', 0],
    ['USC', 0],
    ['UCLA', 0],
    ['Utah', 0],
    ['Arizona', 0],
    ['Arizona State', 0],
    ['Colorado', 0]
]

# match ups 1 x 3 matrix, with team 1, team 2, and winner
matchups = [
    ['Louisville', 'Kentucky', 'Kentucky'],
    ['Florida State', 'Florida', 'Florida State'],
    ['Clemson', 'South Carolina', 'Clemson'],
    ['Georgia Tech', 'Georgia', 'Georgia'],
    # ['Louisville', 'Indiana', 'Louisville'],
    # ['North Carolina', 'Minnesota', 'North Carolina'],
    # ['Duke', 'Northwestern', 'Duke'],
    # ['Virginia Tech', 'Rutgers', 'Rutgers'],
    ['Georgia Tech', 'Ole Miss', 'Ole Miss'],
    # ['Syracuse', 'Purdue', 'Syracuse'],
    # ['Virginia', 'Maryland', 'Maryland'],
    ['Wake Forest', 'Vanderbilt', 'Wake Forest'],
    # ['Virginia Tech', 'Purdue', 'Purdue'],
    ['Miami', 'Texas A&M', 'Miami'],
    ['Florida State', 'LSU', 'Florida State'],
    ['Virginia', 'Tennessee', 'Tennessee'],
    ['North Carolina', 'South Carolina', 'North Carolina']
]


acc_record = 0.0
b10_record = 0.0
sec_record = 0.0
# for each match up, find the winner and add a win to their conference record
for i in range(len(matchups)):
    team1 = matchups[i][0]
    team2 = matchups[i][1]
    result = matchups[i][2]

    if result == team1:
        winner = team1
        loser = team2
    if result == team2:
        winner = team2
        loser = team1


    # find the teams in the conference matrices and replace the team name with the team name and conference ranking
    for j in range(len(acc)):
        if winner == acc[j][0]:
            winner = acc[j]
        if loser == acc[j][0]:
            loser = acc[j]
    for j in range(len(b10)):
        if winner == b10[j][0]:
            winner = b10[j]
        if loser == b10[j][0]:
            loser = b10[j]
    for j in range(len(sec)):
        if winner == sec[j][0]:
            winner = sec[j]
        if loser == sec[j][0]:
            loser = sec[j]

    print('winner')
    print(winner)
    print('loser')
    print(loser)

    victory_score = victory_multiplier(winner[1], loser[1])
    print(victory_score)
    for j in range(len(acc)):
        if winner[0] == acc[j][0]:
            acc_record += victory_score
    for j in range(len(b10)):
        if winner[0] == b10[j][0]:
            b10_record += victory_score
    for j in range(len(sec)):
        if winner[0] == sec[j][0]:
            sec_record += victory_score


# print the records
print('ACC: ' + str(acc_record))
print('B10: ' + str(b10_record))
print('SEC: ' + str(sec_record))

# plot a sample graph of the victory multiplier function
# with the x axis being the difference in conference ranking
# and the y axis being the victory multiplier
a = np.linspace(1, 14, 14)
b = np.linspace(1, 14, 14)

c = np.zeros((len(a), len(b)))
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j] = victory_multiplier(a[i], b[j])
# print(c)

# plot c
plt.imshow(c, cmap='hot')

plt.xlabel('Winner Conference Ranking')
plt.ylabel('Loser Conference Ranking')
plt.title('Victory Multiplier Function')
plt.show()

# plot a sample graph of the victory multiplier function for a #1 team vs all the other matchups
# with x being the conference ranking of the other team
# and y being the victory multiplier
a = np.linspace(1, 14, 14)

c = np.zeros((len(a), 1))
for i in range(len(a)):
    c[i][0] = victory_multiplier(1, a[i])

# print(c)

# plot c
plt.plot(a, c)
plt.xlabel('Conference Ranking of Other Team')
plt.ylabel('Victory Multiplier')
plt.title('Victory Multiplier Function for #1 Team')
plt.show()