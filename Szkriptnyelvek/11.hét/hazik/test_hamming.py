from hamming import hamming

def test_hamming():
    assert hamming("lecke","pecke") == 1
    assert hamming("keceja","valami") == 6
    assert hamming("kétszer","egyszer") == 3
    assert hamming("holv","hlov") == 2
    assert hamming("","") == 0