import theorem

def test_theorem():
    print("Тестируем теорему ...")

    success1 = theorem.check_theorem(1, -5, 6)
    print("Тест 1 пройден:", bool(success1))

    success2 = theorem.check_theorem(1, 2, -3)
    print("Тест 2 пройден:", bool(success2))

    success3 = theorem.check_theorem(2, -8, 6)
    print("Тест 3 пройден:", bool(success3))

    success4 = theorem.check_theorem(2, -5, 2)
    print("Тест 4 пройден:", bool(success4))

    all_passed = success1 == 1 and success2 == 1 and success3 == 1 and success4 == 1
    return all_passed

if __name__ == "__main__":
    all_passed = test_theorem()
    print("Все тесты пройдены:", all_passed)