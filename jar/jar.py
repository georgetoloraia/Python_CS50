class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._cookies = []

    def __str__(self):
        return "🍪" * len(self._cookies)

    def deposit(self, n):
        if len(self._cookies) + n > self._capacity:
            raise ValueError("Exceeded jar capacity")
        self._cookies.extend([None] * n)

    def withdraw(self, n):
        if len(self._cookies) < n:
            raise ValueError("Not enough cookies in the jar")
        del self._cookies[-n:]

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return len(self._cookies)
