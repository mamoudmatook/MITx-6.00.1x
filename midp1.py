def closest_power(base, num):
    if num==1:
        return 0
    if base>num:
        return 0
    result=1
    result2=1
    

    ex=1
    while True:    
        result=base**ex
        result2=base**(ex+1)
        if abs(result-num) <= abs(result2-num):
            break
        else:
            ex=ex+1
    return ex

