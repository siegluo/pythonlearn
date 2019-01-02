# *-* coding: utf-8 *-*
import sys

sys.path.append('List')
from SinglyLinkedList import SinglyLinkedList


def reversed(node):
    reverse_head = None
    while node:
        next = node.next
        node.next = reverse_head
        reverse_head = node
        node = next
    return reverse_head


def is_palindrome(list):
    fast = list._head
    slow = list._head
    position = 0
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        position += 1
    reverse_head = reversed(slow)
    is_plain = True
    node = list._head
    while node and reverse_head:
        if node.data == reverse_head.data:
            node = node.next
            reverse_head = reverse_head.next
        else:
            is_plain = False
            break
    return is_plain


if __name__ == '__main__':
    s = SinglyLinkedList()
    s.add_node(1)
    s.add_node(2)
    s.add_node(3)
    s.add_node(3)
    s.add_node(2)
    s.add_node(1)
    a = is_palindrome(s)
    print(a)
