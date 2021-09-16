def findPrimeNumbers(lower, upper):
    for num in range(lower, upper+1):
        if num>1:
            for i in range(2, num):
                if(num%i==0):
                    break
            else:
                print(num)

if __name__ == "__main__":
    lower = int(input("Enter the lowerbound of limit: "))
    upper = int(input("enter the upperbound of the limit: "))

    print(f"The prime numbers between the limit {lower}:{upper} are: ")
    findPrimeNumbers(lower,upper)