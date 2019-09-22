class Node:
    def __init__ (self, value = None, next = None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__ (self):
        self.first = None
        self.last = None
        self.len = 0

    def length(self) :
        return self.len

    def push (self, x):
        if self.first == None :
            self.first = Node(x)
            self.last = self.first
        else:
            self.first = Node(x, self.first)
        self.len += 1

    def add (self, x):
        if self.first == None :
            self.first = Node(x)
            self.last = self.first
        else:
            self.last.next = self.last = Node(x)
        self.len += 1

    def search (self, x):
        temp = self.first
        while temp != None :
            if temp.value == x :
                return temp
            temp = temp.next
        return temp

    def removebyposition (self, pos):
        if pos == 0 :
            self.first = self.first.next
            self.len -= 1
            return
        current = self.first
        if current == None :
            return
        else:
            previous = None
            cycle = 0
            while current != None and cycle != pos :
                cycle += 1
                previous = current
                current = current.next
            if current != None :
                previous.next = current.next
                self.len -= 1
            return

    def removebyvalue (self, value):
        current = self.first
        if current == None :
            return
        else:
            previous = None
            while current != None and current.value != value :
                previous = current
                current = current.next
            if current != None :
                previous.next = current.next
                self.len -= 1
            return

    def print (self):
        current = self.first
        while current != None :
            print(current.value)
            current = current.next

    def clear (self):
        self.__init__()
        return

#reversed
def IntoList (num) :
    list = SinglyLinkedList()
    if int(num) == 0 :
        list.add(int(num))
        return list
    for c in num :
        list.push(int(c))
    return list