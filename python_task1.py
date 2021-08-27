import random

run_list= [1,2,3,4,5,6]
no_of_overs = int(input("Enter the number of overs you want to play :"))
player_runs= 0
comp_runs = no_of_overs*(random.randint(1,36))
print (f"Computer has scored {comp_runs}\nYou need {comp_runs+1} to win")
no_ball=0

while no_ball < no_of_overs*6 and player_runs <= comp_runs:
    runs= int(input("Enter Runs for Your Batting Turn : "))
    comp_bowl= random.choice(run_list)
    if runs==comp_bowl:
        print (f"Your Choice: {runs},Computer's Choice: {comp_bowl}")
        print (f"\nSorry You Are OUT !!! \nYour Total Runs : {player_runs}")
        break
    elif runs>6:
        print ("ALERT!! You Can Score max 6 in a Single Ball\n")
        continue
    else:
        player_runs= player_runs+runs
        print (f"Your Choice : {runs}\nComputer's Choice : {comp_bowl}")
        print (f"Your runs Now are: {player_runs}")  
        no_ball= no_ball + 1   
        
# Result 
print("\n|______________GAME OVER______________|\n")
if player_runs > comp_runs:
    print("Congrats !!! You have won the game")
elif player_runs == comp_runs:
    print("Its a TIE !!! You have to share the win with Computer")
else:
    print("Sorry You LOST the Match")
