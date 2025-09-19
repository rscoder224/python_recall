
a = [1,2,3,4,5]

def targetFinder(target,list):
          for i in range(0,len(list),1):
                if list[i] == target:
                     print(f"Target is present {list[i]}")
                else:
                     print("Target is not present")
                    
                    
targetFinder(2,a)
targetFinder(0,a)
