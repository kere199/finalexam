def Solution(s):
    length = len(s)
    
    if length % 2 == 0:
        myindex = length // 2 - 1  
        return s[myindex:myindex+2]
    else:
        myindex = length // 2
        return s[myindex]

print(Solution("test"))

print(Solution("testing"))


    

  