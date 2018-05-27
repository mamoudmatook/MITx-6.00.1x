def deep_reverse(L):
    
    L[:]=L[::-1]
    for i in range(len(L)):
        L[i]=L[i][::-1]
