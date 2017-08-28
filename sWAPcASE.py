def swap_case(s):
    atr=''
    for i in s:
        if i.isupper() == True:
            atr+=(i.lower())
        else:
            atr+=(i.upper())             
    return atr
