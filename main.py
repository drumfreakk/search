import binary
import sequential
import random

try:
	maxG = 1000**100

	#maxG = int(input("Maximum range: "))

	a = int(input("A: "))
	b = int(input("B: "))

	maxG = a**b
	
	goal = random.randrange(maxG)
	
	print("goal:")
	print(goal)
	print("binary:")
	print(binary.search(goal, maxG))
	print("sequential:")
	print(sequential.search(goal))
except KeyboardInterrupt:
	print("exitted")
except OverflowError:
	print("overflow")
