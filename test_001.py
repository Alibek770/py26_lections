import pytest

def oper(a,b):
    return a / b

'----------------------------- 1 вариант ----------------------'
# так писать плохо
@pytest.mark.skip(reason = 'не завершен') # пропускает тест-функциию
def test_oper():
    assert oper (10, 5) == 2
    assert oper (20, 5 ) == 4
    assert oper (10, 2 ) == 5
    assert oper (0, 1) == 0

'----------------------------- 2 вариант ----------------------'
# так писать плохо

def test_oper_5():
    assert oper(10,5) == 2

def test_oper_5():
    assert oper(20,5) == 4

def test_oper_5():
    assert oper(10,2) == 5

def test_oper_5():
    assert oper(0,1) == 0

'----------------------------- 3 вариант ----------------------'
#отличный вариант

import pytest

@pytest.mark.parametrize('num1, num2, result', [(10,5,2),
                                                (20,5,4),
                                                (10,2,5),
                                                (0,1,0)])
def test_oper_2(num1, num2, result):
    assert oper(num1, num2) == result

'------------------------ Обработка исключений ----------------------'
#плохой способ
def test_oper_zero():
    with pytest.raises(ZeroDivisionError):
      oper(10/0)


def test_oper_str():
    with pytest.raises(TypeError):
        oper(10,'str') 

#хороший способ
@pytest.mark.parametrize('a, b, error', [(10, 'str', TypeError),
                                            (10,0, ZeroDivisionError)])
def test_oper_error(a,b, error):
    with pytest.raises(error):
        oper(a,b)