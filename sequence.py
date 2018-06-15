class Sequence(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.curr = self.head
        self.count = 0

    class Node(object):
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

        def __str__(self):
            return str(self.data)

    def add_back(self, data):
        node = self.Node(data)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node
        if not self.head:
            self.head = self.tail

        self.count += 1

    def __iter__(self):
        self.curr = self.head
        return self

    def __next__(self):
        if self.curr:
            data = self.curr.data
            self.curr = self.curr.next
            return data
        else:
            raise StopIteration()


    def add_front(self, data):
        node = self.Node(data)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = self.head
        self.count += 1

    def __find__(self, i):
        if i < 0:
            i = abs(i) - 1;

        if i >= self.count:
            return None

        avg = (self.count-1) / 2
        if i < avg:
            j = 0
            node = self.head
            while j < i :
                node = node.next
                j = j + 1
            return node

        if i > avg:
            j = self.count - 1
            node = self.tail
            while j > i:
                node = node.prev
                j = j - 1
            return node

    def __getitem__(self, i):
        node = self.__find__(i)
        return node

    def __len__(self):
        return self.count

    def __setitem__(self, i, v):
            node = self.__find__(i)
            node.data = v

    def remove_front(self):
        if self.head:
            self.head = self.head.next

    def remove_back(self):
        if self.tail:
            tmp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            del(tmp)

    def remove(self, v):
        node = self.head
        while node.data != v:
            node = node.next
        if node:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            del(node)

    def sort(self):
        pass


if __name__ == "__main__":
    S = Sequence()
    len(S)
    S.add_front(3)
    S.add_back(9)
    # print(S[0])
    # print(S[1])
    # print(S[-1])
    S.add_back(12)
    iter = S.__iter__()
    # print(iter.__next__())
    print(list(S))
    # print(next(next(next(iter(S)))))
    S.remove(3)
