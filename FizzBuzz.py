#This program counts from 1 to 100 while replacing each number divisible by 3 with "fizz", replaces each number divisible by 5 with the word "buzz",
#and replaces each number divisible by both 3 and 5 with "fizzbuzz".

def main():
    #Define variables.
    num = 1
    check3 = 0
    check5 = 0

    for x in range(1, 101):                                         #For loop to execute the nested if-else loops.
        
        check3 = num / 3                                            #Divide num by 3 so we can check if the result is an integer.
        check5 = num / 5                                            #Divide num by 5 so we can check if the result is an integer.
        
        if check3.is_integer() and check5.is_integer() is True:     #This utilizes the is_integer() method to check if our check variables are integers, prints "FizzBuzz" if it returns
            print("FizzBuzz")                                       #true, and increments num by 1.
            num += 1
            
        elif check3.is_integer():                                   #This utilizes is_intereger() method to check if our check3 variable is an integer, prints "Fizz" if true,
            print("Fizz")                                           #and increments num by 1.
            num += 1
            
        elif check5.is_integer():                                   #This utilizes is_intereger() method to check if our check5 variable is an integer, prints "Buzz" if true,
            print("Buzz")                                           #and increments num by 1.
            num += 1
            
        elif num:                                                   #This catches the rest of the numbers that are not divisible by 3 or 5 and prints the associated number
            print(num)                                              #and increments num by 1.
            num += 1
            
        else:                                                       #This allows the loop to proceed if none of the above statements are satisfied.
            pass

main()
