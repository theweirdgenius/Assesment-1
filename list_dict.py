new_player1 = { 'firstName': 'LaMarcus', 'lastName': 'Aldridge', 'jersey': '12', 'heightMeters': '2.11', 'nbaDebutYear': '2006', 'weightKilograms': '117.9'}
new_player2 = { 'firstName': 'LeBron', 'lastName': 'James', 'jersey': '2', 'heightMeters': '2.03', 'nbaDebutYear': '2003', 'weightKilograms': '113.4' }
new_player3 = { 'firstName': 'Kawhi', 'lastName': 'Leonard', 'jersey': '2', 'heightMeters': '2.01', 'nbaDebutYear': '2011', 'weightKilograms': '104.3' }

nba_players = []
nba_players.append(new_player1)
nba_players.append(new_player2)
nba_players.append(new_player3)

print(nba_players)


def get_nba_debut_year(player):
    return int(player['nbaDebutYear'])
        
nba_players.sort(key = get_nba_debut_year)
print(nba_players)
