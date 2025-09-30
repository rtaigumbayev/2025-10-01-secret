import theorem

def test_theorem():
    print("Тестируем теорему ...")

    success1 = theorem.check_theorem(1, -5, 6)
    print("Тест 1 пройден:", success1)

    success2 = theorem.check_theorem(1, 2, -3)
    print("Тест 2 пройден:", success2)

    success3 = theorem.check_theorem(2, -8, 6)
    print("Тест 3 пройден:", success3)

    return success1 and success2 and success3

if __name__ == "__main__":
    all_passed = test_theorem()
    print("Все тесты пройдены:", all_passed)