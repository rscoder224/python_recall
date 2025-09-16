

a = int(input("Enter a number :-- "))

odd = 1
even = 0
for i in range(0,a+1,1):
    if i%2 != 0:
      odd = odd + i
    elif i%2==0:
        even = even + i
        print(f"sum of odd numbers: {odd} and even numbers: {even}")
             
