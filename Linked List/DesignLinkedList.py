class Node:

    def __init__(self, value=0, nxt=None):
        self.val = value
        self.nxt = nxt


class MyLinkedList:

    def __init__(self):
        self.node = None

    def get(self, index: int) -> int:
        count = 0
        head = self.node
        self.cout()
        while head:
            if count == index:
                return head.val
            count += 1
            head = head.nxt
        self.cout()
        return -1

    def cout(self):
        head = self.node
        while head:
            print(head.val)
            head = head.nxt

    def addAtHead(self, val: int) -> None:

        temp = self.node
        if temp is None:
            self.node = Node(val)
        else:
            new = Node(val, temp)
            self.node = new
        # self.cout()
    def addAtTail(self, val: int) -> None:
        temp = self.node
        if temp == None:
            self.node = Node(val)
        else:
            while temp:
                if temp.nxt == None:
                    # print("tes")
                    temp.nxt = Node(val)
                    break
                temp = temp.nxt
        # self.cout()

    def addAtIndex(self, index: int, val: int) -> None:
        count = 0
        head = self.node
        if index < 0 or index > self.size():
            return -1
        if index == 0:
            self.addAtHead(val)
        else:
            while head:
                if count == index - 1:
                    n = head.nxt
                    new = Node(val, n)
                    head.nxt = new
                count += 1
                head = head.nxt

    def size(self):
        node = self.node
        count = 0
        while node:
            count = count + 1
            node = node.nxt
        return count

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size():
            return
        elif index == 0:
            node = self.node
            self.node = node.nxt
            del node
        else:
            itr = self.node
            i = index - 1
            while i:
                itr = itr.nxt
                i -= 1
            node = itr.nxt
            itr.nxt = node.nxt
            del node