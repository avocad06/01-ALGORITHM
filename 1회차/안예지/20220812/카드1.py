# 2161.
""" 
"""
from collections import deque
N = int(input())

cards = deque(range(1, N +1))

while len(cards) != 1:
    throw = cards.popleft()
    print(throw, end = " ")
    cards.append(cards.popleft())
    
print(*cards)
# print(queue[0])