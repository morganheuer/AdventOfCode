from pathlib import Path
import time

# Define scoring breakdown
HAND = {
    "ROCK": "A",
    "PAPER": "B",
    "SCISSORS": "C"
}

REQUIRED = {
    "LOSE": "X",
    "DRAW": "Y",
    "WIN": "Z"
}

SCORES = {
    HAND["ROCK"]: 1,
    HAND["PAPER"]: 2,
    HAND["SCISSORS"]: 3,
    "LOSE": 0,
    "DRAW": 3,
    "WIN": 6
}

RULES = {
    # (Their hand, my hand)
    (HAND["ROCK"], HAND["SCISSORS"]): SCORES["LOSE"],
    (HAND["ROCK"], HAND["ROCK"]): SCORES["DRAW"],
    (HAND["ROCK"], HAND["PAPER"]): SCORES["WIN"],
    (HAND["PAPER"], HAND["ROCK"]): SCORES["LOSE"],
    (HAND["PAPER"], HAND["PAPER"]): SCORES["DRAW"],
    (HAND["PAPER"], HAND["SCISSORS"]): SCORES["WIN"],
    (HAND["SCISSORS"], HAND["PAPER"]): SCORES["LOSE"],
    (HAND["SCISSORS"], HAND["SCISSORS"]): SCORES["DRAW"],
    (HAND["SCISSORS"], HAND["ROCK"]): SCORES["WIN"],

    # (Their hand, my goal): score-for-my-hand
    (HAND["ROCK"], REQUIRED["LOSE"]): SCORES[HAND["SCISSORS"]],
    (HAND["ROCK"], REQUIRED["DRAW"]): SCORES[HAND["ROCK"]],
    (HAND["ROCK"], REQUIRED["WIN"]): SCORES[HAND["PAPER"]],
    (HAND["PAPER"], REQUIRED["LOSE"]): SCORES[HAND["ROCK"]],
    (HAND["PAPER"], REQUIRED["DRAW"]): SCORES[HAND["PAPER"]],
    (HAND["PAPER"], REQUIRED["WIN"]): SCORES[HAND["SCISSORS"]],
    (HAND["SCISSORS"], REQUIRED["LOSE"]): SCORES[HAND["PAPER"]],
    (HAND["SCISSORS"], REQUIRED["DRAW"]): SCORES[HAND["SCISSORS"]],
    (HAND["SCISSORS"], REQUIRED["WIN"]): SCORES[HAND["ROCK"]] 
}

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input_files/day02.txt")

def main():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()
    
    rounds = play_rounds(data)
    # scores = play_part_1(rounds)
    scores = play_part_2(rounds)

    print(f"Your score = {sum(scores)}")


def play_rounds(data: list[str]) -> list:
    """ Returns a list. Each element in the list is a pair as a list, e.g. ["A", "X"] """
    rounds = []
    for this_round in data:
        rounds.append(this_round.split())
    return rounds

def play_part_1(rounds: list):
    """ Here we treat X, Y, Z as whether we play Rock, Paper, Scissors, respectively. 
    Calculate our score for each hand based on what hand we play, and whether we win, lose or draw. """
    scores = []
    xyz_to_rps = {"X": HAND["ROCK"], "Y": HAND["PAPER"], "Z": HAND["SCISSORS"]}

    for this_round in rounds:
        their_hand, my_hand = this_round
        my_hand = xyz_to_rps[my_hand]

        this_score = 0
        this_score += SCORES[my_hand]
        this_score += RULES[(their_hand, my_hand)]
        scores.append(this_score)

    return scores

def play_part_2(rounds: list):
    """ Here we treat X, Y, Z as whether we play Lose, Draw, or Win, respectively. 
    Determine what hand we should play to achieve that outcome.
    Then calculate our score for each hand based on what hand we chose, and whether we win, lose or draw. """
    scores = []
    xyz_to_ldw = {"X": SCORES["LOSE"], "Y": SCORES["DRAW"], "Z": SCORES["WIN"]}
    
    for this_round in rounds:
        their_hand, my_goal = this_round
        this_score = 0
        this_score += xyz_to_ldw[my_goal]
        this_score += RULES[(their_hand, my_goal)]
        scores.append(this_score)
    
    return scores


if __name__ == "__main__":
    main()