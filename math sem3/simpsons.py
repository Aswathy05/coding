import sympy as sp

def simpsons_one_third_rule(func, a, b, n):
    if n % 2 != 0:
        raise ValueError("The number of subintervals (n) must be even for Simpson's 1/3 rule.")
    
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [func.subs('x', xi) for xi in x]

    integral = y[0] + y[n]
    
    for i in range(1, n):
        if i % 2 == 0:
            integral += 2 * y[i]
        else:
            integral += 4 * y[i]
    
    integral = integral * (h / 3)
    
    return integral

# Get user input for the function to be integrated
func_str = input("Enter the function to be integrated (e.g., sin(x), log(x), exp(x)): ")

try:
    x = sp.Symbol('x')
    func = sp.sympify(func_str)
    a = float(input("Enter the lower limit of integration (a): "))
    b = float(input("Enter the upper limit of integration (b): "))
    n = int(input("Enter the number of subintervals (must be even): "))
    
    if n % 2 != 0:
        print("The number of subintervals (n) must be even for Simpson's 1/3 rule.")
    else:
        result = simpsons_one_third_rule(func, a, b, n)
        print(f"Approximate integral: {result}")
except (sp.SympifyError, ValueError):
    print("Invalid input. Please enter a valid function and numeric limits/parameters.")
