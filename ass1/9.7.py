import random
suits=['diamonds','hearts','spade','clubs']
ranks=['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']
deck=[f"{rank} of {suit}" for suit in suits for rank in ranks]
card=random.choice(deck)
print(card)