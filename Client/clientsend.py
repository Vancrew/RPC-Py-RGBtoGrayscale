import xmlrpclib, pickle, cv2, Image, os, glob, timeit

proxy = xmlrpclib.ServerProxy("http://localhost:8000/")


"""
with open("b.jpg", "wb") as handle:
    handle.write(proxy.kirim().data)
"""

os.chdir("image")
start = timeit.default_timer()
for file in glob.glob("*.*"):
    try:
        with open("../gray/" + file, "wb") as han:
            with open(file, "rb") as hi:
                han.write(proxy.terima(xmlrpclib.Binary(hi.read())).data)
    except:
        print "--"
stop = timeit.default_timer()

time = stop - start

print "Waktu total = " + str(time)

"""
try:
    with Image.open('b.jpg') as img:
        proxy.gray(img)
except:
    print "ppppp"
"""

"""hi.write(proxy.kirim().data)
"""



print proxy.quadratic(2, -4, 0)

"""a = cv2.imread("s.jpg")
wahyu = []
wahyu.append(a)
x = pickle.dumps(wahyu)
y = pickle.dumps(a)
proxy.ss(x,y)
"""
