# Paste your function here
def dict_invert(d):
    Lvalues=list(d.values())
    inv_dict={}
    index=0
    for i in d.keys():
        if d[i] not in inv_dict:
            inv_dict[Lvalues[index]]=[]
        inv_dict[Lvalues[index]].append(i)
        index=index+1
    for i in inv_dict.keys():
         inv_dict[i]=sorted(inv_dict[i])
    return inv_dict
