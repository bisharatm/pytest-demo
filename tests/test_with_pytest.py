def test_always_passes():
    assert True

#def test_always_fails():
#    assert False

def test_uppercase():
    assert 'loud noises'.upper() == 'LOUD NOISES'

def test_reversed():
    assert list(reversed([1, 2, 3])) == [3, 2, 1]

def test_some_primes():
    assert 11 in {
        num for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }