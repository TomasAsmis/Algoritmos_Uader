def usar_la_fuerza(mochila: list, indice: int = 0) -> tuple:
    SABLE_DE_LUZ = "sable de luz"
 
    if indice >= len(mochila):
        return (False, indice)
 
    objeto_actual = mochila[indice]
 
    if objeto_actual.lower() == SABLE_DE_LUZ:
        return (True, indice + 1)
 
    return usar_la_fuerza(mochila, indice + 1)