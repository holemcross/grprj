#Python Server

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from listparser import loadCSVData
from listparser import sortByGender
from listparser import sortByBirth
from listparser import sortByLastNameDSC
from listparser import fetch_get_records

server_address = ('localhost', 8000)

class GrpojRequestHandler(BaseHTTPRequestHandler):

	#Routes

	def do_GET(self):
		print(self.path)
		# GET /records/name
		if self.path == "/records/name":
			self.make_get_json_wrapper( sortByLastNameDSC(fetch_get_records()))

		# GET /records/birthdate	
		elif self.path == "/records/birthdate":
			self.make_get_json_wrapper( sortByBirth(fetch_get_records()))

		# GET /records/gender
		elif self.path == "/records/gender":
			self.make_get_json_wrapper( sortByGender(fetch_get_records()))

	def do_POST(self):
		if self.path == "/records":
			pass
	def make_get_json_wrapper(self, jsonStr):

		#Stringify
		result = "{"
		for o in jsonStr:
			result+= o.jsonDumps()
			result+=","
		result = result[:-1]
		result +="}"


		self.send_response(200)

		self.send_header("Content-type", 'application/json')
		self.end_headers()

		self.wfile.write(bytes(result, "utf-8"))

if __name__ == '__main__':
	#pass
	print("Server go!")
	server = HTTPServer(("", 8000), GrpojRequestHandler)
	server.serve_forever()