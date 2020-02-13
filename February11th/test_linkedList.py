from unittest import TestCase
from February11th import LinkedList

class TestLinkedList(TestCase):

    def test_append_and_get(self):
        # Arrange
        first = 1
        second = 2
        third = 3
        linked_list = LinkedList()
        linked_list.append(first)
        linked_list.append(second)
        linked_list.append(third)

        # act
        actual_first = linked_list.get(0)
        actual_second = linked_list.get(1)
        actual_third = linked_list.get(2)

        # assert
        self.assertEqual(first, actual_first)
        self.assertEqual(second, actual_second)
        self.assertEqual(third, actual_third)


    def test_insert(self):
        # Arrange
        first = 1
        second = 2
        third = 3
        new_first = 0
        new_third = 42
        linked_list = LinkedList()
        linked_list.append(first)
        linked_list.append(second)
        linked_list.append(third)

        # act
        linked_list.insert(new_first, 0)
        actual_first = linked_list.get(0)

        linked_list.insert(new_third, 3)
        actual_third = linked_list.get(3)

        # assert
        self.assertEqual(new_first, actual_first)
        self.assertEqual(new_third, actual_third)

    def test_pop(self):
        # Arrange
        first = 1
        second = 2
        third = 3
        linked_list = LinkedList()
        linked_list.append(first)
        linked_list.append(second)
        linked_list.append(third)

        # act
        actual_first = linked_list.pop(0)
        actual_last = linked_list.pop()

        # assert
        self.assertEqual(first, actual_first)
        self.assertEqual(third, actual_last)

    def test_remove(self):
        # Arrange
        first = 1
        second = 2
        third = 3
        linked_list = LinkedList()
        linked_list.append(first)
        linked_list.append(second)
        linked_list.append(third)
        expected_size = 1

        # act
        linked_list.remove(first)
        linked_list.remove(third)
        actual_size = len(linked_list)

        # assert
        self.assertEqual(expected_size, actual_size)

    def test_remove_and_add(self):
        # Arrange
        first = 1
        second = 2
        third = 3
        new_second = 42
        linked_list = LinkedList()
        linked_list.append(first)
        linked_list.append(second)
        linked_list.append(third)
        expected_size = 1

        # act
        linked_list.remove(first)
        linked_list.remove(third)
        linked_list.append(new_second)
        actual_second = linked_list.get(1)

        # assert
        self.assertEqual(new_second, actual_second)

