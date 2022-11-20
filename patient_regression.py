
def FR_score(v1, v3, AST, ALT, PLT):
    score = 0.0118 * v1 + 0.0837 * v3 + 0.0059 * AST + (-0.0016 * ALT) + (-0.0024 * PLT) + 1.5850
        
    return score