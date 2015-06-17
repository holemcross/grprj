#Tester

import unittest
from listparser import Person
from listparser import loadCSVData

class DefaultPersonTestCase(unittest.TestCase):

	def setUp(self):
		#self.person = Person('LastName','FirstName', 'Gender', 'FavoriteColor', 'DateOfBirth')
		self.person = Person('Jane', 'Mary', 'F', 'Blue', '1/2/1993')
		self.csvPath = "testFiles/csvsample.txt"
		self.pipePath = "testFiles/pipesample.txt"
		self.spacePath = "testFiles/spacesample.txt"

	def tearDown(self):
		#self.person.dispose()
		self.person = None
		self.csvPath = None
		self.pipePath = None
		self.spacePath = None

	#def test_parser_import(self):

class ImportTest(DefaultPersonTestCase):

	def test_csv_import(self):
		print("test_csv_import")
		testPerson = loadCSVData(self.csvPath)
		self.assertIsNotNone(testPerson, "Import Error")
		self.assertEqual( testPerson.lastName, self.person.lastName, "Last Name Mis-Match")
		self.assertEqual( testPerson.firstName, self.person.firstName, "First Name Mis-Match")
		self.assertEqual( testPerson.gender, self.person.gender, "Gender Mis-Match")
		self.assertEqual( testPerson.favColor, self.person.favColor, "FavColor Mis-Match")
		self.assertEqual( testPerson.dob, self.person.dob, "DOB Mis-Match")

	def runTest(self):
		test_csv_import(self)

#class SortTest(DefaultPersonTestCase):		
	#def test_gender_sort(self):

if __name__ == '__main__':
	unittest.main()