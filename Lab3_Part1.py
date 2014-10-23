#Matt Koppelman
#GIS 501
#Lab 3 Problem 1



import os

FileLocation = "C:/Users/Matt/Documents/UWTacoma/GIS501/GitHub/Lab_3/Lab3_Files/text_files_Copy/"

for FileNames in os.listdir(FileLocation): 
	print FileNames
	MyFiles = FileNames.split('.')
	print MyFiles
	if MyFiles[1] == 'txt':
		os.rename(FileLocation + FileNames, 'file_' + FileNames.lower())
	else:
		os.rename(FileLocation + FileNames, 'file_' + MyFiles[0].lower()+ ".txt")

		

		
