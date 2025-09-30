import theorem

def test_theorem():
    print("Тестируем теорему ...")

    success1 = theorem.check_theorem(1, -5, 6)
    print("Тест 1 пройден:", bool(success1))

    success2 = theorem.check_theorem(1, 2, -3)
    print("Тест 2 пройден:", bool(success2))

    success3 = theorem.check_theorem(2, -8, 6)
    print("Тест 3 пройден:", bool(success3))

    all_passed =  success1 and success2 and success3
    return all_passed == 1

if __name__ == "__main__":
    all_passed = test_theorem()
    print("Все тесты пройдены:", all_passed)