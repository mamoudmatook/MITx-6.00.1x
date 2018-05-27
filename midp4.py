def max_val(t):
    ma=0
    for i in t:

        if isinstance(i,(list,tuple)):
                l=max(i)
                if l>=ma:
                    ma=l
                
            
            
        else:
            if i>=ma:
                ma=i
                
    return ma



t=[[1,5,3],[4,5,6],7]
print(max_val(t))
