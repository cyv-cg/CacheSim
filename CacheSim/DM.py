class DirectMappedCache():
	SIZE = 0
	cache = [None] * SIZE

	hits = 0
	coldMisses = 0
	conflictMisses = 0

	# returns the hash code of a value
	def get_hash_code(self, value):
		return value % self.SIZE

	# adds a value to the cache
	def add(self, value):
		self.cache[self.get_hash_code(value)] = value

	# Searches for a value in the cache and returns a hit, a cold miss, or conflict miss
	def search(self, value):
		code = self.get_hash_code(value)

		if self.cache[code] is value:
			self.hits += 1
		else:
			if not self.cache[code]:
				self.coldMisses += 1
			else:
				self.conflictMisses += 1

			self.add(value)

		return value

	# Returns the hit rate of cache wants finished 
	def hit_rate(self):
		return self.hits / (self.hits + self.coldMisses + self.conflictMisses)