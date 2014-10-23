#Matt Koppelman
#GIS 501
#Lab 3 Problem 2



TextFile = open(r"C:\Users\Matt\Documents\UWTacoma\GIS501\GitHub\Lab_3\Lab3_Files\GIS_is_the_best.txt", 'r')

TotalCount, ScienceCount, SystemsCount = 0, 0, 0

for word in TextFile.read().split(" "):
	if word.lower() == "systems":
		SystemsCount = SystemsCount + 1
	elif word.lower() == "science":
		ScienceCount = ScienceCount + 1
	TotalCount += 1


print "Total words: " + str(TotalCount)
print "Total System Count: " + str(SystemsCount)
print "Total Science Count: " + str(ScienceCount)
		
		
