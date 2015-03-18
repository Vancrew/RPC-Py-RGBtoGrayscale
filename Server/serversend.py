from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib
import math, pickle, Image

def kirim():
     with open("a.jpg", "rb") as handle:
         return xmlrpclib.Binary(handle.read())
def terima(n):
     with open("c.jpg", "wb") as handle:
          handle.write(n.data)
     img = Image.open('c.jpg').convert('LA')
     img.save('c.png')
     with open("c.png", "rb") as handle:
         return xmlrpclib.Binary(handle.read())
def today():
     today = datetime.datetime.today()
     return xmlrpclib.DateTime(today)
def quadratic(a, b, c):
    """Determine `x` values satisfying: `a` * x*x + `b` * x + c == 0"""
    b24ac = math.sqrt(b*b - 4.0*a*c)
    return list(set([ (-b-b24ac) / 2.0*a, (-b+b24ac) / 2.0*a ]))
def ss(buf,huf):
     a = pickle.loads(buf)
     b = pickle.loads(huf)
     print a
     print "-----------------------"
     print b

def gray(img):
     img.convert('LA')
     img.save('ji.jpg')
     


server = SimpleXMLRPCServer(("localhost", 8000))
print "Listening on port 8000..."
server.register_function(kirim, 'kirim')
server.register_function(terima, 'terima')
server.register_function(today, 'today')
server.register_function(quadratic, 'quadratic')
server.register_function(ss,'ss')
server.register_function(gray,'gray')

server.serve_forever()
