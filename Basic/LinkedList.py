class node:
    def __init__(self, value=None, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous

    def get_all(self):
        return (self.value, self.next, self.previous)

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_previous(self):
        return self.previous

    def set_previous(self, previous):
        self.previous = previous


class linkedlist:
    # define starting node
    start = None
    finalNode = None
    currentNode = None
    doubleLinked = False
    length=0

    def __init__(self, doubleLinked=False):
        self.doubleLinked = doubleLinked

    def add(self, value):
        if self.start is None:
            self.start = node(value)
            self.finalNode = self.start
            self.currentNode = self.start
            self.length=1
        else:
            if self.doubleLinked:
                node_aux = node(value)
                previous=self.finalNode
                self.finalNode.set_next(node_aux)
                self.finalNode = node_aux
                self.finalNode.set_previous(previous)
                self.length+=1

            else:
                node_aux = node(value)
                self.finalNode.set_next(node_aux)
                self.finalNode = node_aux
                self.length += 1

    def reset_place(self):
        self.currentNode = self.start

    def increment(self):
        if (self.currentNode.get_next() != None):
            self.currentNode = self.currentNode.get_next()

    def decrement(self):
        if (self.currentNode.get_previous() != None):
            self.currentNode = self.currentNode.get_previous()

    def read_all(self):
        self.currentNode = self.start
        while True:
            print(self.currentNode.get_value())
            if (self.currentNode.get_next() == None):
                break
            else:
                self.increment()

    def get_length(self):
        return self.length


def test():
    x = linkedlist(doubleLinked=False)
    x.add(1)
    x.add(2)
    x.add(3)
    print("Lungimea e: ", x.get_length())
    x.read_all()
    x.add(4)
    x.increment()
    print(x.currentNode.get_value())
    print("Lungimea e: ", x.get_length())
    y = linkedlist(doubleLinked=True)
    y.add(1)
    print(y.currentNode.get_value())
    y.add(2)
    y.increment()
    print(y.currentNode.get_value())
    y.decrement()
    print(y.currentNode.get_value())
    print("Lungimea e: ", y.get_length())


test()
