products = {
    1: 4.0,
    2: 4.5,
    3: 5.0,
    4: 2.0,
    5: 1.5
}

code, quantity = [int(item) for item in input().split()]

print(f'Total: R$ {products[code] * quantity:.2f}')