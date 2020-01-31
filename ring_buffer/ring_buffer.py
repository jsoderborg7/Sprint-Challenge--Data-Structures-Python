from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
    # Ok, so since ring buffers have a specific capacity, the size of the DLL has to be at capacity
    # We'll start with the buffer when it hasn't reached the limit yet
        if self.storage.length != self.capacity:
            self.current = self.storage.head
            self.storage.add_to_tail(item)
        else:
    # If we are at capacity:
    # start by overwriting the current node
            self.current.value = item
    # and if we're at the tail, we need to come back around to the head
            if self.current is self.storage.tail:
                self.current = self.storage.head
            else:
    # if we weren't at the tail, update the position to the next node
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head
        while current:
            list_buffer_contents.append(current.value)
            current = current.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
