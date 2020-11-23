from DM import DirectMappedCache
from FA import FullyAssociativeCache
from NW import NWayAssociativeCache

import random as r
import time

class CacheSim:
	# typical size of an L1 cache, 256 kilobytes
	SIZE_IN_BYTES = 256000
	SIZE_PER_ELEMENT = 4
	SIZE = int(SIZE_IN_BYTES / SIZE_PER_ELEMENT)

	ASSOCIATIVITY = 1

	direct = DirectMappedCache()
	full = FullyAssociativeCache()
	n_way = NWayAssociativeCache()

	cache = full

	max = 1000000
	min = 1

	readFromFile = 0

	FILE = "spacial1.txt"

	# Takes in user-input sizes for the cache (Makes it customizeable)
	def user_control(self):
		# determine the type of cache to use, clamp from 0-2
		userSelect = int(input("Please enter one of the following \n 0) Direct Map Cache \n 1) Fully Associative \n 2) N-Way \n")) % 3

		# whether or not to read from a file, clamp from 0-1
		self.readFromFile = int(input("Read from file? 1/0: ")) % 2

		# get additional settings if it is not reading from a file
		if not self.readFromFile:
			userBytes = input("Enter size of cache in bytes: ")
			self.SIZE = int(int(userBytes) / self.SIZE_PER_ELEMENT)

			self.min = int(input("Enter min element value: "))
			self.max = int(input("Enter max element value: "))
		else:
			with open(self.FILE, 'r') as infile:
				self.SIZE = int(infile.readline())
			infile.close()

		# sets the type of cache
		if userSelect is 0:
			self.cache = self.direct
		elif userSelect is 1:
			self.cache = self.full
		elif userSelect is 2:
			self.cache = self.n_way
			self.ASSOCIATIVITY = int(input("Set associativity: "))
			self.cache.ASSOCIATIVITY = self.ASSOCIATIVITY
	
	def __init__(self):
		# get user customization
		self.user_control()
		# set the cache size
		self.cache.SIZE = self.SIZE

		numElements = self.cache.SIZE

		# initialize the cache
		if self.cache is not self.n_way:
			self.cache.cache = [None] * self.SIZE
			if self.cache is self.full:
				self.cache.accessOrder = [None] * self.SIZE
		else:
			self.cache.cache = [[None] * self.ASSOCIATIVITY for i in range(self.SIZE)]

		if self.readFromFile:
			numElements = len(open(self.FILE).readlines()) - 1

		print("**********\nSimulating cache with " + str(numElements) + " elements \n**********")
		
		# start timer
		self.TIME = time.perf_counter()

		#######################################################################
		if self.readFromFile is 0:
			i = 0
			while(i < self.cache.SIZE):
				# temporal locality
				n = int(r.random() * self.max + self.min)
				self.cache.search(n)
				i += 1
		else:
			# spacial locality
			with open(self.FILE, 'r') as infile:
				i = 1
				for x in infile:
					if i > 1:
						self.cache.search(int(x))
					i += 1
			infile.close()
		#######################################################################

		# prints the type of cache used
		print(type(self.cache))

		# prints number of hits
		print("Hits: " + str(self.cache.hits))

		# prints number and types of misses
		print("Cold Misses: " + str(self.cache.coldMisses))
		if self.cache is self.direct:
			print("Conflict Misses: " + str(self.cache.conflictMisses))
		if self.cache is self.full or self.cache is self.n_way:
			print("Capacity Misses: " + str(self.cache.capacityMisses))

		# prints hit rate
		print("Hit rate: " + str(int(self.cache.hit_rate() * 1000000) / 10000) + "%\n")
		
		# print total time 
		print("Time Elapsed {:.2f}".format(time.perf_counter() - self.TIME) + " seconds")
		print("**********\n")

instance = CacheSim()