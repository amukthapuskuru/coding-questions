def duplicateStrings(num:int,string:str) -> str:
    l=[]
    s=[]
    for i in string:
        for j in range(len(i)):
            if i[j] not in l:
                l+=i[j]
        s.append(l)

    return s




print(duplicateStrings('4',['hi','across','beeeater','bookkeeper']))