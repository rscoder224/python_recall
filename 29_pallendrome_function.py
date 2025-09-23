
def pallendrome(st):
    rev = ""
    for i in range(len(st)-1,-1,-1):
        rev = rev + st[i]
        
    if rev == st:
         print("Pallendrome")
    else:
        print("Not a Pallendrome")
        
        
pallendrome('Shaurya')
