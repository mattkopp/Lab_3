#Matt Koppelman
#GIS 501
#Lab 3 Problem 3



TextFile = open(r"C:\Users\Matt\Documents\UWTacoma\GIS501\GitHub\Lab_3\Lab3_Files\GIS_is_the_best.txt", 'r')
NewText = open(r"C:\Users\Matt\Documents\UWTacoma\GIS501\GitHub\Lab_3\Lab3_Files\GIS_is_the_best_new.txt", 'w')


for word in TextFile.read().split(" "):
	if word == "Science":
		NewText.write('System ')
	elif word == "science":
		NewText.write('system ')
	else:
		NewText.write(word + ' ')