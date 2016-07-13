

def rank_to_str(rank):
    trans = {
        "ace":   "A",
        "two":   "2",
        "three": "3",
        "four":  "4",
        "five":  "5",
        "six":   "6",
        "seven": "7",
        "eight": "8",
        "nine":  "9",
        "ten":   "10",
        "jack":  "J",
        "queen": "Q",
        "king":  "K"
        }

    return trans[rank]

def rank_to_score(rank):
    trans = {
        "ace":   1,
        "two":   2,
        "three": 3,
        "four":  4,
        "five":  5,
        "six":   6,
        "seven": 7,
        "eight": 8,
        "nine":  9,
        "ten":   10,
        "jack":  10,
        "queen": 10,
        "king":  10
        }

    return trans[rank]
    
def suit_to_str(suit):
    trans = {
        "hearts":   u"\u2665",
        "diamonds": u"\u2666",
        "spades":   u"\u2660",
        "clubs":    u"\u2663"
        }

    return trans[suit]
