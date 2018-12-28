def search(goal, maxG):

	prod = int(maxG / 2)

	maxS = maxG
	minS = 0
	step = 0

	while prod != goal:
		step += 1
		if prod < goal:
			minS = prod
		if prod > goal:
			maxS = prod
		prod = int((maxS - minS) / 2) + minS
	return step

