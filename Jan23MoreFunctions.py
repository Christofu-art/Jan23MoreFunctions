#function definition
def surfacearea(r):
    return 4*3.14*r*r
result = surfacearea(12) #function call
print("The surface area of a sphere given its radius is: ", result)

def ChangeChecker(number):
    #if number is divisible by 5 with no remainder
    if number%5==0:
        print("No pennies needed")
    else:
        print( "Pennies needed")
    
ChangeChecker(25) #call function NOT in a print statement

#function defintion
def isPrime(num):
    Prime = true
for i in range(2, num):
    print(i, end = " ") #prints 2-num
    if num%i==0:
        print ("is not prime")
return Prime
result = isPrime(16) #function call