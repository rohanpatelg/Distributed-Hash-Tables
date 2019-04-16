#!/bin/python3
# CODE not tested !!!!!!!!!!!!!!!!!!!!!!
# overall login is prepared : check the remoteNode file also
import sys
import json
import socket
import random
import time
import threading

from remoteNode import *
from address import *
import hashlib

def hash_(str):
	result = hashlib.md5(str.encode())
	x = int(result.hexdigest(),16)
	return x%pow(2,10)
	
class BackGroundProcess(threading.Thread):
	def __init__(self, obj, method):
		threading.Thread.__init__(self)
		self.obj_ = obj
		self.method_ = method

	def run(self):
		getattr(self.obj_, self.method_)()

class Node:
	def __init__(self):
		self._threads = {}

	def start(self):
		self._threads['someOther1'] = BackGroundProcess(self, 'someOther1')
		self._threads['someOther2'] = BackGroundProcess(self, 'someOther2')
		for key in self._threads:
			self._threads[key].start()

	def join(self):
		for key in self._threads:
			self._threads[key].join()

	def someOther1(self):
		i = 0
		while i < 1:
			print("Hello1")
			i = i  + 1
	def someOther2(self):
		print("Hello2")



class A:
	pass




if __name__ == "__main__":
	local = Node()
	local.start()
	local.join()
	# print("\n\n")

	# a = Address("127.0.0.1","1111")
	# b = Address("127.0.0.1","1115")
	# c = Address("127.0.0.1","1200")
	
	

	# aa = RemoteNode(a)
	# bb = RemoteNode(b)
	# cc = RemoteNode(c)

	# print(aa.getIdentifier(),bb.getIdentifier(),cc.getIdentifier())
	

	# print(inrange(100,1024,200))

	# print(aa)
	# print(bb)
	# print(cc)

	# print("xx : ",1," dlsknd",3)

	a = A()
	str(a.__class__)
