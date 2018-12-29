# *-* coding: utf-8 *-*

def is_palindrome(list):
    fast = list._head
    slow = list._head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next


def reversed(node):
    tmp = None
    while node:
        next = node.next
        node.next = tmp
        tmp = node
        node = next
