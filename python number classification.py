### PYTHON PROJECT ###
### NUMBER CLASSIFICATION PROGRAM ###
### MADE BY - JAGDISH KAUR AND KHUSHMANDEEP KAUR DHALIWAL ###

###### Classify as even and odd number ######
def even_odd(num):
    if num % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")

###### Classify as prime and composite number ######
def prime_composite(num):
    if num == 1:
        print("This is neither prime nor composite number")
        return
    
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            print("This is a composite number")
            return
        else:
            print("This is a prime number")
            return

###### Classify as perfect,deficient and abundant number ######
def perfect_deficient_abundant(num):
    if num <= 0:
        print("This number is not applicable")
        
    sum_of_divisors = 0
    for i in range(1,num):
        if num % i == 0:
            sum_of_divisors += i
            
    if sum_of_divisors == num:
        print("This is a perfect number")
    elif sum_of_divisors < num:
        print("This is a deficient number")
    else:
        print("This is an abundant number")

### MAIN FUNCTION ###
def main():
    while True:
        print("------ Number Classification Program ------")
        try:
            num = int(input("Enter an integer: "))

            # Calling functions
            even_or_odd = even_odd(num)
            prime_or_composite = prime_composite(num)
            perfect_or_deficient_or_abundant = perfect_deficient_abundant(num)

        except ValueError:
            print("Invalid input! Please enter a valid integer.")

        ### Ask user if they want to repeat ###
        choice = input("Do you want to check another number? (yes/no): ")
        if choice not in ("yes", "y"):
            print("Thank you for using the Number Classification Program!")
            break

### Run the project ###
if __name__ == "__main__":
    main()



