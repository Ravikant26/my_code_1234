import pytest


class TestClass2:
    @pytest.mark.regression
    @pytest.mark.math
    def test_sum003(self):
        a = 10
        b = 20
        sum = a + b
        print("sum of a +b is-->" + str(sum))
        if sum == 30:
            assert True
        else:
            assert False

    @pytest.mark.math
    def test_sub004(self):
        a = 10
        b = 5
        sub = a - b
        print("sub of a - b is-->" + str(sub))
        if sub == 5:
            assert True
        else:
            assert False


