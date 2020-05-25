from src.mathEx import stat2Num
from src.mathCy import stat2NumCy


class Test_stat2Num(object):
    """ Test class for stat2Num """

    def test_stat2Num_inputInt(self):
        """ Test with integer inputs """
        assert stat2Num(3, 2) == (5, 2.5)
        assert stat2Num(3, 2) == (5.0, 2.5)

    def test_stat2Num_inputFloat(self):
        """ Test with float inputs """
        assert stat2Num(3.5, 2.5) == (6, 3)
        assert stat2Num(3.5, 2.5) == (6.0, 3.0)


class Test_stat2NumCy(object):
    """ Test class for stat2NumCy """

    def test_stat2Num_inputInt(self):
        """ Test with integer inputs """
        assert stat2NumCy(3, 2) == (5, 2.5)
        assert stat2NumCy(3, 2) == (5.0, 2.5)

    def test_stat2Num_inputFloat(self):
        """ Test with float inputs """
        assert stat2Num(3.5, 2.5) == (6, 3)
        assert stat2Num(3.5, 2.5) == (6.0, 3.0)
