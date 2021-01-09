player1 = input("Name of player 1 : ")
player2 = input("Name of player 2 : ")
print("The match will be the best of three =>")
p1_score = 0
p2_score = 0
winner = ""
c = 0
while winner == "":
    c += 1
    p1 = int(input(f'''{player1} Choose: 1 for Rock
          2 for Paper
          3 for Scissor : '''))
    p2 = int(input(f'''{player1} Choose: 1 for Rock
          2 for Paper
          3 for Scissor : '''))
    if (p1 == 1 and p2 == 3) or (p1 == 2 and p2 == 1) or (p1 == 3 and p2 == 2):
        p1_score += 1
    elif (p2 == 1 and p1 == 3) or (p2 == 2 and p1 == 1) or (p2 == 3 and p1 == 2):
        p2_score += 1
    if c == 3:
        if p1_score > p2_score:
            winner = player1
        elif p2_score > p1_score:
            winner = player2
        else:
            print("The match is draw")
print(f"Winner is {winner}")
        
    


        
        

