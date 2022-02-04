def has_cycle(head):
    di = []
    save = head
    while head:
        if head in di:
            return 1
        else:
            di.append(head)
        head = head.next
    return 0
    