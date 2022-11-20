
<<<<<<< HEAD
def FR_score(v1, v3, AST, ALT, PLT):
    score = 0.0118 * v1 + 0.0837 * v3 + 0.0059 * AST + (-0.0016 * ALT) + (-0.0024 * PLT) + 1.5850
        
    return score
=======
def FR_score(v1, v2, AST, ALT, PLT):
    return (15.27 * v1 + 43.62 * v2 + 5.41 * AST) / (1.65 * ALT + 2.35 * PLT)
>>>>>>> 713d8bfb607eb35f1e452755aa80a21e3e04c108
