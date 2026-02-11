from flask import Flask, jsonify, request
import random

app = Flask(__name__)

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = 0 if rank in ['J', 'Q', 'K', '10'] else (1 if rank == 'A' else int(rank))

@app.route('/api/deal', methods=['GET'])
def deal():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [{"suit": s, "rank": r, "val": 0 if r in ['J', 'Q', 'K', '10'] else (1 if r == 'A' else int(r))} for s in suits for r in ranks]
    random.shuffle(deck)
    
    # Player နဲ့ Bot ကို ၂ ကတ်စီပေးမယ်
    res = {
        "player": [deck.pop(), deck.pop()],
        "bot": [deck.pop(), deck.pop()],
        "remaining_deck": deck
    }
    return jsonify(res)

if __name__ == '__main__':
    app.run()
