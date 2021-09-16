def evenAfterOdd(head) :
    if head is None :
        return head

    evenHead, oddHead, evenTail, oddTail = None, None, None, None
    
    while head is not None :
        if (head.data % 2) == 0 :
            if evenHead is None :
                evenHead = head
                evenTail = head
            else :
                evenTail.next = head
                evenTail = evenTail.next
        else:
            if oddHead is None :
                oddHead = head
                oddTail = head
            else:
                oddTail.next = head
                oddTail = oddTail.next

        head = head.next


    if oddHead is None :
        return evenHead
    else :
        oddTail.next = evenHead

    if evenHead is not None :
        evenTail.next = None

    return oddHead