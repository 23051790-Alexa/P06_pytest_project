from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 123
        b = 234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 357
        assert result == expected

    
