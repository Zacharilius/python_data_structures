from contextlib import redirect_stdout
from data_structures.linked_list import LinkedList
from data_structures.binary_search_tree import BinarySearchTree, TreeNode
import io
import unittest


# === Linked List ===

class TestLinkedList(unittest.TestCase):
	def append_list_elems_into_linked_list(self, list):
		linked_list = LinkedList()
		for elem in list:
			linked_list.append(elem)
		return linked_list

	def insert_list_elems_into_linked_list(self, list):
		linked_list = LinkedList()
		for val in list:
			linked_list.insert(val)
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

	TEST_LIST = [1, 66, 44, 231, -44, 55, 100, 22, 55]

	def test_insert_elements_in_list(self):
		linked_list = self.insert_list_elems_into_linked_list(self.TEST_LIST)
		self.assertFalse(linked_list.is_empty())
		self.assertTrue(set(self.TEST_LIST) == set(linked_list.convert_to_list()))

	def test_clear_list(self):
		linked_list = self.insert_list_elems_into_linked_list(self.TEST_LIST)
		linked_list.clear()
		self.assertTrue(linked_list.is_empty())

	def test_find_middle_value(self):
		linked_list = self.append_list_elems_into_linked_list(self.TEST_LIST)
		middle_value = linked_list.get_middle_value()
		self.assertTrue(middle_value == self.TEST_LIST[len(self.TEST_LIST) // 2 - 1])


# === Binary Search Tree ===

class TestBinarySearchTree(unittest.TestCase):
    def test_bst_inorder(self):
        bst = self.insert_list_elems_into_binary_search_tree()
        inorder_output = bst.inorder()
        expected_inorder_output = [-44, 1, 22, 44, 55, 55, 66, 100, 231]
        self.assertTrue(inorder_output == expected_inorder_output)

    def test_bst_preorder(self):
        bst = self.insert_list_elems_into_binary_search_tree()
        preorder_output = bst.preorder()
        expected_preorder_output = [1, -44, 66, 44, 22, 55, 55, 231, 100]
        self.assertTrue(preorder_output == expected_preorder_output)

    def test_bst_postorder(self):
        bst = self.insert_list_elems_into_binary_search_tree()
        postorder_output = bst.postorder()
        expected_postorder_output = [-44, 22, 55, 55, 44, 100, 231, 66, 1]
        self.assertTrue(postorder_output == expected_postorder_output)

    def test_bst_height(self):
        bst = self.insert_list_elems_into_binary_search_tree()
        bst_height = bst.height()
        expected_bst_height = 5
        self.assertTrue(bst_height == expected_bst_height)

    # === Test Util ===

    DEFAULT_LIST = [1, 66, 44, 231, -44, 55, 100, 22, 55]

    def insert_list_elems_into_binary_search_tree(self, test_list=None):
        if test_list is None:
            test_list = self.DEFAULT_LIST
        bst = BinarySearchTree()
        for val in test_list:
            bst.insert(val)
        return bst


# === Main ===
if __name__ == '__main__':
	unittest.main()
