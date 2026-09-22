import random
import time

def print_line():
    print("-" * 40)

def simulate_hit(player_name):
    hits = random.randint(1, 3)
    print(f"{player_name} bites the bottle with a pen {hits} times!")
    return hits

def play_game(rounds=5):
    print("🎮 Welcome to the Bottle Bite Game!")
    print_line()
    
    player1_score = 0
    player2_score = 0
    
    for round_num in range(1, rounds + 1):
        print(f"\n🔁 Round {round_num}")
        print_line()
        
        input("Player 1's turn! Press Enter to hit...")
        p1_hits = simulate_hit("Player 1")
        player1_score += p1_hits
        time.sleep(1)
        
        input("Player 2's turn! Press Enter to hit...")
        p2_hits = simulate_hit("Player 2")
        player2_score += p2_hits
        time.sleep(1)
        
        print_line()
        print(f"Current Score -> Player 1: {player1_score} | Player 2: {player2_score}")
        print_line()
        time.sleep(1)

    print("\n🏁 Final Scores:")
    print(f"Player 1: {player1_score}")
    print(f"Player 2: {player2_score}")
    
    if player1_score > player2_score:
        print("🎉 Player 1 wins!")
    elif player2_score > player1_score:
        print("🎉 Player 2 wins!")
    else:
        print("🤝 It's a tie!")

if __name__ == "__main__":
    play_game()
