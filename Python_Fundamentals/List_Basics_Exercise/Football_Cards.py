cards = input().split()

sent_off_players_teamA = []
sent_off_players_teamB = []
shouldTerminate = False

for card in cards:
    if card in sent_off_players_teamA or card in sent_off_players_teamB:
        continue

    cardSplit = card.split("-")
    teamName = cardSplit[0]
    playerNum = cardSplit[1]

    if teamName == 'A':
        sent_off_players_teamA.append(card)
    elif teamName == 'B':
        sent_off_players_teamB.append(card)

    if len(sent_off_players_teamA) > 4 or len(sent_off_players_teamB) > 4:
        shouldTerminate = True
        break

playerCount = 11
print(f"Team A - {playerCount - len(sent_off_players_teamA)}; Team B - {playerCount - len(sent_off_players_teamB)}")

if shouldTerminate:
    print("Game was terminated")