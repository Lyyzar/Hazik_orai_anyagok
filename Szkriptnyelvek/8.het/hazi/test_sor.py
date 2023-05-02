from sor import Sor


def test_sor():
    testsor = Sor()
    assert testsor.ures() == True
    testsor.betesz(3)
    assert testsor.sor == [3]
    testsor.betesz(1)
    assert testsor.sor == [3, 1]
    assert testsor.meret() == 2
    x = testsor.kivesz()
    assert x == 3
    assert testsor.sor == [1]
    assert testsor.ures() == False
    y = testsor.kivesz()
    assert y == 1
    assert testsor.ures() == True
    z=testsor.kivesz()
    assert z == None
