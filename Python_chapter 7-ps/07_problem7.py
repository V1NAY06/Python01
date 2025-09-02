'''
for n = 3
  *
 ***
*****

For n = 5
    *
   ***
  *****
 ********
**********

'''


n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "* (n-i))
    print("*"* i, end="")
    print("*"* (2*i-1), end="")
    print("")