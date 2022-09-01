import math

def FR_score(v1, v2, AST, ALT, PLT):
    score = 0.0153 * v1 + 0.0436 * v2 + 0.0054 * AST + \
        - 0.0016 * ALT - 0.0024 * PLT + 1.7874
        
    return score