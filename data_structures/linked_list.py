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

	def get_middle_value(self):
		size = self.get_size()
		node = self.head
		for _ in range(size // 2 - 1):
			node = node.get_next()
		return node.get_data()


	def get_size(self):
		if self.head == None:
			return 0
		node = self.head
		size = 1
		while node.get_next() is not None:
			size += 1
			node = node.get_next()
		return size

	def is_empty(self):
		return self.head is None

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

	def clear(self):
		self.head = None

	def convert_to_list(self):
		node = self.head
		linked_list_list = [node.get_data()]
		while node.get_next() is not None:
			node = node.get_next()
			linked_list_list.append(node.get_data())
		return linked_list_list
