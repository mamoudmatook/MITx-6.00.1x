def general_poly (L):
    def applied(x):
        result=0
        for i in rang(0,len(L)):
            power=len(L)-1-i
            result=result+L[i]*(x**power)
        return result
    return applied
