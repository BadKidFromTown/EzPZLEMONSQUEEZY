#Recursive Fuctions: Defined in terms of itself
#Base Case: Single stable value of return or result.
#Fib(1) = 1.

class Fibonacci:
    def __init__(self):
        self.fib_1 = 1
        self.fib_2 = 1
    

    def fibonacci_f(self, n_series):
        if(n_series == 1 or n_series == 2):
            return 1
        else:
            return self.fibonacci_f(n_series - 1) + self.fibonacci_f(n_series-2)



class Factorial_Class:
    def factorial_f(self, n_series):
        if(n_series == 1 ):
            return 1
        else:
            return self.factorial_f(n_series) * self.factorial_f(n_series - 1)