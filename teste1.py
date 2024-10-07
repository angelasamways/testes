def fibonacci_sequence(n):
    fib_seq = [0, 1]

    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    return fib_seq


def check_fibonacci_number(n):
    fib_seq = fibonacci_sequence(n)

    if n in fib_seq:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."


num = 11


resultado = check_fibonacci_number(num)
print(resultado)
