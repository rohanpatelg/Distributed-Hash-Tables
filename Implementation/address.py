from config import *
import hashlib

def hash_(str):
	result = hashlib.md5(str.encode())
	x = int(result.hexdigest(),16)
	return x

# Helper function to determine if a key falls within a range
def inrange(c, a, b):
	# is c in [a,b)?, if a == b then it assumes a full circle
	# on the DHT, so it returns True.
	a = a % SIZE
	b = b % SIZE
	c = c % SIZE
	if a < b:
		return a <= c and c < b
	return a <= c or c < b

class Address:
	def __init__(self,*args):
		self.ip = args[0]
		self.port = int(args[1])

	def __hash__(self):
		# python3 hash() gives same value in one python invocation
		return hash_(("%s:%s" % (self.ip, self.port))) % SIZE

	def __cmp__(self, other):
		return other.__hash__() < self.__hash__()

	def __eq__(self, other):
		return other.__hash__() == self.__hash__()

	def __str__(self):
		return "[\"%s\", %s]" % (self.ip, self.port)