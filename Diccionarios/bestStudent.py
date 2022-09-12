def bestStudent(l):
	if len(l) == 0:
		print("The student list is empty")
	else:
		resultat = {}
		
		for subllista in l:
			resultat[subllista[0]] = sum(subllista[1]) / float(len(subllista))
			claus = resultat.keys()
			mx = claus[0]
			for clau in claus:
				if resultat[clau] > resultat[mx]:
					mx = clau
		print("The best student is", mx, "and its score is", resultat[mx])

bestStudent([[1, [10.0, 8.0]], [2, [5.0, 5.0]]])

# Devuelve cual estudiante tiene la mejor media de notas