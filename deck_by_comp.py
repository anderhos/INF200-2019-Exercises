SUITS = ('C', 'S', 'H', 'D')
VALUES = range(1, 14)

def deck_loop():
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck

deck_comp = [(suit,val) for suit in SUITS for val in VALUES]

if __name__ == '__main__':
    if deck_loop() != deck_comp:
        print('ERROR!')