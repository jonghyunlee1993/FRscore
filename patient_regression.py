
def FR_score(v1, v2, AST, ALT, PLT):
    score = 1.53 * v1 + 4.36 * v2 + 0.54 * AST + \
        - 0.16 * ALT - 0.24 * PLT
        
    return score