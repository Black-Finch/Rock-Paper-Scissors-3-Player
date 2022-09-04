moves = ("rock", "paper", "scissors")

p1_point = 0
p2_point = 0
p3_point = 0

round = 1
win = 0

while True:

    print("-" * 20)
    print("Round", round)
    print("-" * 10)
    print("Player 1 points:", p1_point)
    print("Player 2 points:", p2_point)
    print("Player 3 points:", p3_point)
    print("-" * 20)

    p1_move = input("(Player 1): Enter rock, paper or scissors: ")
    p2_move = input("(Player 2): Enter rock, paper or scissors: ")
    p3_move = input("(Player 3): Enter rock, paper or scissors: ")

    if (p1_move == p2_move and p2_move == p3_move) or (p1_move != p2_move and p1_move != p3_move and p2_move != p3_move):
        p1_point += 1
        p2_point += 1
        p3_point += 1

    elif p1_move == p2_move and p1_move == moves[0]:
        if p3_move == moves[1]:
            p3_point += 1
        elif p3_move == moves[2]:
            p1_point += 1
            p2_point += 1
    elif p1_move == p2_move and p1_move == moves[1]:
        if p3_move == moves[0]:
            p1_point += 1
            p2_point += 1
        elif p3_move == moves[2]:
            p3_point += 1
    elif p1_move == p2_move and p1_move == moves[2]:
        if p3_move == moves[0]:
            p3_point += 1
        elif p3_move == moves[1]:
            p1_point += 1
            p2_point += 1

    elif p1_move == p3_move and p1_move == moves[0]:
        if p2_move == moves[1]:
            p2_point += 1
        elif p2_move == moves[2]:
            p1_point += 1
            p3_point += 1
    elif p1_move == p3_move and p1_move == moves[1]:
        if p2_move == moves[0]:
            p1_point += 1
            p3_point += 1
        elif p2_move == moves[2]:
            p2_point += 1
    elif p1_move == p3_move and p1_move == moves[2]:
        if p2_move == moves[0]:
            p2_point += 1
        elif p2_move == moves[1]:
            p1_point += 1
            p3_point += 1

    elif p2_move == p3_move and p2_move == moves[0]:
        if p1_move == moves[1]:
            p1_point += 1
        elif p1_move == moves[2]:
            p2_point += 1
            p3_point += 1
    elif p2_move == p3_move and p2_move == moves[1]:
        if p1_move == moves[0]:
            p2_point += 1
            p3_point += 1
        elif p1_move == moves[2]:
            p1_point += 1
    elif p2_move == p3_move and p2_move == moves[2]:
        if p1_move == moves[0]:
            p1_point += 1
        elif p1_move == moves[1]:
            p2_point += 1
            p3_point += 1

    if round >= 3 and not(p1_point == p2_point and p2_point == p3_point):
        mx = max(p1_point, p2_point, p3_point)
        if mx == p1_point:
            if mx != p2_point and mx != p3_point:
                win = 1
        elif mx == p2_point:
            if mx != p1_point and mx != p3_point:
                win = 2
        elif mx == p3_point:
            if mx != p1_point and mx != p2_point:
                win = 3

    if win:
        print("-" * 20)
        print("Player 1 points:", p1_point)
        print("Player 2 points:", p2_point)
        print("Player 3 points:", p3_point)
        print("-" * 20)
        print("Player", win, "is the winner!")
        break

    round += 1
