import random
name = input("Please Enter the Playername: ")
print()
print(f"Welcome {name} to a game of ROCK, PAPER AND SCISSOR")
print()
print("Here are the Rules:-")
print(" ROCK vs PAPER; PAPER wins \n PAPER vs SCISSOR; SCISSOR wins \n ROCK vs SCISSOR; ROCK wins")
print()
print("YOU COULD QUIT THE GAME EARLY CHOSING YOUR ACTION AS QUIT")
print()
def play_round(player_action, AI_action):
    if player_action == AI_action :
        return "It's a TIE"
    elif (player_action == "ROCK" and AI_action == "SCISSOR"):
        return "You WIN!"
    elif (player_action == "PAPER" and AI_action == "ROCK"):
        return "You WIN!"
    elif (player_action == "SCISSOR" and AI_action == "PAPER"):
        return "You WIN!"
    else :
        return "You LOSE!"
max_points = int(input("MAXIMUM POINT: "))
print()
player_wins = 0
AI_wins = 0
player_action = "player action"
while player_wins < max_points and AI_wins < max_points and player_action != "QUIT": 
    options = ["ROCK", "PAPER", "SCISSOR"]
    player_action = input("PLEASE ENTER YOUR ACTION: ").upper()
    AI_action = random.choice(options)
    print()
    if player_action == "QUIT" :
        print("PLAYER QUIT THE GAME")
    else :
        while player_action not in options :
            player_action = input("PLEASE ENTER A VALID ACTION: ").upper()
            print()
        print(f"PLAYER ACTION = {player_action}")
        print(f"AI ACTION = {AI_action}")
        print()
        result = play_round(player_action, AI_action)
        print(result)
        print()
        if result == "You WIN!" :
            player_wins += 1
        elif result == "You LOSE!" :
            AI_wins += 1
        else :
            player_wins += 0
    print(f"PLAYER POINTS = {player_wins}")
    print(f"AI POINTS = {AI_wins}")
print()
if player_action == "QUIT" :
    print("NO RESULT!! Player Quit the Game")
elif player_wins > AI_wins :
    print(f"{name} WON THE GAME")
elif player_wins < AI_wins :
    print(f"{name} LOST THE GAME")
else :
    print("GAME ENDS IN DRAW")
print()
print(f"THANKS FOR PLAYING {name}")
print("SEE YOU SOON")
    
    

      
      
          
          
        
    