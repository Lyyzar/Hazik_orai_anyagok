from median import median

def test_median():
    assert median([1])==1
    assert median([3, 1, 2, 5, 3])==3
    assert median([3, 6, 20, 99, 10, 15])==12.5
    assert median([1, 5, 4, 2, 7, 7, 4, 4, 3])==4
    
    
   
    