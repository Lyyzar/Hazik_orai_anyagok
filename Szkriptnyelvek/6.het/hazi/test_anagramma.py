from anagramma import anagramma

def test_anagramma():
    assert anagramma("listen","silent") == True
    assert anagramma("egymás","sámga") == False
    assert anagramma("dormitory","dirty room") == False
    assert anagramma("valami","semmi") == False
    assert anagramma("","fwa") == False
    assert anagramma("","") == True
    assert anagramma("valami","malavi") == True


