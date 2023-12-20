"""
	Write a program to input a player's name (string) and runs (integer) scored for n number of players where n should be input from the keyboard. Store the player�s details in a dictionary called 'cricket'. After preparing the dictionary, input the player's name and print the runs scored by the player, otherwise return '-1' if the player's name is not found. 
"""

n = int(input("Enter the number of players: "))
cricket = {}

for _ in range(n):
    player_name = input("Enter player's name: ")
    runs_scored = int(input("Enter runs scored: "))
    cricket[player_name] = runs_scored

search_player = input("Enter the player's name to search: ")
runs_scored = cricket.get(search_player, -1)
print(f"Runs scored by {search_player}: {runs_scored}")
    
"""
	------- output -------
    Enter the number of players: 5     
    Enter player's name: Ravindra Jadeja
    Enter runs scored: 2000
    Enter player's name: Jasprit Bumrah
    Enter runs scored: 1522
    Enter player's name: MS Dhoni
    Enter runs scored: 2256
    Enter player's name: Rohit Sharma
    Enter runs scored: 1823
    Enter player's name: Virat Kohli
    Enter runs scored: 2280
    Enter the player's name to search: Jasprit Bumrah
    Runs scored by Jasprit Bumrah: 1522
"""