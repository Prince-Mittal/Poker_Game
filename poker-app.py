import Poker
from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def welcome():
    cards = ['AH', 'KH', 'QH', 'JH', '10H', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H',
            'AD', 'KD', 'QD', 'JD', '10D', '9D', '8D', '7D', '6D', '5D', '4D', '3D', '2D',
            'AS', 'KS', 'QS', 'JS', '10S', '9S', '8S', '7S', '6S', '5S', '4S', '3S', '2S',
            'AC', 'KC', 'QC', 'JC', '10C', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C']
    user1_card = []
    user2_card = []
    random.shuffle(cards)
    for i in range(0,5):
        user1_card.append(cards[i])
    for i in range(5,10):
        user2_card.append(cards[i])
    output=Poker.check(user1_card,user2_card)
    return render_template("index.html", cards1=user1_card, cards2=user2_card,winner=output)


if __name__ == '__main__':
    print(app.config)
    app.config['DEBUG'] = True
    app.run()