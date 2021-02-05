class SingleNode(object):
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        prependedNode = SingleNode(value)
        prependedNode.next = self.head
        self.head = prependedNode
        return

    def append(self, value):
        if self.isEmpty():
            self.head = SingleNode(value)
            return
        prev = None
        pointer = self.head
        while pointer != None:
            prev = pointer
            pointer = pointer.next
        prev.next = SingleNode(value)
        pointer = None
        return

    def pop(self) -> SingleNode:
        if (self.isEmpty()):
            raise Exception('is empty')
        removedNode = self.head
        self.head = self.head.next
        return removedNode

    def get(self, indexNo):
        if self.isEmpty():
            raise Exception('is empty')
        pointer = self.head
        counter = 0
        while pointer != None and counter != indexNo:
            pointer = pointer.next
            counter += 1
        if pointer != None:
            return pointer.value
        else:
            raise Exception("out of index")

    def isEmpty(self):
        return self.head is None

    def count(self):
        if self.isEmpty():
            return 0
        counter = 0
        pointer = self.head
        while pointer != None:
            counter += 1
            pointer = pointer.next
        return counter

    def removeValue(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return
        length = self.count()
        pointer = self.head
        prev = None
        counter = 0
        while pointer.value != value and counter < length - 1:
            prev = pointer
            pointer = pointer.next
            counter += 1

        if pointer.value != value:
            raise Exception("not in list")
        pointer = pointer.next
        prev.next = pointer
        return

    def remove(self, indexNo):
        pointer = self.head
        prev = None
        counter = 0
        while pointer != None and counter != indexNo:
            prev = pointer
            pointer = pointer.next
            counter += 1
        if counter == indexNo:
            prev.next = pointer.next
            pointer.next = None
        else:
            raise Exception("not in index")

    def __str__(self):
        string = ''
        pointer = self.head
        if (self.isEmpty()):
            return string
        while pointer.next != None:
            string += str(pointer.value) + '->'
            pointer = pointer.next
        string += str(pointer.value)
        return string



class DoublyList(object):
  def __init__(self):
    self.head = None
    self.tail = None

  def prepend(self, value):
    NewNode = SingleNode(value)
    NewNode.next = self.head
    if self.head is not None:
      self.head.prev = NewNode
    self.head = NewNode
    return

  def append(self, value):
    NewNode = SingleNode(value)
    NewNode.next = None
    if self.head is None:
      NewNode.prev = None
      self.head = NewNode
      return
    last = self.head
    while (last.next is not None):
      last = last.next
    last.next = NewNode
    NewNode.prev = last
    return

  def isEmpty(self):
    return self.head is None
    


class Stack(LinkedList):
    def __init__(self):
        super().__init__()



class Queue(object):
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, value):
        eNode = SingleNode(value)
        if self.queue.isEmpty():
            self.queue.head = eNode
            self.queue.tail = eNode
            return
        self.queue.prepend(value)
        return

    def dequeue(self):
        if self.queue.isEmpty():
            raise Exception('Empty queue')
        elif self.queue.head.next == None:
            self.queue.head = None
            self.queue.tail = None
            return
        prev = None
        pointer = self.queue.head
        while pointer != self.queue.tail:
            prev = pointer
            pointer = pointer.next
        prev.next = None
        self.queue.tail = prev
        return

    def __str__(self):
        return self.queue.__str__()


class IntegerArray(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.items = LinkedList()

    def append(self, value):
        if self.count >= self.capacity:
            raise Exception("Array is full")
        self.items.append(value)
        self.count += 1
        return

    def removeValue(self, value):
        self.items.removeValue(value)

    def pop(self, indexNo=0):
        if indexNo == 0:
            self.items.pop()
        else:
            self.items.remove(indexNo)
        self.count -= 1

    def isEmpty(self):
        return self.count == 0

    def sum(self) -> int:
        if self.isEmpty():
            return 0
        returnValue = 0

        for i in range(self.count):
            returnValue += self.get(i)
        return returnValue
        # while counter < self.count:
        #   sum += pointer.value
        #   pointer = pointer.next
        #   counter += 1
        # return sum

    def get(self, indexNo):
        return self.items.get(indexNo)

    def __str__(self):
        return self.items.__str__()


class DynamicArray(object):
    def __init__(self):
        self.count = 0
        self.capacity = 1
        self.items = LinkedList()

    def append(self, value):
        if self.count >= self.capacity:
            self.capacity += 1
        self.items.append(value)
        self.count += 1
        return

    def getItem(self, index):
        if index > self.capacity - 1:
            raise Exception("Out of index")
        elif self.items.isEmpty():
            raise Exception("Array is empty")
        counter = 0
        pointer = self.items.head
        while counter < index:
            pointer = pointer.next
            counter += 1
        return pointer.value

    def setItem(self, index, value):
        if index > self.capacity - 1:
            raise Exception("Out of index")
        elif self.items.isEmpty():
            raise Exception("Array is empty")
        counter = 0
        pointer = self.items.head
        while counter < index:
            pointer = pointer.next
            counter += 1
        pointer.value = value
        return

    def len(self):
        return self.count

    def setCapacity(self, value):
        if value == 0:
            self.count = 0
            self.capacity = 0
            self.items.head = None
            return
        elif self.count > value and value > 0:
            counter = 1
            pointer = self.items.head
            while counter < value:
                pointer = pointer.next
                counter += 1
            pointer.next = None
            self.capacity = value
            self.count = value
            return
        elif value < 0:
            raise Exception('Invalid capacity')
        self.capacity = value
        return

    def removeValue(self, value):
        self.items.removeValue(value)

    def get(self, indexNo):
        return self.items.get(indexNo)

    def __str__(self):
        string = '['
        empty = '[]'
        pointer = self.items.head
        if (self.items.isEmpty()):
            return empty
        while pointer.next != None:
            string += str(pointer.value) + ', '
            pointer = pointer.next
        string += str(pointer.value)
        string += ']'
        return string


class algebraic_term(object):
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent

    def value(self, input: int):
        return self.coefficient * (input**self.exponent)

    def __str__(self):
        string = str(self.coefficient) + "x"
        if self.exponent >= 2:
            string += "^" + str(self.exponent)
        return string


class function_equation(object):
    def __init__(self, coefficients_list):
        # self.qt = qt(first)
        # self.lt = lt(second)
        # self.const = third]
        self.terms = []
        self.const = 0
        for i in range(len(coefficients_list) - 1):
            self.terms.append(
                algebraic_term(coefficients_list[i],
                               len(coefficients_list) - i - 1))
        if coefficients_list != []:
            self.const = coefficients_list[-1]

    def inputValue(self, input):
        return sum([i.value(input) for i in self.terms]) + self.const

    def __str__(self):
      strings = [i.__str__() for i in self.terms]
      x = ''
      for i in strings:
        x+=i+'+'
      x+=str(self.const)
      return x

