class NumberTools:
    
    @staticmethod
    def find_factorial(n):
        product = 1
        for num in range(1, n + 1):
            product *= num
        return product

    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        for divider in range(2, int(n ** 0.5) + 1):
            if n % divider == 0:
                return False
        return True

    @staticmethod
    def show_results(n):
        fact = NumberTools.find_factorial(n)
        prime_status = NumberTools.is_prime(n)

        print(f"Factorial of {n} is {fact}")
        if prime_status:
            print(f"{n} is a prime number.")
        else:
            print(f"{n} is not a prime number.")

NumberTools.show_results(10)