import heapq as heap

class FullyAssociativeCache():
	SIZE = 0

	cache = [None] * SIZE

	# keeps track of how recently elements were accessed
	# elements closer to the front were accesed less recently
	accessOrder = [None] * SIZE

	# number of elements currently held in the cache
	numElements = 0

	hits = 0
	coldMisses = 0
	capacityMisses = 0

	# returns the least recently used element
	def least_recently_used(self):
		return self.accessOrder[0]

	def add(self, value):
		# if the cache is not full, place value into the first available slot
		if self.numElements < self.SIZE:
			self.cache[self.numElements] = value
			self.numElements += 1
		# if the cache is full
		else:
			index = 0
			i = 0
			# replace the least recently accessed element
			while i < self.numElements:
				if self.cache[index] is self.least_recently_used():
					index = i
					break
				i += 1
			self.cache[index] = value

		self.update_access_order(value)

	# search for a value in the cache
	def search(self, value):
		containsValue = False
		index = -1

		# checks if the value is in the cache
		i = 0
		while i < self.SIZE:
			if self.cache[i] is value:
				containsValue = True
				index = i
				break
			i += 1

		# returns the value
		if containsValue:
			self.hits += 1
			self.update_access_order(value)
			return self.cache[index]
		# insert the element to the cache
		else:
			if self.numElements is self.SIZE:
				self.capacityMisses += 1
			else:
				self.coldMisses += 1
			self.add(value)
			return value

	# recalculates the least recently accessed element
	def update_access_order(self, value):
		index = 0
		containsValue = False

		i = 0
		# checks if the element exists in the cache
		while i < self.numElements:
			if self.accessOrder[i] is value:
				index = i
				containsValue = True
				break
			i += 1

		# if the element exists in the cache
		if containsValue:
			# move the most recently accessed element to the back of the list
			self.accessOrder.remove(value)
		# if the element does not exist in the cache
		else:
			# overwrite the least recently used element if the cache is at capacity
			self.accessOrder.remove(self.least_recently_used())

		self.accessOrder.append(value)

	# returns the hit rate of the cache
	def hit_rate(self):
		return self.hits / (self.hits + self.coldMisses + self.capacityMisses)