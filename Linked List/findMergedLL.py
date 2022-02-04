def findMergeNode(head1, head2):
    di = {}
    while head1:
        di[head1] = head1
        head1 = head1.next
    print(di)
    while head2:
        if head2 in di:
            return head2.data
        head2 = head2.next