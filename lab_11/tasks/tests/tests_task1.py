import pytest

from lab_11.tasks.tools.calculator import (
    Calculator,
    CalculatorError,
    EmptyMemory,
    NotNumberArgument,
    WrongOperation,
)


@pytest.fixture
def calculator():
    return Calculator()


@pytest.mark.parametrize("operator,arg1,arg2,expected",
                         [("+", 2, 3, 5),
                          ("-", 2, 5, -3),
                          ("*", 2, 3, 6),
                          ("/", 3, 2, 1.5),
                          ])
def test_run_valid_data(operator, arg1, arg2, expected, calculator):
    assert calculator.run(operator, arg1, arg2) == expected


@pytest.mark.parametrize("operate,arg1,expected",
                         [('+', 3, 6),
                          ('-', 3, 0),
                          ('/', 3, 1),
                          ('*', 3, 9),
                          ])
def test_memorize(calculator, operate, arg1, expected):
    calculator.run('+', 2, 1)
    assert calculator._short_memory == 3

    # set number 3 to memory
    calculator.memorize()
    assert calculator.memory == 3

    assert calculator.run(operate, arg1) == expected

    calculator.clean_memory()
    with pytest.raises(EmptyMemory):
        calculator.in_memory()


@pytest.mark.parametrize("operator,arg1,arg2,expected",
                         [("+", 1, "b", NotNumberArgument),
                          ("-", "a", 1, NotNumberArgument),
                          ("-", "a", "b", NotNumberArgument),
                          ("^", 1, 2, WrongOperation),
                          ("/", 1, 0, CalculatorError),
                          ("/", 2, None, EmptyMemory),
                          ])
def test_run_invalid_data(operator, arg1, arg2, expected, calculator):
    with pytest.raises(expected):
        calculator.run(operator, arg1, arg2)
