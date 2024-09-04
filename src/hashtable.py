class HashTable:
    def __init__(self, capacity):
        self._pairs = [None] * capacity

    def __len__(self):
        return len(self._pairs)

    def __setitem__(self, key, value):
        idx = self._index(key)
        self._pairs[idx] = (key, value)

    def __getitem__(self, key):
        idx = self._index(key)
        pair = self._pairs[idx]
        if pair is None:
            raise KeyError(f'{key} not found.')
        return pair[1]

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __delitem__(self, key):
        if key in self:
            self._pairs[self._index(key)] = None
        else:
            raise KeyError(f'{key} not found.')

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    @property
    def pairs(self):
        return {pair for pair in self._pairs if pair}

    @property
    def keys(self):
        return {pair[0] for pair in self.pairs}

    @property
    def values(self):
        return [pair[1] for pair in self.pairs]

    def _index(self, key):
        h = hash(key)
        return h % len(self)

if __name__ == '__main__':
    ht = HashTable(capacity=10)
    ht['hola'] = 'hello'
    ht[98.6] = 37
    ht[False] = True
    ht['obj'] = [1, 2, 3]
    ht['0'] = 'zero'
    ht[0] = '000'

    print(ht._pairs)
