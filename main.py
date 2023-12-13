
class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.count = 0

    def insert_at_begining(self, value):
        node = Node(value, self.head)
        self.head = node

    def insert_at_end(self, value):

        if self.head is None:     # when head is null (at the end)
            self.head = Node(value, None)     # None is the next pointer location
            return
        else:
            pointer = self.head
            while pointer.next:    # this run until pointer.next as None value(at the end)
                pointer = pointer.next     # this will increment pointer value

            pointer.next = Node(value, None)       # at the element at the end
            return

    def inster(self, value, index):
        pointer = self.head
        count = 0
        if index < 0 or index > self.lenth():
            raise Exception("Invalid Index")

        else:
            while pointer:
                if count == index - 1:
                    temp = pointer.next      # store the pointer.next value
                    pointer.next = Node(value, pointer.next.next)    # give new value to next pointer
                    pointer.next.next = temp    # give the new stored value its pointer.next store value
                    """   use this 
                    node = Node(value, pointer.next)    first create node and store "next" value
                    pointer.next = node                 now change the "next" value
                    """
                count += 1
                pointer = pointer.next

    def lenth(self):
        pointer = self.head
        count = 0
        while pointer:
            count += 1
            pointer = pointer.next

        return count

    def display(self):

        if self.head is None:        # if head is null then list is empty
            print("linked list is empty")
            return

        pointer = self.head          # first value
        lstr = ''
        while pointer:                 # run until pointer is null
            lstr += str(pointer.value) + ' --> '     # making word1 key of all the element is linked list
            pointer = pointer.next          # incrementing value of pointer

        print(lstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(12)
    ll.insert_at_end(50)
    ll.inster(22, 1)
    ll.inster(60, 3)
    ll.display()
