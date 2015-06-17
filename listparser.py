# Python File
# ListParser

def main(argv):
	src ="";
	try:
		opts, args =getopt.getopt(argv, "hg:d", ["help", "source="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-s", "--source"):
			src = arg

	# DO WORK HERE

def loadCSVData(path):
	dataObj = open( path, "r") #Read only
	dataString = dataObj.read()
	dataObj.close()

	return parseDataStringWithDelimiter(dataString, ',')

def parseData(data):
	#Insert Work Here
	dataObj = open( data, "r") #Read only
	dataString = dataObj.read()
	dataObj.close()

	csvArray = parseCSV(dataString)
	pipeArray = parsePipe(dataString)
	pareseSpace = pareseSpace(dataString)

	mergedList = []
	mergedList.append(csvArray)
	mergedList.append(pipeArray)
	mergedList.append(pareseSpace)

	#Print Sort
	genderSorted = sortByGender(mergedList)
	birthSorted = sortByBirth(mergedList)
	lastNameSorted = sortByLastNameDSC(mergedList)

	print(genderSorted)
	print(birthSorted)
	print(lastNameSorted)


def parseDataStringWithDelimiter(dataString, delimiter):

	#TODO Implement validation
	splitList = dataString.split( delimiter )
	objList = []
	print(objList)

	for obj in splitList:
		# Append strips to new list
		# Work around for issue with setting value instead of reference
		objList.append( obj.replace(' ', '') )
	
	print(objList)
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
	return sorted(personList, key=attrgetter('gender','lastName','firstname'))

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

