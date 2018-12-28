def search(goal):
	prod = 1.0
	sin = 1

	step = 1

	while goal != prod:
		step += 1
		if(prod < goal):
			prod += 1.0 / sin
		elif(prod >  goal):
			prod -= 1.0 / sin
			sin = sin * 10

	return step
