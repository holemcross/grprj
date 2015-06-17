#Tester

import unittest
from listparser import Person
from listparser import loadCSVData
from listparser import sortByGender
from listparser import sortByBirth
from listparser import sortByLastNameDSC

class DefaultPersonTestCase(unittest.TestCase):

	def setUp(self):
		#self.person = Person('LastName','FirstName', 'Gender', 'FavoriteColor', 'DateOfBirth')
		self.person = Person('Jane', 'Mary', 'F', 'Blue', '1/2/1993')
		self.csvPath = "testFiles/csvsample.txt"
		self.pipePath = "testFiles/pipesample.txt"
		self.spacePath = "testFiles/spacesample.txt"
		self.csv1Path = "testFiles/csv_01.txt"
		self.csv2Path = "testFiles/csv_02.txt"
		self.csv3Path = "testFiles/csv_03.txt"

	def tearDown(self):
		#self.person.dispose()
		self.person = None
		self.csvPath = None
		self.pipePath = None
		self.spacePath = None
		self.csv1Path = None
		self.csv2Path = None
		self.csv3Path = None

	#def test_parser_import(self):

class ImportTest(DefaultPersonTestCase):

	# Import Test
	def test_csv_import(self):

		testPerson = loadCSVData(self.csvPath)
		self.assertIsNotNone(testPerson, "Import Error")
		self.assertEqual( testPerson.lastName, self.person.lastName, "Last Name Mis-Match")
		self.assertEqual( testPerson.firstName, self.person.firstName, "First Name Mis-Match")
		self.assertEqual( testPerson.gender, self.person.gender, "Gender Mis-Match")
		self.assertEqual( testPerson.favColor, self.person.favColor, "FavColor Mis-Match")
		self.assertEqual( testPerson.dob, self.person.dob, "DOB Mis-Match")

	# Sort Tests
	def test_sort_by_gender(self):

		masterList = []
		masterList.append(loadCSVData(self.csv1Path))
		masterList.append(loadCSVData(self.csv2Path))
		masterList.append(loadCSVData(self.csv3Path))
		sortedList = sortByGender(masterList)

		self.assertEqual( sortedList[0].lastName, 'Lopez', "First Person out of order")
		self.assertEqual( sortedList[1].lastName, 'Smith', "Second Person out of order")
		self.assertEqual( sortedList[2].lastName, 'Zebra', "Third Person out of order")

	def test_sort_by_birth(self):

		masterList = []
		masterList.append(loadCSVData(self.csv2Path))
		masterList.append(loadCSVData(self.csv1Path))
		masterList.append(loadCSVData(self.csv3Path))
		sortedList = sortByBirth(masterList)

		self.assertEqual( sortedList[0].lastName, 'Smith', "First Person out of order")
		self.assertEqual( sortedList[1].lastName, 'Lopez', "Second Person out of order")
		self.assertEqual( sortedList[2].lastName, 'Zebra', "Third Person out of order")

	def test_sort_by_last_name_dsc(self):

		masterList = []
		masterList.append(loadCSVData(self.csv2Path))
		masterList.append(loadCSVData(self.csv1Path))
		masterList.append(loadCSVData(self.csv3Path))
		sortedList = sortByLastNameDSC(masterList)

		self.assertEqual( sortedList[0].lastName, 'Zebra', "First Person out of order")
		self.assertEqual( sortedList[1].lastName, 'Smith', "Second Person out of order")
		self.assertEqual( sortedList[2].lastName, 'Lopez', "Third Person out of order")

	def runTest(self):
		test_csv_import(self)
		test_sort_by_gender(self)
		test_sort_by_birth(self)
		test_sort_by_last_name_dsc(self)

#class SortTest(DefaultPersonTestCase):		
	#def test_gender_sort(self):

if __name__ == '__main__':
	unittest.main()