import random
import time

chords = ['Am', 'E', 'Em', 'C', 'G']
for i in range(5):
    print(random.choice(chords))
    time.sleep(3)