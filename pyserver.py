#Python Server

import SimpleHTTPServer
import BaseHTTPServer
import list

server_address = ('localhost', 8000)

class grpojRequestHandler(BaseHTTPRequestHandler):

	#Routes

	def do_GET(self):
		
		# GET /records/name
		if self.path == "/records/name":
			make_get_json_wrapper(self,"[]")

		# GET /records/birthdate	
		elif self.path == "/records/birthdate":
			self.send_response(200)
			self.send_header("Content-type", 'application/json')
			self.end_headers()
			self.wfile.write(bytes("Text Goes here!"))

		# GET /records/gender
		elif self.path == "/records/gender":
			self.send_response(200)
			self.send_header("Content-type", 'application/json')
			self.end_headers()
			self.wfile.write(bytes("Text Goes here!"))
		else
			print("Error!")
	def do_POST(self):
		if self.path == "/records":
			pass
	def make_get_json_wrapper(self, jsonStr):
		self.send_response(200)
			self.send_header("Content-type", 'application/json')
			self.end_headers()
			self.wfile.write(bytes(jsonStr))