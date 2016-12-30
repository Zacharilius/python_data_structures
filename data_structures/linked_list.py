class Node(object):
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, node):
		self.next = node


class LinkedList(object):
	def __init__(self):
		self.head = None

	def is_empty(self):
		return self.head is None

	def insert(self, data):
		old_head = self.head
		self.head = Node(data)
		self.head.set_next(old_head)

	def append(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		node = self.head
		while node.get_next() is not None:
			node = node.get_next()
		node.set_next(new_node)

	def remove(self, location):
		if location == 0:
			removing_head = self.head
			self.head = self.head.next
			return  removing_head
		prev_node = self.head
		node = prev_node.get_next()
		for _ in range(location) - 1:
			prev_node = node
			node = node.get_next()
		removing_node = node
		prev_node.set_next(node.get_next())
		return removing_node

	def convert_to_list(self):
		node = self.head
		linked_list_list = [node.get_data()]
		while node.get_next() is not None:
			node = node.get_next()
			linked_list_list.append(node.get_data())
		return linked_list_list

	def clear(self):
		self.head = None
