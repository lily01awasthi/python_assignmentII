"""8. Write a function, is_prime, that takes an integer and returns True if
the number is prime and False if the number is not prime.
"""
def check_prime(num):
    if (num > 1):
        for i in range(2, num):
            if (num % i) == 0:
                return False

        else:
            return True
    else:
        return False


inp = int(input("enter the number to check: "))
satus=check_prime(inp)
print(satus)