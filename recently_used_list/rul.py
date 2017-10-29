# TDD Iterations

# 1. Write the simplest failing test.

# 2. Write the simplest production
# code that passes all tests.

# 3. Refactor both production code
# and tests, if necessary.

class RecentlyUsedList(object):
    def __init__(self):
        self._list = []

    def __len__(self):
        return len(self._list)

    def insert(self, item):
        try:
            self._list.remove(item)
        except ValueError:
            pass
        self._list.insert(0, item)

    def __getitem__(self, index):
        return self._list[index]

    def __eq__(self, other):
        return self._list == other._list


if __name__ == '__main__':
    rul = RecentlyUsedList()
    rul.insert('first')
    rul.insert('second')
    rul.insert('third')
    # rul[0] == rul.__getitem__(0)
    print(rul[0])  # ==> 'third'
    # len(rul) == rul.__len__()
    print(len(rul))  # ==> 3
    print(list(rul))  # ==> ['third', 'second', 'first']
    rul.insert('second')
    print(list(rul))  # ==> ['second', 'third', 'first']
    
    # a == b is the same as a.__eq__(b)
    print(rul == RecentlyUsedList())  # ==> False
    another = RecentlyUsedList()
    another.insert('first')
    another.insert('third')
    another.insert('second')
    print(rul == another)  # ==> True
