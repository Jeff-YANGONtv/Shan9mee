from flask import Flask, jsonify, request
import random

app = Flask(__name__)

def get_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return [{"suit": s, "rank": r} for s in suits for r in ranks]

def calculate_score(hand):
    score = 0
    for card in hand:
        r = card['rank']
        if r in ['10', 'J', 'Q', 'K']: score += 0
        elif r == 'A': score += 1
        else: score += int(r)
    return score % 10

@app.route('/api/play', methods=['POST'])
def play():
    deck = get_deck()
    random.shuffle(deck)
    
    player_hand = [deck.pop(), deck.pop()]
    bot_hand = [deck.pop(), deck.pop()]
    
    # Simple Bot AI: ၅ မှတ်အောက်ဆို နောက်တစ်ကတ်ဆွဲမယ်
    bot_score = calculate_score(bot_hand)
    if bot_score < 5:
        bot_hand.append(deck.pop())
        bot_score = calculate_score(bot_hand)

    return jsonify({
        "player": player_hand,
        "bot": bot_hand,
        "player_score": calculate_score(player_hand),
        "bot_score": bot_score
    })

if __name__ == "__main__":
    app.run()
