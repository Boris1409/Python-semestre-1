"""Escriba en Python una funci ́on recursiva con el siguiente encabezado:

deff ib(i) : ...

que reciba un n umero entero i y entregue el i- ́esimo t ́ermino de esta sucesi   on."""


# SE CREA UNA FUNCION EN LA CUAL EL METODO DE FIBONACCI, SUMARA LOS DOS ULTIMOS NUMEROS DENTRO DE UN ARREGLO
def fibonacci(i):
    if i == 1 or i == 2:
        return 1
    else:
        return fibonacci(i - 1) + fibonacci(i - 2)

# RESULTADOS
print("fib(1):", fibonacci(1))
print("fib(2):", fibonacci(2))
print("fib(3):", fibonacci(3))
print("fib(4):", fibonacci(4))
print("fib(5):", fibonacci(5))
print("fib(6):", fibonacci(6))
print("fib(7):", fibonacci(7))