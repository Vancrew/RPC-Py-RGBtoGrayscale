from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib
import math, pickle, Image

def terima(n,f):
     with open("c.jpg", "wb") as handle:
          handle.write(n.data)
     img = Image.open('c.jpg').convert('LA')
     img.save('c.png')
     with open("c.png", "rb") as handle:
         return xmlrpclib.Binary(handle.read())

def terima2(n):
     with open("cd.jpg", "wb") as handle:
          handle.write(n.data)
     img = Image.open('cd.jpg').convert('LA')
     img.save('cd.png')
     with open("cd.png", "rb") as handle:
         return xmlrpclib.Binary(handle.read())

def today():
     today = datetime.datetime.today()
     return xmlrpclib.DateTime(today)


server = SimpleXMLRPCServer(("0.0.0.0", 8000))
print "Listening on port 8000..."
server.register_function(terima, 'terima')
server.register_function(today, 'today')
server.register_function(terima2,'terima2')

server.serve_forever()
