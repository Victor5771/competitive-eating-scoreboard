def calculate_score(participant):
    """
    Calculate the score for a participant based on the points for each food.
    """
    return participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2

def generate_scoreboard(participants):
    """
    Generate the scoreboard sorted by score, with ties broken alphabetically by name.
    """
    scoreboard = []
    for participant in participants:
        scoreboard.append({'name': participant['name'], 'score': calculate_score(participant)})
    
    
    scoreboard.sort(key=lambda x: (-x['score'], x['name']))
    return scoreboard


participants = [
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]

# print the scoreboard
scoreboard = generate_scoreboard(participants)
print(scoreboard)