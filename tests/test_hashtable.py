from src.hashtable import HashTable

import pytest
from pytest_unordered import unordered

def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None

def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100

# todo: revisit this
def test_should_not_contain_none_value_when_created(fresh_empty_hashtable):
    #ht = HashTable(capacity=10)
    assert None not in fresh_empty_hashtable.values

def test_should_create_empty_value_slots():
    # Justification for directly accessing internal attribute: white-box testing
    assert HashTable(capacity=3)._pairs == [None, None, None]

def test_should_insert_key_value_pairs():
    hashtable = HashTable(capacity=100)
    hashtable['hola'] = 'hello'
    hashtable[98.6] = 37
    hashtable[False] = True

    assert 'hola' in hashtable
    assert 98.6 in hashtable
    assert False in hashtable
    assert ('hola', 'hello') in hashtable.pairs
    assert (98.6, 37) in hashtable.pairs
    assert (False, True) in hashtable.pairs

    assert len(hashtable) == 100

def test_should_insert_none_value():
    hashtable = HashTable(capacity=10)
    hashtable['key'] = None
    assert 'key' in hashtable
    assert ('key', None) in hashtable.pairs

def test_should_find_value_by_key(sample_hashtable):
    assert sample_hashtable['hola'] == 'hello'
    assert sample_hashtable[98.6] == 37
    assert sample_hashtable[False] == True

def test_should_raise_error_on_missing_key(sample_hashtable):
    with pytest.raises(KeyError) as exception_info:
        sample_hashtable['missing_key']
    assert exception_info.value.args[0] == 'missing_key not found.'

def test_should_find_key_if_exists(sample_hashtable):
    assert 'hola' in sample_hashtable
    assert 98.6 in sample_hashtable
    assert False in sample_hashtable

def test_should_not_find_key_if_not_exists(sample_hashtable):
    assert 'missing_key' not in sample_hashtable

def test_should_get_value(sample_hashtable):
    assert sample_hashtable.get('hola') == 'hello'

def test_should_get_default_value_on_missing_key(sample_hashtable):
    assert sample_hashtable.get('missing_key', 'default') == 'default'

def test_should_get_none_on_missing_key(sample_hashtable):
    assert sample_hashtable.get('missing_key') == None

def test_should_get_value_with_default_given(sample_hashtable):
    assert sample_hashtable.get('hola', 'default') == 'hello'

def test_should_delete_key_value_pair(sample_hashtable):
    assert 'hola' in sample_hashtable
    assert ('hola', 'hello') in sample_hashtable.pairs
    assert len(sample_hashtable) == 50

    del sample_hashtable['hola']

    assert 'hola' not in sample_hashtable
    assert ('hola', 'hello') not in sample_hashtable.pairs
    assert len(sample_hashtable) == 50

def test_should_raise_error_when_deleting_missing_key(sample_hashtable):
    with pytest.raises(KeyError) as exception_info:
        del sample_hashtable['missing_key']
    assert exception_info.value.args[0] == 'missing_key not found.'

def test_should_update_value(sample_hashtable):
    assert sample_hashtable['hola'] == 'hello'

    sample_hashtable['hola'] = 'howdy'

    assert sample_hashtable['hola'] == 'howdy'
    assert sample_hashtable[98.6] == 37
    assert len(sample_hashtable) == 50

def test_should_return_copy_of_pairs(sample_hashtable):
    assert sample_hashtable.pairs is not sample_hashtable.pairs

def test_should_not_include_blank_pairs(sample_hashtable):
    assert None not in sample_hashtable.pairs

def have_same_elements(list1, list2):
    return all(elem in list1 for elem in list2)

def test_should_return_duplicate_values_if_applicable():
    ht = HashTable(capacity=10)
    ht['alice'] = 42
    ht['bob'] = 50
    ht['job'] = 42

    assert sorted(ht.values) == [42, 42, 50]
    assert have_same_elements(ht.values, [42, 42, 50])
    assert unordered(ht.values) == [42, 42, 50]

def test_should_get_values_of_empty_hashtable():
    assert HashTable(capacity=10).values == []

def test_should_return_copy_of_values(sample_hashtable):
    assert sample_hashtable.values is not sample_hashtable.values

def test_should_get_keys(sample_hashtable):
    assert sample_hashtable.keys == {'hola', 98.6, False}

def test_should_get_keys_of_empty_hashtable():
    assert HashTable(capacity=10).keys == set()

def test_should_return_copy_of_keys(sample_hashtable):
    assert sample_hashtable.keys is not sample_hashtable.keys

def test_should_return_pairs(sample_hashtable):
    assert sample_hashtable.pairs == {
        (False, True), ('hola', 'hello'), (98.6, 37)
    }

def test_should_get_pairs_of_empty_hashtable():
    assert HashTable(capacity=10).pairs == set()

def test_should_convert_to_dict(sample_hashtable):
    dictionary = dict(sample_hashtable.pairs)
    assert set(dictionary.keys()) == sample_hashtable.keys
    assert list(dictionary.values()) == unordered(sample_hashtable.values)
    assert set(dictionary.items()) == sample_hashtable.pairs

@pytest.fixture
def sample_hashtable():
    '''Returns a hashtable of capacity 50 and some items populated.'''
    sample_data = HashTable(capacity=50)
    sample_data['hola'] = 'hello'
    sample_data[98.6] = 37
    sample_data[False] = True
    #sample_data[0] = 'zero'
    return sample_data

@pytest.fixture
def fresh_empty_hashtable():
    '''Returns a newly created empty hastable of capacity 10.'''
    return HashTable(capacity=10)