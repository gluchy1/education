class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Program przechodzi przez listę i obraca jej kolejność,
        # tak aby ostatni węzeł stał się pierwszym, drugi ostatnim, itd.

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Porównuje części listy

        while prev and head:
            if prev.val != head.val:
                return False
            prev, head = prev.next, head.next

        # Przywraca oryginalny stan listy

        curr, prev = prev, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        slow.next = prev

        return True