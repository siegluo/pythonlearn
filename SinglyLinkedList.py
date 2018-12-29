# -*- coding: utf-8 -*-

class Node:

    def __init__(self, data, next=None):
        self._next = next
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def find_by_value(self, value):
        node = self._head
        while node is not None and node.data != value:
            node = node.next
        return node

    def find_by_index(self, index):
        pos = 0
        node = self._head
        while node is not None and pos != index:
            pos += 1
            node = node.next
        return node

    def add_node(self, value):
        node = Node(value)
        node._next = self._head
        self._head = node

    def insert_after_node(self, value, index):
        after_node = self.find_by_index(index)
        if after_node is None:
            return
        node = Node(value, after_node.next)
        after_node.next = node

    def insert_before_node(self, value, index):

        after_node = self.find_by_index(index)
        if after_node is None:
            return
        node = Node(value)
        node.next = after_node
        if index == 0:
            return
        else:
            before_node = self.find_by_index(index - 1)
            before_node.next = node

    def delete_by_index(self, index):
        after_node = self.find_by_index(index)
        if after_node is None:
            return
        before_node = self.find_by_index(index - 1)
        before_node.next = after_node.next

    def has_ring(self):
        fast = self._head
        slow = self._head
        while fast.next is not None and fast is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def find_mid(self):
        fast = self._head
        slow = self._head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reversed_list(self):
        pro = self._head
        node = self._head.next
        while node.next:
            pro, node = self._reversed_two(pro, node)
        self._head = pro

    def _reversed_two(self, pro, node):
        temp = node.next
        node.next = pro
        return (node, temp)


if __name__ == '__main__':
    list = SinglyLinkedList()
    list.add_node(1)
    list.add_node(2)
    print(list.find_by_value(1))
