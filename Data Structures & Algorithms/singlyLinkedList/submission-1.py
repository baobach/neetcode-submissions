class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next  # type: ignore
        return current.data 

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1  

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        if index == 0:
            # remove head
            self.head = self.head.next  # type: ignore
            self.size -= 1
            return True

        prev = self.head
        for _ in range(index - 1):
            prev = prev.next  # type: ignore

        # skip over the node at index
        to_remove = prev.next  # type: ignore
        prev.next = to_remove.next  # type: ignore
        self.size -= 1
        return True
        
    def getValues(self) -> List[int]:
        empty_list = list()
        current = self.head
        while current:
            empty_list.append(current.data)
            current = current.next
        return empty_list
        
