def moveTower(h, f, t, c):
	if h >= 1:
		moveTower(h-1, f, c, t)
		print(h, f, t)
		moveTower(h-1, c, t, f)

moveTower(2,"1","3","2")
