from data_structures.linked_list import LinkedList
import unittest


class TestLinkedList(unittest.TestCase):
	def append_list_elems_into_linked_list(self, list):
		linked_list = LinkedList()
		for elem in list:
			linked_list.append(elem)
		return linked_list

	def insert_list_elems_into_linked_list(self, list):
		linked_list = LinkedList()
		for elem in list:
			linked_list.insert(elem)
		return linked_list

	# === Basic Append, Remove Tests ===

	def test_empty(self):
		empty = []
		linked_list = self.append_list_elems_into_linked_list(empty)
		self.assertTrue(linked_list.is_empty())

	def test_one(self):
		one = [23]
		linked_list = self.append_list_elems_into_linked_list(one)
		self.assertFalse(linked_list.is_empty())
		linked_list.remove(0)
		self.assertTrue(linked_list.is_empty())

	def test_even(self):
		even = [1, 66, 44, 231, -44, 55]
		linked_list = self.append_list_elems_into_linked_list(even)
		self.assertFalse(linked_list.is_empty())
		for _ in even:
			linked_list.remove(0)
		self.assertTrue(linked_list.is_empty())

	def test_odd(self):
		odd = [1, 66, 44, 231, -44, 55, 100]
		linked_list = self.append_list_elems_into_linked_list(odd)
		self.assertFalse(linked_list.is_empty())
		for _ in odd:
			linked_list.remove(0)
		self.assertTrue(linked_list.is_empty())

	# === Test LinkedList methods ===

	TEST_LIST = [1, 66, 44, 231, -44, 55, 100]

	def test_insert_elements_in_list(self):
		linked_list = self.insert_list_elems_into_linked_list(self.TEST_LIST)
		self.assertFalse(linked_list.is_empty())
		self.assertTrue(set(self.TEST_LIST) == set(linked_list.convert_to_list()))

	def test_clear_list(self):
		linked_list = self.insert_list_elems_into_linked_list(self.TEST_LIST)
		linked_list.clear()
		self.assertTrue(linked_list.is_empty())

if __name__ == '__main__':
	unittest.main()
