# %% Parte A
def net_gain(volumen, inicial_price, final_price):
    """
    Calcular la ganancia de la venta de los items.
   
    Parameters
    ----------
    volumen : float
        Almacena la cantidad items comprados.
    inicial_price : float
        Almacena el valor inicial de los items comprados.
    final_price : float
        Almacena el valor final de los items comprados.

    Returns
    -------
    stonks : float
        Calcula la ganancias de vender los items a un precio
        distinto al de compra.

    """
    stonks = (volumen) * (final_price - inicial_price)
    return stonks
print('Mis ganancias fueron de',net_gain(12095.2, 0.86, 1.28),'GRO')

# %% Parte B
def net_gain(volumen, inicial_price, final_price, cost):
    """
    Calcular cuantos items tienen que ser vendido para pagar el coste
    del libro y la deuda.
    
    Parameters
    ----------
    volumen : float
         Almacena la cantidad de items comprados.
    inicial_price : float
         Almacena el valor inicial de los items comprados.
    final_price : float
         Almacena el valor final de los items comprados.
    cost : float
        Almacena el valor en GRO del libro.
    -------
    products_for_book : float
        Calcula la cantidad de items que tienen que ser vendido para
        pagar el libro.
    products_for_debt : float
        Calcula la cantidad de items que tienen que ser vendido para 
        pagar la deuda.
    total_products : float
        Suma la cantidad de items que tienen que ser vendidos para
        pagar la deuda y el libro.

    """
    products_for_book = cost / final_price
    products_for_debt = (volumen * inicial_price) / final_price
    total_products = products_for_book + products_for_debt
    print('Tiene que vender', products_for_book, 'items para pagar el libro')
    print('Tiene que vender', products_for_debt, 'items para pagar la deuda')
    print('En total nos da', total_products, 'items a vender')
net_gain(12095.2, 0.86, 1.28, 2831.97)