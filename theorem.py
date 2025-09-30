def find_roots(a, b, c):

    discriminant = b * b - 4 * a * c
    
    if discriminant < 0:
        print("Нет действительных корней")
        return  None, None
    
    root1 = (-b + discriminant ** 0.5) / 2 * a
    root2 = (-b - discriminant ** 0.5) / 2 * a
    
    return root1, root2

def check_theorem(a, b, c):
    roots = find_roots(a, b, c)
    
    if roots == None:
        return False
    
    root1, root2 = roots
    
    actual_sum = root1 + root2
    actual_product = root1 * root2
    
    expected_sum = b / a
    expected_product = c / a
    
    sum_correct = abs(actual_sum - expected_sum) < 0.001
    product_correct = abs(actual_product - expected_product) < 0.001
    
    print(f"Уравнение: {a}x² + {b}x + {c} = 0")
    print(f"Корни: {root1:.2f} и {root2:.2f}")
    print(f"Сумма корней: {actual_sum:.2f}")
    print(f"По теореме должно быть: {expected_sum:.2f}")
    print(f"Произведение корней: {actual_product:.2f}") 
    print(f"По теореме должно быть: {expected_product:.2f}")
    
    if sum_correct and product_correct:
        return 1
    else:
        return 0

if __name__ == "__main__":
    result = check_theorem(1, -5, 6)
    print("Теорема выполняется:", bool(result))