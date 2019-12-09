"""
Quiz program för att gissa portar!

"""

import random

PORT = 0
TECH = 1

facit = [
    ('22', 'SSH'),
    ('20', 'FTP'),
    ('21', 'FTP'),

]

QUESTION = random.randint(0, len(facit)-1)
print("What is the port for:", facit[QUESTION][TECH])




