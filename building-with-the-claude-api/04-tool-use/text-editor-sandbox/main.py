def greet(name):
    return f"Hello, {name}!"


def add(a, b):
    return a + b


def calculate_pi_5_digits():
    """
    Calculate pi to the 5th decimal digit using the Machin formula.
    Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    Returns pi rounded to 5 decimal places: 3.14159
    """
    from decimal import Decimal, getcontext
    
    # Set precision high enough to calculate pi to 5 decimal places
    getcontext().prec = 50
    
    def arctan(x, num_terms=100):
        """Calculate arctan(x) using Taylor series"""
        x = Decimal(x)
        power = x
        result = power
        for n in range(1, num_terms):
            power *= -x * x
            result += power / (2 * n + 1)
        return result
    
    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi = 4 * (4 * arctan(Decimal(1) / Decimal(5)) - arctan(Decimal(1) / Decimal(239)))
    
    # Round to 5 decimal places
    return round(float(pi), 5)


if __name__ == "__main__":
    print(greet("world"))
    print(add(2, 3))
