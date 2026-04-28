def romano_a_decimal(romano: str) -> int:
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
 
    if len(romano) == 0:
        return 0
    if len(romano) == 1:
        return valores[romano[0]]
 
    valor_actual = valores[romano[0]]
    valor_siguiente = valores[romano[1]]
 
    if valor_actual < valor_siguiente:
        return -valor_actual + romano_a_decimal(romano[1:])
    else:
        return valor_actual + romano_a_decimal(romano[1:])