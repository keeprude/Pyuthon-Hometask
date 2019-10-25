"""solution"""

class Node:
    """definition of nodes for SinglyLinkedList"""

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    """definition of the class"""

    def __init__(self):
        self.first = None
        self.last = None
        self.len = 0

    def length(self):
        """returns the number of elements in SinglyLinkedList"""

        return self.len

    def push(self, num):
        """puts element in the beginning of the SinglyLinkedList"""

        if self.first is None:
            self.first = Node(num)
            self.last = self.first
        else:
            self.first = Node(num, self.first)
        self.len += 1

    def add(self, num):
        """puts element in the end of SinglyLinkedList"""

        if self.first is None:
            self.first = Node(num)
            self.last = self.first
        else:
            self.last.next = self.last = Node(num)
        self.len += 1

    def search(self, value):
        """returns the node with requested value"""

        temp = self.first
        while temp is not None:
            if temp.value == value:
                return temp
            temp = temp.next
        return temp

    def remove_by_position(self, pos):
        """removes element in SinglyLinkedList by the requested position"""

        if pos == 0:
            self.first = self.first.next
            self.len -= 1
            return
        current = self.first
        if current is None:
            return
        else:
            previous = None
            cycle = 0
            while current is not None and cycle != pos:
                cycle += 1
                previous = current
                current = current.next
            if current is not None:
                previous.next = current.next
                self.len -= 1
            return

    def remove_by_value(self, value):
        """removes element in SinglyLinkedList by the requested value"""
        
        current = self.first
        if current is None:
            return
        else:
            previous = None
            while current is not None and current.value != value:
                previous = current
                current = current.next
            if current is not None:
                previous.next = current.next
                self.len -= 1
            return

    def print(self):
        """prints the SinglyLinkedList"""

        current = self.first
        result = []
        while current is not None:
            #print(current.value)
            result.append(current.value)
            current = current.next
        print(result)

    def clear(self):
        """destroys the SinglyLinkedList"""

        self.__init__()
        return

def into_list(num):
    """reversed"""

    my_list = SinglyLinkedList()
    if int(num) == 0:
        my_list.add(int(num))
        return my_list
    for digit in num:
        my_list.push(int(digit))
    return my_list

if __name__ == "__main__":
    INPUT_NUMBER = input()
    MY_LISTING = into_list(INPUT_NUMBER)
    SinglyLinkedList.print(MY_LISTING)
