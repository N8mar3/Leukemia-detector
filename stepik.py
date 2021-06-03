"""number = int(input())
string = team_memory = []
main_dict = {}
for rows in range(number):
    string.append(str(input()))
for j in range(number):
    champion, score_1, loser, score_2 = string[j].strip().split(';')
    if champion not in team_memory:
        team_memory.append(champion)
        main_dict.update({champion: [0, 0, 0, 0, 0]})
    if loser not in team_memory:
        team_memory.append(loser)
        main_dict.update({loser: [0, 0, 0, 0, 0]})
    champion_params = [team_memory.count(champion), 1, 0, 0, 3]
    loser_params = [team_memory.count(loser), 0, 0, 1, 0]
    pars_params = [team_memory.count(champion), 0, 1, 0, 1]
    if int(score_1) != int(score_2):
        if int(score_1) < int(score_2):
            champion, loser = loser, champion
        main_dict[champion] = [main_dict[champion][0] + champion_params[0],
                               main_dict[champion][1] + champion_params[1],
                               main_dict[champion][2] + champion_params[2],
                               main_dict[champion][3] + champion_params[3],
                               main_dict[champion][4] + champion_params[4]]
        main_dict[loser] = [main_dict[loser][0] + loser_params[0],
                            main_dict[loser][1] + loser_params[1],
                            main_dict[loser][2] + loser_params[2],
                            main_dict[loser][3] + loser_params[3],
                            main_dict[loser][4] + loser_params[4]]
    else:
        main_dict[champion] = [main_dict[champion][0] + pars_params[0],
                               main_dict[champion][1] + pars_params[1],
                               main_dict[champion][2] + pars_params[2],
                               main_dict[champion][3] + pars_params[3],
                               main_dict[champion][4] + pars_params[4]]
        main_dict[loser] = [main_dict[loser][0] + pars_params[0],
                            main_dict[loser][1] + pars_params[1],
                            main_dict[loser][2] + pars_params[2],
                            main_dict[loser][3] + pars_params[3],
                            main_dict[loser][4] + pars_params[4]]
for keys in main_dict:
    print(keys+':', *main_dict[keys], sep=' ')
"""
import math
n = [15, 20]


def count(n):
    vals = [('log log_2 n' , math.log(math.log(n, 2) )),
            ('sqrt log_4 n' ,math.sqrt(math.log(n, 4))),
            ('log_3 n', math.log(n, 3)),
            ('(log_2 n)^2', math.log(n, 2) ** 2),
            ('sqrt n' , math.sqrt(n)),
            ('n / log_5 n'  ,n / math.log(n, 5)),
            ('log (n!)', math.log(math.factorial(n),2)),
            ('3 ^ log_2(n)', 3 ** math.log(n, 2)),
            ('n ^2 ', n ** 2),
            ('7 ^ log_2(n) ',7 ** (math.log(n, 2))),
            ('log_2(n) ^ log_2(n) ',  math.log(n, 2) ** (math.log(n, 2))),
            ('n^ log_2 (n) ', n ** (math.log(n, 2))),
            ('n^ sqrt n ' , n ** (math.sqrt(n))),
            ('2**n ' , 2**n),
            ('4**n' , 4**n),
            ('2 ** (3 * n)' , 2 ** (3 * n)),
            ('n!' , math.factorial(n))
            ]
    return vals

# add some changes
# add some changes again
# champion: print(2 ** (2 ** n))
vals_1 = sorted(count(n[0]), key=lambda x : x[1])
vals_2 = sorted(count(n[1]), key=lambda x : x[1])
print([x[0] for x in vals_1])
print([x[0] for x in vals_2])
# print(2 ** (2 ** n))