# Python File
# ListParser

import getopt
from operator import attrgetter

def main():

	csvPathList = []
	pipePathList =[]
	spacePathList =[]
	csvList = []
	pipeList =[]
	spaceList =[]
	masterList =[]

	try:
		opts, args =getopt.getopt(sys.argv[1:], "hc:", ["help", "csv="])
	except getopt.GetoptError:
		print("Error!")
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-c", "--commaseperated"):
			csvPathList.append(arg)
		elif opt in ("-p","--pipe"):
			pipePathList.append(arg)
		elif opt in ("-s", "--space"):
			spacePathList.append(arg)

	#Load Files from Paths
	for item in csvPathList:
		masterList.append(loadCSVData(item))

	for item in pipePathList:
		masterList.append(loadPipeData(item))

	for item in spacePathList:
		masterList.append(loadSpaceData(item))

	#Print Views
	genderSorted = sortByGender(masterList)
	birthSorted = sortByBirth(masterList)
	lastNameSorted = sortByLastNameDSC(masterList)

	print(genderSorted)
	print(birthSorted)
	print(lastNameSorted)

def loadCSVData(path):
	dataObj = open( path, "r") #Read only
	dataString = dataObj.read()
	dataObj.close()

	return parseDataStringWithDelimiter(dataString, ',')

def loadPipeData(path):
	dataObj = open( path, "r") #Read only
	dataString = dataObj.read()
	dataObj.close()

	return parseDataStringWithDelimiter(dataString, '|')

def loadSpaceData(path):
	dataObj = open( path, "r") #Read only
	dataString = dataObj.read()
	dataObj.close()

	return parseDataStringWithDelimiter(dataString, ' ')

def parseDataStringWithDelimiter(dataString, delimiter):

	#TODO Implement validation
	splitList = dataString.split( delimiter )
	objList = []
	for obj in splitList:
		# Append strips to new list
		# Work around for issue with setting value instead of reference
		objList.append( obj.replace(' ', '') )

	return Person(objList[0],objList[1],objList[2],objList[3],objList[4])

def parseCSV(dataString):
	#Insert Work Here
	return parseDataStringWithDelimiter(dataString, ',')

def parsePipe(data):
	#Insert Work
	return parseDataStringWithDelimiter(dataString, '|')

def pareseSpace(data):
	#Insert Work
	return parseDataStringWithDelimiter(dataString, ' ')

def sortByGender(personList):
	#Then last name
	return sorted(personList, key=attrgetter('gender','lastName','firstName'))

def sortByBirth(personList):
	#Ascending
	return sorted(personList, key=attrgetter('dob'))

def sortByLastNameDSC(personList):
	#descending
	return sorted(personList, key=attrgetter('lastName', 'firstName'), reverse=True)

# Person Class
class Person:
	def __init__(self, lastName, firstName, gender, favColor, dob):
		self.lastName = lastName
		self.firstName = firstName
		self.gender = gender
		self.favColor = favColor
		self.dob = dob
	def __repr__(self):
		return repr((self.lastName, self.firstName, self.gender, self.favColor, self.dob))

# Main
if __name__ == '__main__':
	main()
