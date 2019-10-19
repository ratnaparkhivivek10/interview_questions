# create custom iterator that will print even numbers

class InfiniteEvenNumbers(object):
    def __init__(self):
        self._cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        e = self._cursor
        self._cursor += 2

        return e


even_iter = InfiniteEvenNumbers()

for i in even_iter:
    print(i)

    if i == 30:
        break