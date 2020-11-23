class NWayAssociativeCache():
	SIZE = 0
	ASSOCIATIVITY = 1

	cache = [[None] * 1 for i in range(1)]
	hits = 0
	coldMisses = 0
	capacityMisses = 0

	#retrieves the hash code
	def get_hash_code(self,value):
		return value % self.SIZE

	#searches for the given value if it is found reports a hit if it isnt reports one of the two possible misses 
	def search(self, value):
		code = self.get_hash_code(value)
		atCapacity = True

		#if found reports miss
		if value in self.cache[code]:
			self.hits += 1
			self.updateAccessOrder(value)
			return value

		i = 0
		#if it isnt found checks if the cache is at full capacity
		while i < self.ASSOCIATIVITY:
			if not self.cache[code][i]:
				atCapacity = False
			i += 1
			#if it is reports a capacity miss
		if atCapacity:
			self.capacityMisses += 1
			#if not reports a cold miss
		else:
			self.coldMisses += 1
		self.add(value)

	# adds the values to the cache
	def add(self, value):
		code = self.get_hash_code(value)

		i = 0
		#adds value to the first empty slot
		while i < self.ASSOCIATIVITY:
			if not self.cache[code][i] and self.cache[code][i] is not 0:
				self.cache[code][i] = value
				return value
			i += 1
		# if there is no empty slot adds to the first index and updates the order
		self.cache[code][0] = value
		self.updateAccessOrder(value)

	# updates the order of when elements were accessed
	def updateAccessOrder(self, value):
		code = self.get_hash_code(value)
		i = 0
		# if the shifts the value to the back of the cache slot 
		while i < self.ASSOCIATIVITY - 1:
			if self.cache[code][i] is value and self.cache[code][i + 1] is not None:
				self.cache[code][i] = self.cache[code][i + 1]
				self.cache[code][i + 1] = value
			i += 1

	# Returns the hit rate of cache wants finished 
	def hit_rate(self):
		return self.hits / (self.hits + self.coldMisses + self.capacityMisses)




		#chris is cute u~w~u -----> ~/)(\~ "ba-ba-ba-baka its not like i like him or anything" 
		#(┬┬﹏┬┬)