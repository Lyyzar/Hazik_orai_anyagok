from prim_palindrom import is_palindrom, is_prime, palin_prim


def test_is_palindrom():
    assert is_palindrom(123321) == True
    assert is_palindrom(3246) == False
    assert is_palindrom(1) == True
    assert is_palindrom(12) == False


def test_is_prime():
    assert is_prime(0) == False
    assert is_prime(3) == True
    assert is_prime(11) == True
    assert is_prime(139) == True
    assert is_prime(100) == False
    assert is_prime(66) == False


def test_palin_prim():
    assert palin_prim(0) == 2
    assert palin_prim(31) == 101
    assert palin_prim(130) == 131
    assert palin_prim(131) == 131
    assert palin_prim(1977) == 10301
